class Config:

    def get(self, name):
        return self._cfg[name] if name in self._cfg else None
