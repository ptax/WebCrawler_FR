from lib.factory.Loader import Loader as Factory
from lib.config.Yaml import Yaml as Config

config = Config('./config/config.yml')

loader = Factory.loader_gmaps_with_cache(config.get('googlemaps'), config.get('mongodb'))

address = 'France, Paris'

address_content = loader.by_address(address=address)

address_content_cached = loader.from_cache(loader.address_key(address))

print(address_content_cached)

print('.' if address_content == address_content_cached else 'E', end='')
