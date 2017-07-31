import pandas as pd
from time import time
import sys
from getopt import getopt
from lib.factory.Loader import Loader
from lib.parser.wiki.France import France as WikiFr
from lib.config.Yaml import Config
from lib.factory.Storage import Storage as DocFactory
from lib.logger.File import File as FileLog


config = Config('./config/config.yml')

opts = getopt(sys.argv[1:], 'fs:r:l:',)
insee_index = 0
name_index = 1
population_index = 2
force_update = '-f' in opts
headers = {'User-Agent': 'Mozilla/5.0'}
loader = Loader.loader_with_mongodb(config['mongodb'])
document_factory = DocFactory(config['mongodb'])
log = FileLog('./log/wiki_france_{time}.log'.format(time()))
log.add('Start')
log.add('Params: [{0}]'.format(repr(sys.argv[1:]).encode('utf-8')))

url_format = "https://fr.wikipedia.org/w/index.php?search={0}&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"

use_insee_list = '-s' in opts
file_name_insee_list = opts['-s'] if use_insee_list else './WorkBaseFile/BaseCommuneInInseeFR'

use_request = '-r' in opts
custom_request = opts['-r'] if use_request else ''

use_link = '-l' in opts
custom_link = opts['-l'] if use_link else ''


def parsing(url, factory, force=False, headers=None):
    content = loader.load(url, headers=headers)
    parser = WikiFr(content)

    if parser.is_many_answers():
        urls = parser.get_answers_links()
        for url in urls:
            doc = factory.wiki(url)
            if doc.is_new() or force:
                page = WikiFr(loader.load(url, headers=headers))
                doc.update(page.as_dictionary())
    else:
        doc = factory.wiki(url)
        if doc.is_new() or force:
            doc.update(parser.as_dictionary())


if use_insee_list:
    df = pd.read_csv(file_name_insee_list, delimiter="\t")
    for index, row in df.iterrows():
        try:
            insee = row[insee_index]
            name = row[name_index]
            population = row[population_index].replace(' ', '')

            url = url_format.format('insee+' + str(insee))
            parsing(url=url, factory=document_factory, force=force_update, headers=headers)
        except:
            log.add('Have error with insee [{insee}]'.format(insee=insee), FileLog.WARNING)

elif use_request:
    url = url_format.format(custom_request)
    parsing(url=url, factory=document_factory, force=force_update, headers=headers)

elif use_link:
    parsing(url=custom_link, factory=document_factory, force=force_update, headers=headers)

else:
    print('use parameters like -s csv file or -r query string or -l link to wiki page')

log.add('Finish')