from lib.loader.HttpRequest import HttpRequest as HttpRequest


class HttpRequestWithCache(HttpRequest):
    def __init__(self, storage):
        self._storage = storage

    def load(self, url, headers=None, use_cache=True):
        result = ''
        code = 200
        if use_cache:
            result = self.from_cache(url, headers=headers)
        if not result:
            result, code = super(HttpRequestWithCache, self).load(url, headers=headers)
            self.to_cache(url, content=result, headers=headers)

        return result, code

    def from_cache(self, url, headers=None):
        return self._storage.get(url, headers=headers)

    def to_cache(self, url, content, headers=None):
        self._storage.set(url=url, content=content, headers=headers)