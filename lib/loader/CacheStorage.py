class MongoDBStorage:

    def __init__(self, mongoDBDriver, hashLib):
        self._driver = mongoDBDriver
        self._hashLib = hashLib

    def get(self, url, headers=none):
        hash = self.makeHash(url, headers=headers)
        return self._driver.findOne({'key': hash})

    def set(self, url, content, headers=none):
        hash = self.makeHash(url, headers=headers)
        self._driver.set(hash, content)

    def makeHash(self, url, headers=none):
        return '{0}_{1}'.format(self._hashLib.sha512(url).hexdigest(), self._hashLib.sha512(headers).hexdigest())