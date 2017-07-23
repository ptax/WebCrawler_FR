import lib.factory.Loader as Loader
import lib.config.Yaml as Config

config = Config('./config/config.yml')
loader = Loader.loader_with_mongodb(config['mongodb'])

url = 'https://fr.wikipedia.org/wiki/Paris'
headers = {'User-Agent': 'Mozilla/5.0'}

content = loader.load(url, headers=headers)

content_from_storage = loader.from_cache(url, headers=headers)

if content == content_from_storage:
    print('.')
else:
    print('E')

loader._storage.remove(url, headers=headers)