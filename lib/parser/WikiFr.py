import lib.parser.Wiki
from bs4 import BeautifulSoup

class WikiFr(Wiki):

    def __init__(self, content):
        super(WikiFr, self).__init__(content)
        self._main_block_soap = self.get_main_block()
        self._content_soap = BeautifulSoup(self.content)

    def get_main_block(self):
        return BeautifulSoup(self.content).find("table", { "class" : "infobox_v2" })

    def get_name(self):
        name_raw = elf._content_soap.find('#firstHeading')
        if not name_raw:
            name_raw = elf._content_soap.find('tr:nth-child(1) > td')

        return self.replace_html(name_raw) if name_raw else ''

    def get_admin_hierarchy(self):
        '''
        contain short name, long name, type and tree for hierarchy or sort bya index
        '''
        pass

    def _get_admin_value(self, column_name):
        match = re.search(
            r"<th[^>]*>.*?" + re.escape(column_name) + r".*?<[^>]*th>\s*<td[^>]*>.*?<a[^>]*href=\"(?P<url>/wiki/[^\"]*)\"[^>]*>(?P<name>[^<]*)</a>.*?<[^>]*td>",
            self.content,
            re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)

        return {"url": match.group('url'), "name": self.replace_html(match.group('name'))} if match else {}

    def _get_country(self):
        return self._get_admin_value(u"Pays")

    def _get_region(self):
        return self._get_admin_value(u"Région")

    def _get_city(self):
        return self._get_admin_value(u"Ville")