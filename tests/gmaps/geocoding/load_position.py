from lib.factory.Loader import Loader as Factory
from lib.config.Yaml import Yaml as Config


config = Config('./config/config.yml')

loader = Factory.loader_gmaps(config.get('googlemaps'))

lat, lng = 48.861077, 2.344552

position_content = loader.by_position(lat=lat, lng=lng)
print(position_content)