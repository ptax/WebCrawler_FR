from lib.factory.Loader import Loader as Factory
from lib.config.Yaml import Yaml as Config
import json


config = Config('./config/config.yml')

loader = Factory.loader_gmaps(config.get('googlemaps'))

lat, lng = 48.861077, 2.344552

position_content = loader.by_position(lat=lat, lng=lng)


print('.' if len(position_content) else 'E', end='')

fh = open('tmp/gmaps_position.json', 'w+')
fh.write(json.dumps(position_content))
fh.close()