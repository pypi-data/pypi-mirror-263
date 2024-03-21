import datetime
import tarfile
from urllib.parse import urljoin

from amb.cache import Cache


class Package:
    pkgname: str
    pkgver: str
    arch: str
    size: int | None
    installed_size: int | None
    description: str | None
    url: str | None
    license: str | None
    origin: str | None
    maintainer: str | None
    build_time: int | None
    commit: str | None
    provider_priority: int | None
    dependencies: list[str]
    provides: list[str]
    install_if: list[str]
    checksum: str

    def __init__(self, index=None):
        self._index = index
        self.pkgname = ""
        self.pkgver = ""
        self.arch = ""
        self.size = None
        self.installed_size = None
        self.description = None
        self.url = None
        self.license = None
        self.origin = None
        self.maintainer = None
        self.build_time = None
        self.commit = None
        self.provider_priority = None
        self.dependencies = []
        self.provides = []
        self.install_if = []
        self.checksum = ""

    @property
    def build_datetime(self):
        if self.build_time is None:
            return None
        return datetime.datetime.fromtimestamp(self.build_time)

    @property
    def apk_url(self):
        if self._index is None:
            return None
        return f'{self._index.base}/{self.pkgname}-{self.pkgver}.apk'

    def __repr__(self):
        return f'<Package {self.pkgname} {self.pkgver} [{self.arch}]>'


class ApkIndex:
    def __init__(self, url, cache=None):
        self.cache = cache
        if self.cache is None:
            self.cache = Cache()
        self.base = url

        self.packages = {}
        self.pkg_count = 0

        url = urljoin(self.base + "/", 'APKINDEX.tar.gz')
        self.index_file = self.cache.fetch(url)

        if not self.cache.exists("parsed-", "apkindex"):
            self._parse()

    def _parse(self):
        if tarfile.is_tarfile(self.index_file):
            with tarfile.open(self.index_file, "r:gz") as tar:
                with tar.extractfile(tar.getmember("APKINDEX")) as handle:
                    self._parse_iter(handle)
        else:
            with open(self.index_file, "r", encoding="utf-8") as handle:
                self._parse_iter(handle)

    def _parse_iter(self, handle):
        """

        :param handle:
        :return:
        """

        attrib_map = {
            'C': 'checksum',
            'P': 'pkgname',
            'V': 'pkgver',
            'A': 'arch',
            'S': 'size',
            'I': 'installed_size',
            'T': 'description',
            'U': 'url',
            'L': 'license',
            'o': 'origin',
            'm': 'maintainer',
            't': 'build_time',
            'c': 'commit',
            'k': 'provider_priority',
            'D': 'dependencies',
            'p': 'provides',
            'i': 'install_if',
        }
        arrays = ['D', 'p', 'i']
        integers = ['S', 'I', 't', 'k']

        package = Package(index=self)
        for line in handle:
            if line == b'\n':
                if package.pkgname not in self.packages:
                    self.packages[package.pkgname] = {}
                self.packages[package.pkgname][package.pkgver] = package
                self.pkg_count += 1
                package = Package(index=self)
                continue
            key, val = line.decode().split(':', maxsplit=1)
            if key in attrib_map:
                val = val.strip()
                if key in arrays:
                    val = val.split()
                if key in integers:
                    val = int(val)
                setattr(package, attrib_map[key], val)

    def latest(self, pkgname) -> Package | None:
        if pkgname not in self.packages:
            return None
        if len(self.packages[pkgname]) == 1:
            return next(iter(self.packages[pkgname].values()))

    def __getitem__(self, item) -> Package:
        if isinstance(item, tuple):
            return self.packages[item[0]][item[1]]
        elif isinstance(item, str):
            return self.packages[item]

    def __len__(self):
        return self.pkg_count

    def __repr__(self):
        return f'<ApkIndex {self.pkg_count} packages: {self.base}>'


if __name__ == '__main__':
    apkindex = ApkIndex('https://dl-cdn.alpinelinux.org/alpine/edge/main/x86_64')
    print(apkindex.latest('mesa'))
