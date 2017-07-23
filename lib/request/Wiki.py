import lib.request.Request as Request


class Wiki(Request):
    def __init__(self, loader):
        self._loader = loader

