from lib.hashlib.sha512 import sha512
from pymongo import MongoClient
from lib.location.Wiki import Wiki
from lib.location.GMap import GMap


class Storage:

    def __init__(self, storage_config):
        self._hash_lib = sha512()
        connection = MongoClient(storage_config['host'], storage_config['port'])
        self._db = connection.location

    def wiki(self, url):
        code = self._hash_lib.make(url)
        return Wiki(code=code, storage=self._db)


    def gmaps(self, code):
        return GMap(code=code, storage=self._db)

    def gmaps_collection(self):
        return self._db[GMap.TYPE]

    def wiki_collection(self):
        return self._db[Wiki.TYPE]