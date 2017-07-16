class Loader:

    def __init__(self, loader_lib):
        self._loader_lib = loader_lib

    def load(self, url, headers=none):
        self._loader_lib.Request(url, headers)
        return urllib2.urlopen(req)
