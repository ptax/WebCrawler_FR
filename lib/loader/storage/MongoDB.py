import gzip

class MongoDB:

    def __init__(self, db):
        self._db = db

    def has(self, key):
        return self._db.exists({"filename": key})

    def get(self, key):
        result = None
        document = self._db.find_one({'filename': key})
        if document:
            result = self.deserialize(document.read())
        return result

    def set(self, key, content):
        return self._db.put(self.serialize(content), filename=key)

    def remove(self, key):
        document = self._db.find_one({'filename': key})
        if document:
            self._db.delete(document._id)

    @staticmethod
    def serialize(content):
        return gzip.compress(content, compresslevel=9)

    @staticmethod
    def deserialize(content):
        return gzip.decompress(content)