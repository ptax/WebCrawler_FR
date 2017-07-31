from lib.factory.Loader import Loader as Loader
from lib.config.Yaml import Yaml as Config


config = Config('./config/config.yml')
loader = Loader.loader_with_mongodb(config.get('mongodb'))

url = 'https://fr.wikipedia.org/wiki/Paris'
headers = {'User-Agent': 'Mozilla/5.0'}

content = loader.load(url, headers=headers)

content_from_storage = loader.from_cache(url, headers=headers)

if len(content) == len(content_from_storage):
    print('.', end='')
else:
    print('E', end='')

loader._storage.remove(url, headers=headers)