class MongoDB:

    def __init__(self, db, hash_lib):
        self._db = db
        self._hash_lib = hash_lib

    def get(self, url, headers=none):
        hash = self.make_hash(url, headers=headers)
        document = self._db.find_one({'code': hash})
        return document.content if 'content' in document else ''

    def set(self, url, content, headers=none):
        hash = self.make_hash(url, headers=headers)
        self._db.set(hash, content)

    def make_hash(self, url, headers=none):
        return self._hash_lib.make(url, headers)

    def remove(self, url, headers=none):
        self._hash_lib.remove({'code': self.make_hash(url, headers=headers)})
