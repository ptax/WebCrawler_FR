class Location:

    def __init__(self, code, storage):
        self._storage = storage
        self._query = {'code': code}
        self._new = False
        self._document = self._get_or_create_doc()


    def _get_or_create_doc(self):
        document = self._storage.find_one(self._query)
        if not document:
            self._storage.insert_one(self._query)
            document = self._storage.find_one(self._query)
            self._new = True

        return document

    def is_new(self):
        return self._new

    def update(self, new_data):
        new_doc = {**self._get_or_create_doc(), **new_data}
        self._storage.update_one(self._query, {'$set': new_doc})