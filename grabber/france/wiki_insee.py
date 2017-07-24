import pandas as pd
import lib.factory.Loader as Loader
import lib.parser.wiki.France as WikiFr
import lib.config.Yaml as Config


config = Config('./config/config.yml')

insee_index = 0
name_index = 1
population_index = 2
headers = {'User-Agent': 'Mozilla/5.0'}
loader = Loader.loader_with_mongodb(config['mongodb'])

url_format = "https://fr.wikipedia.org/w/index.php?search=%22Code+commune+{0}%22&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"

file_name_insee_list = './WorkBaseFile/BaseCommuneInInseeFR'

df = pd.read_csv(file_name_insee_list, delimiter="\t")

for index, row in df.iterrows():
    insee = row[insee_index]
    name = row[name_index]
    population = row[population_index].replace(' ', '')

    url = url_format.format('insee+' + insee)
    content = loader.load(url, headers=headers)
    parser = WikiFr(content)

    if parser.is_many_answers():
        urls = parser.get_answers_links()
        pages = []
        weight = []
        for url in urls:
            page = WikiFr(loader.load(url, headers=headers))
            pages.append(page)
            weight.append()
