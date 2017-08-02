from lib.loader.storage.MongoDB import MongoDB


class ComplexData(MongoDB):

    def __init__(self, db, hash_lib):
        super(ComplexData, self).__init__(db=db)
        self._hash_lib=hash_lib

    def has(self, params):
        return super(ComplexData, self).has(self.make_hash(params))

    def get(self, params):
        return super(ComplexData, self).get(key=self.make_hash(params))


    def set(self, content, params):
        return super(ComplexData, self).set(key=self.make_hash(params), content=content)

    def make_hash(self, params):
        return self._hash_lib.make(params)

    def remove(self, **params):
        if self.has(params):
            super(ComplexData, self).remove(key=self.make_hash(params))