import lib.storage.External


class Wiki(ExternalLocation):
    
    def __init__(self, code, storage):
        super(Wiki, self).__init__(code, storage=storage, type='wiki')