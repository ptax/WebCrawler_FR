class Config:

    def __init__(self):
        pass

    def get(self, name):
        return self._cfg[name] if name in self._cfg else None
