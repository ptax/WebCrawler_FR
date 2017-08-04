from lib.factory.Loader import Loader as LoaderFactory
from lib.parser.map.google.GMapFactory import GMapFactory as MapFactory
from lib.config.Yaml import Yaml as Config


config = Config('./config/config.yml')

loader = LoaderFactory.loader_gmaps_with_cache(config.get('googlemaps'), config.get('mongodb'))

address = 'France, Paris'

address_content = loader.by_address(address=address)

print('.' if len(address_content) else 'E', end='')

objects = MapFactory.france(address_content)

print('.' if len(objects) else 'E', end='')

paris = objects[0]

print(paris.as_dictionary())