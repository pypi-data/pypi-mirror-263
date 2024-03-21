import logging
import os

from amb.architecture import host_arch
from amb.cache import Cache
from amb.chroot import Chroot
from amb.logger import init_logging

_cache = Cache()


def init(path, arch=None, branch=None, repository=None):
    if arch is None or arch == "native":
        arch = host_arch().alpine
    if branch is None:
        branch = 'edge'

    if repository is not None:
        base = f'https://dl-cdn.alpinelinux.org/alpine/{branch}'
        temp_r = []
        for r in repository:
            if '/' not in r:
                temp_r.append(f'{base}/{r}')
            else:
                temp_r.append(r)
        repository = temp_r

    logging.info(f'Creating a new {arch} Alpine Linux installation in {path}')

    chroot = Chroot(path, cache=_cache, arch=arch, branch=branch)
    chroot.init_alpine(repositories=repository)


def shell(path):
    logging.info(f"Entering {path} chroot and launching shell")
    chroot = Chroot(path, cache=_cache)
    chroot.shell()


def main():
    global _cache
    import argparse

    parser = argparse.ArgumentParser(description="Alpine Linux bootstrapping tool for mobile platforms")

    parser.add_argument('--verbose', '-v', action='store_true', help='Show more verbose log messages')
    parser.add_argument('--debug', '-V', action='store_true', help='Show the maximum amount of log messages')

    subparsers = parser.add_subparsers(dest='command', required=False, title='sub-commands:',
                                       description='These are the subcommands implemented:')

    init_cmd = subparsers.add_parser('init', help='Start a new installation')
    init_cmd.add_argument('path', help='Path to the installation to create')
    init_cmd.add_argument('--arch', '--architecture', '-A', default='native',
                          help='Installation architecture, defaults to native')
    init_cmd.add_argument('--branch', '-b', default='edge', help='Alpine branch to use, defaults to edge')
    init_cmd.add_argument('--repository', '-X', action='append', help='Add additional repository')
    shell_cmd = subparsers.add_parser('shell', help='Get a shell in an installation')
    shell_cmd.add_argument('path', help='Path to the installation to create')

    subparsers.add_parser('help', help='Display this help text')

    kwargs = vars(parser.parse_args())
    cmd = kwargs.pop('command')

    if cmd == 'help' or cmd is None:
        parser.print_help()
        exit(0)

    # Init logging
    init_logging(verbose=kwargs.pop('verbose'), debug=kwargs.pop('debug'))
    logging.debug(f"Executing the {cmd} command with " + str(kwargs))

    # Initialize the caching system
    xdg_cache_home = os.path.expanduser(os.getenv('XDG_CACHE_HOME', '~/.cache'))
    cache_path = os.path.join(xdg_cache_home, 'ambootstrap')
    os.makedirs(cache_path, exist_ok=True)
    _cache = Cache(cache_path)

    # Dispatch the subcommand to the function with the same name
    globals()[cmd.replace('-', '_')](**kwargs)


if __name__ == '__main__':
    main()
