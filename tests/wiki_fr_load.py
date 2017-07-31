from lib.factory.Loader import Loader as Factory


loader = Factory.loader()

url = 'https://fr.wikipedia.org/wiki/Paris'
headers = {'User-Agent': 'Mozilla/5.0'}

content, code = loader.load(url, headers=headers)

if code == 200 and len(content) > 0:
    print('.')
else:
    print('E')