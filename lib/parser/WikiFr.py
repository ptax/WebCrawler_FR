import lib.parser.Wiki
from bs4 import BeautifulSoup

class WikiFr(Wiki):

    def __init__(self, content):
        super(WikiFr, self).__init__(content)
        self._main_block_soap = self.get_main_block()

    def get_main_block(self):
        return BeautifulSoup(self.content).find("table", { "class" : "infobox_v2" })
