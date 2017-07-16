import lib.storage.Location


class VerifiedLocation(Location):

    def _addSource(self, name, value):
        data = self._get_obj()
        if not data[name]:
            data[name] = []
        data[name].append(value)

        self._storage.save({'code': self.code}, data)

    def addWikiSource(self, code):
        self._addSource('wiki', code)

    def addGoogleMapSource(self, code):
        self._addSource('gmaps', code)

    def getWikiSources(self):
        data = self._get_obj()
        return data.wiki if data.wiki else []

    def getGoogleMapSources(self):
        data = self._get_obj()
        return data.gmaps if data.gmaps else []