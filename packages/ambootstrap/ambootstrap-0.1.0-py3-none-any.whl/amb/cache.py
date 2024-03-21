import logging
import os
import tempfile
import hashlib
import urllib.request
from urllib.error import HTTPError

try:
    from tqdm import tqdm
except ImportError:
    tqdm = None


def _progress(t):
    def update_to(block=1, blocksize=1, totalsize=None):
        if totalsize is not None:
            t.total = totalsize
        t.update(block * blocksize - t.n)

    return update_to


class DownloadError(Exception):
    def __init__(self, error):
        if isinstance(error, HTTPError):
            url = error.filename
            message = f'Could not fetch {url}: {error}'
        else:
            raise
        super().__init__(message)


class Cache:
    def __init__(self, path=None):
        self.logger = logging.getLogger('cache')
        self.path = path
        if self.path is None:
            self.tempdir = tempfile.TemporaryDirectory(prefix='pmb2-')
            self.path = self.tempdir.name
        self.logger.debug(f'Initialize cache at {path}')

    def fetch(self, url, max_age=None):
        self.logger.debug(f'downloading {url}')
        cache_key = hashlib.sha1(url.encode('utf-8')).hexdigest()
        target = os.path.join(self.path, "http")
        if not os.path.isdir(target):
            os.makedirs(target)
        target = os.path.join(target, cache_key)

        if os.path.isfile(target):
            return target
        try:
            if tqdm:
                with tqdm(unit='B', unit_scale=True, unit_divisor=1024, miniters=1, desc=url, delay=1) as t:
                    urllib.request.urlretrieve(url, target, reporthook=_progress(t))
            else:
                urllib.request.urlretrieve(url, target)
        except HTTPError as e:
            raise DownloadError(e)
        return target

    def exists(self, cache_key, category):
        return os.path.isfile(self.get(cache_key, category))

    def get(self, cache_key, category):
        return os.path.join(self.path, category, cache_key)

    def put(self, cache_key, category, data):
        target = os.path.join(self.path, category)
        if not os.path.isdir(target):
            os.makedirs(target)
        target = os.path.join(target, cache_key)

        if isinstance(data, bytes):
            with open(target, "wb") as handle:
                handle.write(data)
        else:
            with open(target, "w") as handle:
                handle.write(data)
        return target
