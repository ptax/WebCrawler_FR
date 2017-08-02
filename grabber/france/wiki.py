import pandas as pd
from time import time
import sys
from lib.factory.Loader import Loader
from lib.parser.wiki.France import France as WikiFr
from lib.config.Yaml import Yaml as Config
from lib.factory.Storage import Storage as DocFactory
from lib.logger.File import File as FileLog
from argparse import ArgumentParser


config = Config('./config/config.yml')

arg_parser = ArgumentParser(description='Download data from wiki by link or search request')
arg_parser.add_argument('-f', help='turn on the force mode')
arg_parser.add_argument('-s', help='source with insee list')
arg_parser.add_argument('-r', help='custom request for search text in wiki')
arg_parser.add_argument('-l', help='custom link to page with result(s)')
opts = arg_parser.parse_args()

insee_index = 0
name_index = 1
population_index = 2
force_update = opts.f
headers = {'User-Agent': 'Mozilla/5.0'}
loader = Loader.loader_with_mongodb(config.get('mongodb'))
document_factory = DocFactory(config.get('mongodb'))
log = FileLog('./log/wiki_france_{time}.log'.format(time=time()))
log.add('Start', log.INFO)
log.add('Params: [{0}]'.format(repr(opts).encode('utf-8')), log.INFO)

url_format = "https://fr.wikipedia.org/w/index.php?search={0}&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"
message_format = 'Parsing request:[{0}]'

use_insee_list = opts.s
file_name_insee_list = opts.s if use_insee_list else './WorkBaseFile/BaseCommuneInInseeFR'

use_request = opts.r
custom_request = opts.r if use_request else ''

use_link = opts.l
custom_link = opts.l if use_link else ''


def update_meta(url, request, document):
    actual_doc = document.get_document()
    actual_doc.update(url=url)
    added_requests = actual_doc.get('requests', []) + [request]
    actual_doc.update(requests=list(set(added_requests)))
    document.update(actual_doc)


def parsing(request_url, factory, force=False, headers=None):
    content, code = loader.load(request_url, headers=headers)
    parser = WikiFr(content)

    if parser.is_many_answers():
        urls = parser.get_answers_links()
        for url in urls:
            doc = factory.wiki(url)
            if doc.is_new() or force:
                page, code = loader.load(url, headers=headers)
                page_parser = WikiFr(page)
                if page_parser.is_location_page():
                    doc.update(page_parser.as_dictionary())
            update_meta(url=url, request=request_url, document=doc)
    elif parser.is_location_page():
        doc = factory.wiki(request_url)
        if doc.is_new() or force:
            doc.update(parser.as_dictionary())
        update_meta(url=request_url, request=request_url, document=doc)

try:
    if use_insee_list:
        df = pd.read_csv(file_name_insee_list, delimiter="\t")
        for index, row in df.iterrows():
            try:
                insee = row[insee_index]
                name = row[name_index]
                population = row[population_index].replace(' ', '')
                request = 'insee+' + str(insee)
                log.add(message_format.format(request), log.INFO)
                url = url_format.format(request)
                parsing(request_url=url, factory=document_factory, force=force_update, headers=headers)
            except:
                log.add('Have error with insee [{insee}]'.format(insee=insee), FileLog.WARNING)

    elif use_request:
        url = url_format.format(custom_request)
        log.add(message_format.format(custom_request), log.INFO)
        parsing(request_url=url, factory=document_factory, force=force_update, headers=headers)

    elif use_link:
        log.add(message_format.format(custom_link), log.INFO)
        parsing(request_url=custom_link, factory=document_factory, force=force_update, headers=headers)

    else:
        log.add('Wrong command', log.ERROR)
        print('use parameters like -s csv file or -r query string or -l link to wiki page')
except:
    message = str(sys.exc_info())
    log.add('Unexpected error: [{0}]'.format(message), log.ERROR)
    raise

log.add('Finish', log.INFO)