import lib.loader.Loader


class LoaderWithCache(Loader):
    def __init__(self, loader_lib, storage):
        super(LoaderWithCache, self).__init__(loader_lib)
        self._storage = storage

    def load(self, url, headers=none, use_cache=true):
        result = ''
        if use_cache:
            result = self.from_cache(url, headers=headers)

        if not result:
            result = super(LoaderWithCache, self).load(url, headers=headers)
            self.to_cache(url, content=result, headers=headers)

        return result

    def from_cache(self, url, headers=none):
        return self._storage.get(url, headers=headers)

    def to_cache(self, url, content=result, headers=headers):
        self._storage.set(url, content=content, headers=headers)