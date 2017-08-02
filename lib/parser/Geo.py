import re
from geopy.distance import vincenty

class Geo:

    WITHOUT_ZERO = r'^-?[\.,]\d+'
    LAT_REGEXP = r"([^\d\.,-]|-(?=-)|^)(?P<coordinate>-?(([0-8]?\d([\.,]\d+)?|90([\.,]0+)?)))([^\d,.°’\'\"]|(?<=(\d|[\.,\"\'])\d{2})\"?$|$)"
    LNG_REGEXP = r"([^\d\.,-]|-(?=-)|^)(?P<coordinate>-?(\d{1,2}([\.,]\d+)?|1([0-7]\d([\.,]\d+)?|80([\.,]0+)?)))([^\d,.°’\'\"]|(?<=(\d|[\.,\"\'])\d{2})\"?$|$)"

    def lat(self, text):
        return re.search(self.LAT_REGEXP, text, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)

    def lng(self, text):
        return re.search(self.LNG_REGEXP, text, re.MULTILINE | re.UNICODE | re.IGNORECASE | re.DOTALL)

    def to_dot(self, text):
        pass

    @staticmethod
    def distance(start_lat, start_lng, end_lat, end_lng):
        return vincenty((start_lat, start_lng), (end_lat, end_lng)).meters