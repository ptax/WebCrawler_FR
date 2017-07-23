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
        pass

    def get_longitude(self):
        pass

    def get_altitude(self):
        pass

    def get_population(self):
        pass

    def get_density(self):
        pass

    def get_area(self):
        pass

    def get_postal_codes(self):
        pass

    def get_lang_links(self):
        pass

    def is_location_page(self):
        pass

    def is_many_answers(self):
        pass

    def get_answers_links(self):
        pass

    def _is_range(self, content):
        return re.match(r"\d+-\d+") is not None

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