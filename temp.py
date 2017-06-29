# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
'''
listData = open(r'Ozera/PlaceID_Lac_all.txt').read().split('\n')

print len(listData)


DictPlaceRadar = {}
for data in listData:
    try:
        data = data.split('\t')
        ColPlaceRadiuc = data[0].strip()
        CoordinatesCetrRadios = data[1].strip()
        CordinatPlace_1 = data[2].strip()
        CordinatPlace_2 = data[3].strip()
        PlaceId = data[4].strip()
        DictPlaceRadar[PlaceId] = {'ColPlaceRadiuc':ColPlaceRadiuc,
                                   'CoordinatesCetrRadios':CoordinatesCetrRadios,
                                   'CordinatPlace_1':CordinatPlace_1,
                                   'CordinatPlace_2':CordinatPlace_2,
                                   'PlaceId':PlaceId
                                   }
    except:
        pass
print len(listData)
print len(DictPlaceRadar)

for MYdata in DictPlaceRadar.values():
    MYdata =  str(MYdata['ColPlaceRadiuc']) + '\t' + str(MYdata['CoordinatesCetrRadios']) + '\t' + str(MYdata['CordinatPlace_1']) + '\t' + str(MYdata['CordinatPlace_2']) + '\t' + str(MYdata['PlaceId'])
    print MYdata
    text_file = open(r"Ozera\PlaceID_Lac_all.txt", "a")
    text_file.write(MYdata +'\n')
text_file.close()


print len(listData)
print len(DictPlaceRadar)
'''
import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg')



Coordinates_1 = '43.929549935614595'
Coordinates_2 = '6.328125'
Coordinates = Coordinates_1,Coordinates_2
test = gmaps.places_radar(location=Coordinates, radius=10000, keyword=u'lac')
Coordinates = str(Coordinates).replace("(",'').replace(")",'').replace(" ",'').replace("'",'')

for i in test['results']:
    Name  = i['reference']
    Coordinates_1 = i['geometry']['location']['lat']
    Coordinates_2 = i['geometry']['location']['lng']
    #Adress = i['formatted_address']
    #types = (',').join(i['types'])
    place_id = i['place_id']
    #Date = str(len(test['results'])) + '\t' + Coordinates + '\t' + str(Coordinates_1) + '\t'  + str(Coordinates_2) +  '\t' + place_id
    Date = len(test['results']),Coordinates,str(Coordinates_1),str(Coordinates_2),place_id
    Mydata = '{0}\t{1}\t{2}\t{3}\t{4}'.format(len(test['results']),Coordinates,str(Coordinates_1),str(Coordinates_2),place_id)
    print Mydata
