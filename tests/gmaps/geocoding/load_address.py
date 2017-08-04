from lib.factory.Loader import Loader as Factory
from lib.config.Yaml import Yaml as Config
import json


config = Config('./config/config.yml')

loader = Factory.loader_gmaps(config.get('googlemaps'))

address = 'France, Paris'

address_content = loader.by_address(address=address)

print('.' if len(address_content) else 'E', end='')

fh = open('tmp/gmaps_address.json', 'w+')
fh.write(json.dumps(address_content))
fh.close()