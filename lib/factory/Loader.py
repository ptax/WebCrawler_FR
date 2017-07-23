import urllib2
import lib.loader.LoaderWithCache as LoaderWithCache
import lib.loader.Loader as LoaderWOCache
import lib.loader.storage.MongoDB as MongoDBStorage

from pymongo import MongoClient


class Loader:

    @staticmethod
    def loader_with_mongodb(storage_config):
        """

        :param storage_config:
        :return:
        """
        connection = MongoClient(storage_config['host'], storage_config['port'])
        db = connection.loader_cache
        storage = MongoDBStorage(db=db, hash_lib=hashlib)
        return LoaderWithCache(loader_lib=urllib2, storage=storage)

    @staticmethod
    def loader():
        """

        :return lib.loader.Loader:
        """
        return LoaderWOCache(loader_lib=urllib2)
