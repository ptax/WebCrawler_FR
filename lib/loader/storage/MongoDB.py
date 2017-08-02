class MongoDB:

    def __init__(self, db):
        self._db = db

    def has(self, key):
        return self._db.exists({"filename": key})

    def get(self, key):
        result = None
        document = self._db.find_one({'filename': key})
        if document:
            result = self.unserialyse(document.read())
        return result

    def set(self, key, content):
        return self._db.put(self.serialyse(content), filename=key)

    def remove(self, key):
        document = self._db.find_one({'filename': key})
        if document:
            self._db.delete(document._id)

    @staticmethod
    def serialyse(content):
        return content

    @staticmethod
    def unserialyse(content):
        return content