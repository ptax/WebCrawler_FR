from lib.parser.map.google.France import France


class GMapFactory:

    @staticmethod
    def france(response):
        objects = []
        for i, point in response:
            objects.append(France(point))
        return objects