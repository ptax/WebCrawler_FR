class MongoDBStorage:

    def __init__(self, mongodb_driver, hash_lib):
        self._driver = mongodb_driver
        self._hash_lib = hash_lib

    def get(self, url, headers=none):
        hash = self.make_hash(url, headers=headers)
        return self._driver.find_one({'key': hash})

    def set(self, url, content, headers=none):
        hash = self.make_hash(url, headers=headers)
        self._driver.set(hash, content)

    def make_hash(self, url, headers=none):
        return '{0}_{1}'.format(self._hash_lib.sha512(url).hexdigest(), self._hash_lib.sha512(headers).hexdigest())