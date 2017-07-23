import lib.factory.Loader as Loader

loader = Loader.loader()

url = 'https://fr.wikipedia.org/wiki/Paris'
headers = {'User-Agent': 'Mozilla/5.0'}

content = loader.load(url, headers=headers)
