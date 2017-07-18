import lib.storage.Location


class External(Location):
    
    def __init__(self, code, storage, type):
        super(External, self).__init__(code, storage=storage)
        self._type = type