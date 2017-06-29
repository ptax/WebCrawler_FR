# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg')




def GetInRadiusPlace(Coordinates_1,Coordinates_2,Keyword):
        '''
            You write data in Coordinates Radious and Keyword
            You Get PlaceID in Radius 10 km dict in format GooleMapsApi
            Return Dict in table format
        '''
        DictPlaceId = {}
        Coordinates = Coordinates_1,Coordinates_2
        GetPlace = gmaps.places_radar(location=Coordinates, radius=10000, keyword=Keyword)
        Coordinates = str(Coordinates).replace("(",'').replace(")",'').replace(" ",'').replace("'",'')
        ColResult = len(GetPlace['results'])
        for placeDict in GetPlace['results']:
            place_id = str(placeDict['place_id']).strip()
            DictPlaceId[place_id] = {'Name':placeDict['reference'].strip(),
                                     'CoordinatesRadios':str(Coordinates),
                                     'Coordinates_1':int(placeDict['geometry']['location']['lat']),
                                     'Coordinates_2':int(placeDict['geometry']['location']['lng']),
                                     'ColResult':int(ColResult),
                                     'PlaceID':place_id
                                     }
        return DictPlaceId






print help(GetInRadiusPlace)

print GetInRadiusPlace(43.51668853502907,-1.38427734375,u'plage')


''''

listData = []
#ListMyKeyWords = [u'lac',u'loch',u'étang',u'rivière',u'fleuve',u'baie',u'golfe']
for file in open(r'Radius_10kmFR'):
    File = file.split(',')
    Coordinates_1 = File[0]
    Coordinates_2 = File[1]
    Coordinates = Coordinates_1,Coordinates_2
    test = gmaps.places_radar(location=Coordinates, radius=10000, keyword=u'plage')
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
        listData.append(Date)
        Mydata = '{0}\t{1}\t{2}\t{3}\t{4}'.format(len(test['results']),Coordinates,str(Coordinates_1),str(Coordinates_2),place_id)
        #print Mydata
        #text_file = open("PlaceID_golfe_2.txt", "a")
        #text_file.write(Mydata +'\n')
    #text_file.close()


DictPlaceRadar = {}
for data in listData:
    ColPlaceRadiuc = data[0]
    CoordinatesCetrRadios = data[1]
    CordinatPlace_1 = data[2]
    CordinatPlace_2 = data[3]
    PlaceId = data[4]
    DictPlaceRadar[PlaceId] = {'ColPlaceRadiuc':ColPlaceRadiuc,
                               'CoordinatesCetrRadios':CoordinatesCetrRadios,
                               'CordinatPlace_1':CordinatPlace_1,
                               'CordinatPlace_2':CordinatPlace_2,
                               'PlaceId':PlaceId
                               }
print len(listData)
print len(DictPlaceRadar)

for MYdata in DictPlaceRadar.values():
    MYdata =  str(MYdata['ColPlaceRadiuc']) + '\t' + str(MYdata['CoordinatesCetrRadios']) + '\t' + str(MYdata['CordinatPlace_1']) + '\t' + str(MYdata['CordinatPlace_2']) + '\t' + str(MYdata['PlaceId'])
    print MYdata
    text_file = open("PlaceID_Plage.txt", "a")
    text_file.write(MYdata +'\n')
text_file.close()
'''