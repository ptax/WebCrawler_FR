class MongoDB:

    def __init__(self, db, hash_lib):
        self._db = db
        self._hash_lib = hash_lib

    def has(self, url, headers=None):
        hash = self.make_hash(url, headers=headers)
        return self._db.exists({"filename": hash})

    def get(self, url, headers=None):
        result = ''
        if self.has(url, headers):
            hash = self.make_hash(url, headers=headers)
            document = self._db.find_one({'filename': hash})
            result = document.read()
        return result

    def set(self, url, content, headers=None):
        hash = self.make_hash(url, headers=headers)
        return self._db.put(content, filename=hash)

    def make_hash(self, url, headers=None):
        return self._hash_lib.make(url, headers)

    def remove(self, url, headers=None):
        if self.has(url, headers):
            document = self._db.find_one({'filename': self.make_hash(url, headers=headers)})
            self._db.delete(document._id)
