from lib.location.Location import Location


class External(Location):
    
    def __init__(self, code, storage, type):
        collection = storage[type]
        super(External, self).__init__(code, storage=collection)
