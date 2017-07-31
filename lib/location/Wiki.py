from lib.location.External import External


class Wiki(External):
    
    def __init__(self, code, storage):
        super(Wiki, self).__init__(code, storage=storage, type='wiki')