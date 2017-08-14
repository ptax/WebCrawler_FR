from lib.loader.HttpRequestWithCache import HttpRequestWithCache as HttpRequestWithCache
from lib.loader.HttpRequest import HttpRequest as HttpRequestWOCache
from lib.loader.storage.HttpRequest import HttpRequest as HttpRequestStorage
from lib.loader.storage.ComplexData import ComplexData as ComplexData
from lib.hashlib.sha512 import sha512
from lib.loader.GMaps import GMaps as LoaderGMapsWOCache
from lib.loader.GMapsWithCache import LoaderGMapsWithCache as LoaderGMapsWithCache
import googlemaps

from pymongo import MongoClient
import gridfs


class Loader:

    @staticmethod
    def loader():
        return HttpRequestWOCache()

    @staticmethod
    def loader_with_mongodb(storage_config):
        connection = MongoClient(storage_config['host'], storage_config['port'])
        db = connection.loader_cache
        storage = HttpRequestStorage(db=gridfs.GridFS(db), hash_lib=sha512())
        return HttpRequestWithCache(storage=storage)

    @staticmethod
    def loader_gmaps(gmaps_config):
        return LoaderGMapsWOCache(googlemaps=googlemaps.Client(key=gmaps_config['geocoding']))

    @staticmethod
    def loader_gmaps_with_cache(gmaps_config, storage_config):
        connection = MongoClient(storage_config['host'], storage_config['port'])
        db = connection.loader_gmaps_cache
        storage = ComplexData(db=gridfs.GridFS(db), hash_lib=sha512())
        return LoaderGMapsWithCache(googlemaps=googlemaps.Client(key=gmaps_config['geocoding']), storage=storage)
