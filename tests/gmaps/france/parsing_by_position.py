from lib.factory.Loader import Loader as LoaderFactory
from lib.parser.map.google.GMapFactory import GMapFactory as MapFactory
from lib.config.Yaml import Yaml as Config


config = Config('../../../config/config.yml')

loader = LoaderFactory.loader_gmaps_with_cache(config.get('googlemaps'), config.get('mongodb'))

address = 'France, Paris'

position_content = loader.by_position(lat=48.83333, lng=2.33333)

print('.' if len(position_content) else 'E', end='')

objects = MapFactory.france(position_content)

print('.' if len(objects) else 'E', end='')
