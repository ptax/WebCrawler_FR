from lib.location.External import External


class Wiki(External):

    TYPE = 'wiki'

    def __init__(self, code, storage):
        super(Wiki, self).__init__(code, storage=storage, type=self.TYPE)