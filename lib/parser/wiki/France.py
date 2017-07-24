import re
import parser.wiki.Wiki as Wiki

from bs4 import BeautifulSoup


class France(Wiki):

    HOST = 'https://fr.wikipedia.org'

    def __init__(self, content):
        super(France, self).__init__(content)
        self._main_block_soap = self.get_main_block()
        self._content_soap = BeautifulSoup(self.content)

    def as_dictionary(self):
        dic = {}

        dic.name = self.get_name()

        admin = self.get_admin_hierarchy()
        if admin:
            dic.admin_hierarchy = self.get_admin_hierarchy()

        dic.i18n = self.get_lang_links()

        capital = serf.get_capital()
        if capital:
            dic.capital = capital

        lat = self.get_latitude()
        lng = self.get_longitude()
        if lat and lng:
            dic.center = {
                'latitude': lat,
                'longitude': lng
            }

        altitude = self.get_altitude()
        if altitude:
            dic.altitude = altitude

        population = self.get_population()
        if population:
            dic.population = population

        density = self.get_density()
        if density:
            dic.density = density

        area = self.get_area()
        if area:
            dic.area = area

        postal_codes = self.get_postal_codes()
        if postal_codes:
            dic.postal_codes = postal_codes

        commune_codes = self.get_commune_codes()
        if commune_codes:
            dic.commune_codes = commune_codes

        return dic

    def get_main_block(self):
        return BeautifulSoup(self.content).find("table", { "class" : "infobox_v2" })

    def get_name(self):
        name_raw = elf._content_soap.find('#firstHeading')
        if not name_raw:
            name_raw = elf._content_soap.find('tr:nth-child(1) > td')

        return self.replace_html(name_raw) if name_raw else ''

    def get_admin_hierarchy(self):
        admin = []

        country = self._get_country()
        if country:
            admin.append(country)

        region = self._get_region()
        if region:
            admin.append(region)

        department = self._get_department()
        if department:
            admin.append(department)

        borough = self._get_borough()
        if borough:
            admin.append(borough)

        city = self._get_city()
        if city:
            admin.append(city)

        return admin

    def _get_value_with_link(self, column_name):
        match = re.search(
            r"<th[^>]*>.*?" + re.escape(column_name) + r".*?<[^>]*th>\s*<td[^>]*>.*?<a[^>]*href=\"(?P<url>/wiki/[^\"]*)\"[^>]*>(?P<name>[^<]*)</a>.*?<[^>]*td>",
            self.content,
            re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)

        return {"url": self.HOST + match.group('url'), "name": self.replace_html(match.group('name'))} if match else {}

    def _get_country(self):
        return self._get_value_with_link(u"Pays")

    def _get_region(self):
        return self._get_value_with_link(u"Région")

    def _get_department(self):
        return self._get_value_with_link(u"Département")

    def _get_borough(self):
        return self._get_value_with_link(u"Arrondissement")

    def _get_city(self):
        return self._get_value_with_link(u"Ville")

    def get_altitude(self):
        result = {}
        data = self._get_value(u'Altitude')

        min = self._get_min_altitude(data)
        if min is not None:
            result.min = min

        max = self._get_max_altitude(data)
        if max is not None:
            result.max = max

        return result


    def get_population(self):
        population = self._get_value(u"Population<br />\nmunicipale")
        first_numbers = self._first_numbers(population)

        return first_numbers if first_numbers else population

    def get_density(self):
        data = self._get_value(u"Densité")
        first_numbers = self._first_numbers(data)

        return first_numbers if first_numbers else data

    def get_area(self):
        data = self._get_value(u'Superficie')
        first_numbers = self._first_numbers(data)

        return first_numbers if first_numbers else data

    def get_capital(self):
        result = {}

        capital = self._get_value_with_link(u"Siège")
        if not result and capital:
            result = capital

        capital = self._get_value_with_link(u"Siège de la préfecture")
        if not result and capital:
            result = capital

        capital = self._get_value_with_link(u"Chef-lieu")
        if not result and capital:
            result = capital

        capital = self._get_value_with_link(u"Capitale")
        if capital:
            result = capital

        return result


    def _get_value(self, column_name):
        match = re.search(
            r"<th[^>]*>.*?" + re.escape(column_name) + r".*?<[^>]*th>\s*<td[^>]*>(?P<name>.*)<[^>]*td>",
            self.content,
            re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)

        return self.replace_html(match.group('name'))

    def get_postal_codes(self):
        data = self._get_value('Code postal')
        return self._parse_postal_codes(data) if data else ''

    def get_commune_codes(self):
        data = self._get_value('Code commune')
        return self._parse_commune_codes(data) if data else ''

    def is_location_page(self):
        match = re.search(r"href=[\"']/wiki/Mod%C3%A8le:Infobox_(?P<code>Pays|(R%C3%A9gion|D%C3%A9partement|Arrondissement|Canton|Intercommunalit%C3%A9|Commune)_de_France)[\"']",
                          self.content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        return bool(match.group('code'))

    def _parse_postal_codes(self, content):
        codes = []
        content = re.sup(ur"(?i)\s*à\s*", "-", content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        content = re.sup(r"(?i)\s*et(\s+de)?\s*", ",", content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)
        content = re.sup(r"\s+", "", content, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)

        for code_bloc in content.split(','):
            codes += self._parse_postal_code(code_bloc)

        return codes

    def _parse_commune_codes(self, content):
        return self._parse_postal_codes(content)

    def get_residents(self):
        result = self._get_value(u"Gentilé")
        return result if result else ''




