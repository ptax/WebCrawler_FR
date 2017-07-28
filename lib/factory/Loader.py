from lib.loader.LoaderWithCache import LoaderWithCache as LoaderWithCache
from lib.loader.Loader import Loader as LoaderWOCache
from lib.loader.storage.MongoDB import MongoDB as MongoDBStorage
from lib.hashlib.sha512 import sha512

from pymongo import MongoClient
import gridfs


class Loader:

    @staticmethod
    def loader_with_mongodb(storage_config):
        """

        :param storage_config:
        :return:
        """
        connection = MongoClient(storage_config['host'], storage_config['port'])
        db = connection.loader_cache
        storage = MongoDBStorage(db=gridfs.GridFS(db), hash_lib=sha512())
        return LoaderWithCache(storage=storage)

    @staticmethod
    def loader():
        """

        :return lib.loader.Loader:
        """
        return LoaderWOCache()
