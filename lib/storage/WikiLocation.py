import lib.storage.ExternalLocation


class WikiLocation(ExternalLocation):
    
    def __init__(self, code, storage):
        super(WikiLocation, self).__init__(code, storage=storage, type='wiki')