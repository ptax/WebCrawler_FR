import lib.loader.Loader


class LoaderWithCache(Loader):
    def __init__(self, loader_lib, storage):
        super(LoaderWithCache, self).__init__(loader_lib)
        self._storage = storage

    def load(self, url, headers=none, use_cache=true):
        result = ''
        if use_cache:
            result = self._storage.get(url, headers=headers)

        if not result:
            result = super(LoaderWithCache, self).load(url, headers=headers)
            self._storage.set(url, content=result, headers=headers)

        return result
