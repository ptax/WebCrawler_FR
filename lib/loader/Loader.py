class Loader:

    def __init__(self, loader_lib):
        self._loader_lib = loader_lib

    def load(self, url, headers=none):
        req = self._loader_lib.Request(url, headers)
        return self._loader_lib.urlopen(req)
