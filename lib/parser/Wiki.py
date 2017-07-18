import lib.parser.Parser

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
        :return:
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

