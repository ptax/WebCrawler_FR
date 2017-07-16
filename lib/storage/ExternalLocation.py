import lib.storage.Location


class ExternalLocation(Location):
    
    def __init__(self, code, storage, type):
        super(ExternalLocation, self).__init__(code, storage=storage)
        self._type = type