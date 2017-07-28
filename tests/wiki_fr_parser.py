from lib.factory.Loader import Loader as Factory
import sys
from lib.config.Yaml import Yaml as Config
from lib.parser.wiki.France import France as WikiParser


sys.path.insert(0, "/app")
config = Config('./config/config.yml')

loader = Factory.loader_with_mongodb(config.get('mongodb'))

url = 'https://fr.wikipedia.org/wiki/Paris'
headers = {'User-Agent': 'Mozilla/5.0'}

content, code = loader.load(url, headers=headers)

if code == 200 and len(content) > 0:
    print('.')
else:
    print('E')
    sys.exit()


parser = WikiParser(content)

print(parser.as_dictionary())