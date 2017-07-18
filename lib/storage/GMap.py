import lib.storage.External


class GMap(ExternalLocation):
    
    def __init__(self, code, storage):
        super(WikiLocation, self).__init__(code, storage=storage, type='gmap')