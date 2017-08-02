from lib.factory.Loader import Loader as Factory
from lib.config.Yaml import Yaml as Config


config = Config('./config/config.yml')

loader = Factory.loader_gmaps_with_cache(config.get('googlemaps'), config.get('mongodb'))

lat, lng = 48.861077, 2.344552

position_content = loader.by_position(lat=lat, lng=lng)

position_content_cached = loader.from_cache(loader.position_key(position))

print(position_content_cached)

print('.' if position_content == position_content_cached else 'E', end='')