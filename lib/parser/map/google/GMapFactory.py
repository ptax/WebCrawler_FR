from lib.parser.map.google.France import France


class GMapFactory:

    @staticmethod
    def france(response):
        objects = []
        for point in response:
            objects.append(France(point))
        return objects