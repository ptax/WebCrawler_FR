from lib.parser.map.google.GMap import GMap as GMap


class France(GMap):

    ADMIN_LEVEL_1 = 'country'
    ADMIN_LEVEL_2 = 'administrative_area_level_1'
    ADMIN_LEVEL_3 = 'administrative_area_level_2'
    ADMIN_LEVEL_4 = 'locality'
    ADMIN_LEVEL_5 = 'sublocality'
    ADMIN_LEVEL_6 = 'neighborhood'

    QUANTITY_OF_ADMIN_LEVELS = 6