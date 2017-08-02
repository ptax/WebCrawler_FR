class GMaps:
    def __init__(self, googlemaps):
        self._googlemaps = googlemaps

    def by_address(self, address):
        return self._googlemaps.geocode(address)

    def by_position(self, lat, lng):
        return self._googlemaps.reverse_geocode((lat, lng))