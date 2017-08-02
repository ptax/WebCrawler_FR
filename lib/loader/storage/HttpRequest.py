from lib.loader.storage.MongoDB import MongoDB


class HttpRequest(MongoDB):

    def __init__(self, db, hash_lib):
        super(HttpRequest, self).__init__(db=db)
        self._hash_lib = hash_lib

    def has(self, url, headers=None):
        return super(HttpRequest, self).has(self.make_hash(url, headers=headers))

    def get(self, url, headers=None):
        result = super(HttpRequest, self).get(self.make_hash(url, headers=headers))

        return result

    def set(self, url, content, headers=None):
        return super(HttpRequest, self).set(self.make_hash(url, headers=headers), content=content)

    def make_hash(self, url, headers=None):
        return self._hash_lib.make(url, headers)

    def remove(self, url, headers=None):
        if self.has(url, headers):
            super(HttpRequest, self).remove(self.make_hash(url, headers=headers))
