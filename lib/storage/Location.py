class Location:

    def __init__(self, code, storage):
        self._storage = storage
        self.code = code

    def _get_obj(self):
        return self._storage.findOne({'code': self.code})