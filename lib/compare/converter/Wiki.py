import lib.compare.converter.Converter as Converter

class Wiki(Converter):

    def __init__(self, obj):
        super(Wiki, self).__init__(obj)
        self._admin_levels = {
            self.obj.ADMIN_LEVEL_1:1,
            self.obj.ADMIN_LEVEL_2:2,
            self.obj.ADMIN_LEVEL_3:3,
            self.obj.ADMIN_LEVEL_4:4,
            self.obj.ADMIN_LEVEL_5:5,
            self.obj.ADMIN_LEVEL_6:6
        }

    def by_name(self):
        dic = {origin: self.obj.name}
        for key, value in self.obj.i18n.items():
            dic[key] = value.name
        return dic

    def by_distance(self):
        return {lat: self.obj.center.latitude, lng: self.obj.center.longitude}

    def _admin_value(self, value):
        dic = {origin: value.name}
        for key, val in value.i18n.items():
            dic[key] = val.name
        return dic

    def _admin_index(self, value):
        return self._admin_levels[value.type]

    def by_admin_hierarchy(self):
        admins = []
        for key, value in self.obj.admin_hierarchy:
            admins[self._admin_index(value)] = self._admin_value(value)

        return admins



    def by_polygon(self):
        return self.by_distance()