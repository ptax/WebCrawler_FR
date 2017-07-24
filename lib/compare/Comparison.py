from geopy.distance import vincenty


class Comparison:

    @staticmethod
    def by_name(original, candidate):
        pass

    @staticmethod
    def by_distance(original, candidate):
        return vincenty((original.lat, original.lng), (candidate.lat, candidate.lng)).meters

    @staticmethod
    def by_admin_hierarchy(original, candidate):
        pass

    @staticmethod
    def by_polygon(polygon, candidate):
        pass