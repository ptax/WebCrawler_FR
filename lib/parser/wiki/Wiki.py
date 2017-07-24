import re
import lib.parser.Parser as Parser


class Wiki(Parser):
    NAME = 'name'
    ADMIN_HIERARCHY = 'admin_hierarchy'
    LATITUDE = 'latitude'
    LONGITUDE = 'longitude'
    ALTITUDE = 'altitude'
    POPULATION = 'population'
    DENSITY = 'density'
    AREA = 'area'
    POSTAL_CODES = 'postal_codes'
    LANG_LINKS = 'lang_links'

    ADMIN_LEVEL_1 = ''
    ADMIN_LEVEL_2 = ''
    ADMIN_LEVEL_3 = ''
    ADMIN_LEVEL_4 = ''
    ADMIN_LEVEL_5 = ''
    ADMIN_LEVEL_6 = ''

    def __init__(self, content):
        super(Wiki, self).__init__(content=content)

    def get_main_block(self):
        pass

    def get_name(self):
        pass

    def get_admin_hierarchy(self):
        '''
        contain short name, long name, type and tree for hierarchy or sort bya index
        '''
        pass

    def get_latitude(self):
        result = None
        match = re.search(r"data-lat=\"(?P<lat>[\d\.]+)\"", self.content)
        if match.group('lat'):
            result = match.group('lat')
        return result

    def get_longitude(self):
        result = None
        match = re.search(r"data-lon=\"(?P<lon>[\d\.]+)\"", self.content)
        if match.group('lon'):
            result = match.group('lon')
        return result

    def get_altitude(self):
        pass

    def _get_min_altitude(self, content):
        result = None
        match = re.search(r"(?i)Min\.?\s*(?P<min>\d+)", content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        if match.group('min'):
            result = match.group('min')
        return result

    def _get_max_altitude(self, content):
        result = None
        match = re.search(r"(?i)Max\.?\s*(?P<max>\d+)", content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        if match.group('max'):
            result = match.group('max')
        return result

    def get_population(self):
        pass

    def get_density(self):
        pass

    def get_area(self):
        pass

    def get_postal_codes(self):
        pass

    def get_residents(self):
        pass

    def get_capital(self):
        pass

    def get_lang_links(self):
        result = {}
        match = re.search(ur"(?i)<li[^>]+class\s*=\s*[\"'][^\"']*interlanguage[^\"]*[\"'].*?href=[\"'](?P<url>.*?)[\"'][^>]*?title=[\"']\s*(?P<name>.*?)\s*—[^\"']*[\"'].*?lang=[\"'](?P<lang>\w+)[\"']",
                          self.content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        if match.group('url'):
            urls = match.group('url')
            langs = match.group('lang')
            names = match.group('name')
            for key, lang in langs:
                result[lang] = {'name': names[key], 'url':urls[key]}

        return result

    def is_location_page(self):
        pass

    def is_many_answers(self):
        match = re.search(r"(class=\"results-info\")", self.content)
        return bool(match.group(0))

    def get_answers_links(self):
        match = re.search(r"<div[^>]*?class=[\"']mw-search-result-heading[\"'][^>]*?>\s*<a href=[\"'](?P<url>/wiki/[^\"]+)[\"']", self.content)
        return [(self.HOST + x) for x in match.group('url')]

    def _is_range(self, content):
        return re.match(r"\d+-\d+", content) is not None

    def _range(self, content):
        codes = []
        match = re.search(r"(?P<start>\d+)-(?P<end>\d+)", content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        if match.group('start'):
            start = match.group('start')
            end = match.group('end')
            if start > end:
                start, end = end, start
            codes = renge(start, end + 1, 1)
        return codes

    def _parse_postal_code(self, codes):
        find_codes = []
        for code in codes:
            if self._is_range(code):
                find_codes += self._range(code)
            else:
                find_codes.append(code)
        return find_codes

    def _first_numbers(self, content):
        match = re.search(r"^(?P<number>([\d,\.]+))", content.replace(' ', ''))
        return match.group('number').strip(',.') if match.group('number') else 0