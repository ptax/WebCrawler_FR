from lib.loader.Loader import Loader as Loader


class LoaderWithCache(Loader):
    def __init__(self, storage):
        self._storage = storage

    def load(self, url, headers=None, use_cache=True):
        result = ''
        if use_cache:
            result = self.from_cache(url, headers=headers)

        if not result:
            result, code= super(LoaderWithCache, self).load(url, headers=headers)
            self.to_cache(url, content=result, headers=headers)

        return result

    def from_cache(self, url, headers=None):
        return self._storage.get(url, headers=headers)

    def to_cache(self, url, content, headers=None):
        self._storage.set(url, content=content, headers=headers)