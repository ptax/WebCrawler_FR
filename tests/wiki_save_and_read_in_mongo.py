from lib.factory.Storage import Storage as DocFactory
from lib.factory.Loader import Loader as LoaderFactory
from lib.config.Yaml import Yaml as Config
from lib.parser.wiki.France import France as WikiParser


config = Config('./config/config.yml')
document_factory = DocFactory(config.get('mongodb'))

url = 'https://fr.wikipedia.org/wiki/Paris'
headers = {'User-Agent': 'Mozilla/5.0'}

loader = LoaderFactory.loader_with_mongodb(config.get('mongodb'))

content, code = loader.load(url, headers=headers)

parser = WikiParser(content)

doc = document_factory.wiki(url)

print('.' if doc.is_new() else 'E', end='')

document = doc.get_document()

print('.' if 'code' in document else '', end='')

doc.update(parser.as_dictionary())

print(doc.get_document())


