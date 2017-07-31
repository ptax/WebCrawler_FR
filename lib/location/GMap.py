from lib.location.External import External


class GMap(External):
    
    def __init__(self, code, storage):
        super(GMap, self).__init__(code, storage=storage, type='gmap')