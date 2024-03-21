import logging
import os
import shlex
import shutil
import stat
import subprocess
import tarfile
import tempfile

from amb.apkindex import ApkIndex
from amb.architecture import host_arch, get_arch
from amb.cache import Cache


class ChrootBackend:
    PRIV_CHOWN = 1

    def __init__(self):
        self.logger = logging.getLogger('chroot')

    def run_host(self, cmd: list[str], privileges=0, reason=None, cwd=None, input=None):
        if privileges > 0:
            print(f"\nSuperuser privileges required: {reason}")
            cmd = ['sudo'] + cmd
        self.logger.debug('[host] ' + ' '.join(cmd))
        subprocess.run(cmd, input=input)

    def run(self, cmd: list[str], root=None, input=None, interactive=False):
        command = ['chroot', root] + cmd
        subprocess.run(command, input=input)

    def make_nodes(self, root, nodes):
        script = ''
        for name, nodetype, major, minor, mode in nodes:
            ntype = 'c' if nodetype == stat.S_IFCHR else 'b'
            script += f'mknod -m {mode} dev/{name} {ntype} {major} {minor}; '

        self.run_host(['sh', '-c', script], privileges=1, reason='Create device nodes in the chroot', cwd=root)

    def write(self, root, path, contents, uid=0, gid=0):
        self.run_host(['sh', '-c', ''], privileges=1, input=contents)
        with open(os.path.join(root, path), 'wb') as handle:
            handle.write(contents)

    def make_environment(self):
        path = [
            '/usr/local/sbin',
            '/usr/local/bin',
            '/usr/sbin',
            '/usr/bin',
            '/sbin',
            '/bin',
        ]
        environment = {
            "CHARSET": "UTF-8",
            "HISTFILE": "~/.ash_history",
            "HOME": "/root",
            "LANG": "UTF-8",
            "PATH": ':'.join(path),
            "SHELL": "/bin/ash",
            "TERM": os.getenv("TERM", "linux"),
        }
        return environment


class ChrootBackendUnshare(ChrootBackend):
    def __init__(self, uid_start=100000, uid_count=10000, gid_start=100000, gid_count=10000):
        super().__init__()
        self.uid_start = uid_start
        self.uid_count = uid_count
        self.gid_start = gid_start
        self.gid_count = gid_count

    def run_host(self, cmd: list[str], privileges=0, reason=None, cwd=None, input=None):
        if privileges & ChrootBackend.PRIV_CHOWN:
            # Create a userns to allow chowning files
            unshare = ['unshare',
                       '--user',
                       f'--map-users={self.uid_start},0,{self.uid_count}',
                       f'--map-groups={self.gid_start},0,{self.gid_count}',
                       '--setuid', '0',
                       '--setgid', '0',
                       '--wd', os.path.abspath(cwd),
                       ]

            # The unshare command changes the uid mapping before executing the command.
            # This creates the problem where unshare doesn't have permissions to load
            # the file from the host filesystem anymore. Copy the executable to a
            # tmp filesystem so it should have 777 permissions from the root dir up
            executable = cmd[0]
            workspace = tempfile.TemporaryDirectory(prefix='amb-')
            os.chmod(workspace.name, 0o777)
            tmp_ex = os.path.join(workspace.name, os.path.basename(executable))
            shutil.copy(executable, tmp_ex)
            cmd[0] = tmp_ex

            cmd = unshare + cmd
        self.logger.debug('[host] ' + shlex.join(cmd))
        try:
            subprocess.run(cmd, cwd=cwd, check=True, input=input)
        except subprocess.CalledProcessError as e:
            self.logger.fatal("Failed to launch:")
            self.logger.fatal(shlex.join(cmd))
            exit(1)

    def run(self, cmd: list[str], root=None, input=None, interactive=False):
        unshare = [
            'unshare',
            '--user',
            '--fork',
            '--pid',
            '--mount',
            '--mount-proc',
            f'--map-users={self.uid_start},0,{self.uid_count}',
            f'--map-groups={self.gid_start},0,{self.gid_count}',
            '--setuid', '0',
            '--setgid', '0',
            '--wd', root,
            '--',
        ]
        script = [
            ['mount', '-t', 'proc', 'none', 'proc'],
        ]
        for bind in ['zero', 'null', 'full', 'random', 'urandom']:
            script += [
                ['touch', f'dev/{bind}'],
                ['mount', '-o', 'rw,bind', f'/dev/{bind}', f'dev/{bind}'],
            ]
        script += [['chroot', '.'] + cmd]
        script_oneline = ''
        for c in script:
            script_oneline += shlex.join(c) + ' ; '
        cmd = unshare + ['sh', '-c', script_oneline]
        chroot_name = os.path.basename(root)
        self.logger.debug(f'[{chroot_name}] ' + ' '.join(cmd))
        try:
            subprocess.run(cmd, check=True, input=input, env=self.make_environment())
        except subprocess.CalledProcessError as e:
            self.logger.fatal("Failed to launch:")
            self.logger.fatal(shlex.join(cmd))
            exit(1)

    def make_nodes(self, root, nodes):
        # Device nodes are not created in the unbound scenario. Instead the devices are bind-mounted when creating
        # the chroot so the binds are in the mount namespace.
        pass

    def write(self, root, path, contents, uid=0, gid=0):
        if isinstance(contents, str):
            contents = contents.encode()
        script = ['/bin/sh', '-c', f'cat > {path}']
        self.run(script, input=contents, root=root)


class Chroot:
    repository: ApkIndex | None

    def __init__(self, root, cache=None, arch=None, branch=None, backend=None):
        self.root = root
        self.cache = cache
        if self.cache is None:
            self.cache = Cache()
        self.arch = arch or "x86_64"
        self.branch = branch or "edge"
        self.backend = backend
        if backend is None:
            self.backend = ChrootBackendUnshare()
        elif not isinstance(backend, ChrootBackend):
            raise ValueError("backend needs to be a ChrootBackend subclass")

        self.repository_base = f'https://dl-cdn.alpinelinux.org/alpine/{self.branch}/main'
        self.repository = None
        self.logger = logging.getLogger('chroot')

    def init_alpine(self, packages: list[str] | None = None, repositories: list[str] | None = None):
        """

        :packages: package list to pass to the base install command. If not specified it will default to ["alpine-base"]
        """

        if packages is None:
            packages = ['alpine-base']
        packages = set(packages)

        if repositories is None:
            repositories = [self.repository_base]
        repositories = set(repositories)

        # Initialize the apk.static binary which is used for creating the alpine chroot
        self.repository = ApkIndex(self.repository_base + f'/{self.arch}', cache=self.cache)
        apk_static = self.init_apk_tools_static()

        # Make sure binfmt_misc is available and set-up when a cross-arch chroot is created
        self.setup_binfmt()

        # Create the folder for the new rootfs, 777 permissions are required to allow the
        # mapped uid/gid inside the chroot to work beceause from the perspective inside the
        # chroot the / folder will have an uid/gid that's out of range.
        os.makedirs(self.root, exist_ok=True)
        os.chmod(self.root, 0o777)

        # This is the first part that has to run outside the chroot (because the chroot doesn't exist yet)
        command = [apk_static]
        for r in repositories:
            command.extend(['-X', r])
        command.extend([
            '--update-cache',
            '--allow-untrusted',
            '--arch', self.arch,
            '--root', '.',
            '--initdb',
            'add',
            '--no-interactive',
        ])
        command.extend(packages)
        self.logger.info('Bootstrapping Alpine with apk.static')
        self.backend.run_host(command, privileges=ChrootBackend.PRIV_CHOWN, cwd=self.root)

        # Set up all the extra chroot related stuff
        nodes = [
            ('full', stat.S_IFCHR, 1, 7, 666),
            ('zero', stat.S_IFCHR, 1, 5, 666),
            ('null', stat.S_IFCHR, 1, 3, 666),
            ('random', stat.S_IFCHR, 1, 8, 666),
            ('urandom', stat.S_IFCHR, 1, 9, 666),
        ]
        self.backend.make_nodes(self.root, nodes)

        self.logger.info('Copying over /etc/resolv.conf')
        with open('/etc/resolv.conf', 'r') as handle:
            resolv_conf = handle.read()
        self.backend.write(self.root, "/etc/resolv.conf", resolv_conf)

        self.logger.info('Setting up repositories')
        repo_file = ''
        for url in repositories:
            repo_file += f'{url}\n'
        self.backend.write(self.root, "/etc/apk/repositories", repo_file)

    def init_apk_tools_static(self):
        package = self.repository.latest("apk-tools-static")

        binary_name = f"apk-tools-static-{package.pkgver}"
        if not self.cache.exists(binary_name, "tools"):
            self.logger.info(f'Downloading apk-tools-static {package.pkgver}')
            apk = self.cache.fetch(package.apk_url)
            with tarfile.open(apk, "r:gz") as tar:
                with tar.extractfile(tar.getmember("sbin/apk.static")) as handle:
                    binary = handle.read()

            path = self.cache.put(f"apk-tools-static-{package.pkgver}", "tools", binary)
            os.chmod(path, 0o755)
        self.logger.debug(f'Using apk-tools-static {package.pkgver}')
        return self.cache.get(binary_name, "tools")

    def setup_binfmt(self):
        # Don't mess with binfmt_misc if it's not needed
        if host_arch() == get_arch(alpine=self.arch):
            self.logger.debug('Making a native chroot, binfmt_misc skipped')
            return

        # Check if the binfmt_misc module is ready
        if not os.path.isfile('/proc/sys/fs/binfmt_misc/status'):
            raise RuntimeError("The binfmt_misc module is not loaded")

    def shell(self):
        self.backend.run(['/bin/ash'], root=self.root, interactive=True)


if __name__ == '__main__':
    from pathlib import Path
    from amb.logger import init_logging

    init_logging(debug=True)

    testdir = Path(__file__).parent.parent / 'test-arm'
    logging.info(f"Making chroot in {testdir}")
    test = Chroot(str(testdir), cache=Cache("/workspace"), arch='aarch64')
    test.init_alpine()
