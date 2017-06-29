
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import googlemaps
from datetime import datetime
gmaps = googlemaps.Client(key='AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg')

'''
# Geocoding an address
geocode_result = gmaps.geocode('1600 Amphitheatre Parkway, Mountain View, CA')



# Look up an address with reverse geocoding
reverse_geocode_result = gmaps.reverse_geocode((40.714224, -73.961452))


# Request directions via public transit
now = datetime.now()
directions_result = gmaps.directions("Sydney Town Hall",
                                     "Parramatta, NSW",
                                     mode="transit",
                                     departure_time=now)

#test = gmaps.places(location='50.401699,30.252512',radius='50000',language='ru')
#test = test['results']

#test = gmaps.places(query="natural_feature",location='50.401699,30.252512',radius='50000',language='ru')

test = gmaps.places(query="natural_feature",location='50.7303727,1.5711146',radius=50000,language='fr')


for i in test['results']:
    Name  = i['name']
    Coordinates_1 = i['geometry']['location']['lat']
    Coordinates_2 = i['geometry']['location']['lng']
    Adress = i['formatted_address']
    types = (',').join(i['types'])
    place_id = i['place_id']
    Date = Name + '\t' + str(Coordinates_1) + '\t'  + str(Coordinates_2) + '\t' + str(Adress) + '\t' + types + '\t' + place_id
    #print Date

test = gmaps.places_nearby(location='50.7303727,1.5711146', radius=50000, type='point_of_interest', language='fr')
for i in test['results']:
    Name  = i['name']
    Coordinates_1 = i['geometry']['location']['lat']
    Coordinates_2 = i['geometry']['location']['lng']
    #Adress = i['formatted_address']
    types = (',').join(i['types'])
    place_id = i['place_id']
    Date = Name + '\t' + str(Coordinates_1) + '\t'  + str(Coordinates_2) + '\t' + types + '\t' + place_id
    #print Date

test = gmaps.places_radar(location='50.7303727,1.5711146', radius=50000, keyword='natural_feature')
for i in test['results']:
    Name  = i['reference']
    Coordinates_1 = i['geometry']['location']['lat']
    Coordinates_2 = i['geometry']['location']['lng']
    #Adress = i['formatted_address']
    #types = (',').join(i['types'])
    place_id = i['place_id']
    Date = Name + '\t' + str(Coordinates_1) + '\t'  + str(Coordinates_2) +  '\t' + place_id
    #print Date
'''

'''
for file in open(r'coordinat'):
    Cordinat = file.split('\t')
    Cordinat_1 = Cordinat[0].strip()
    Cordinat_2 = Cordinat[1].strip()

    GeocodeResult = gmaps.reverse_geocode((Cordinat_1,Cordinat_2),language='fr')

    Coordinates_1 = GeocodeResult[0]['geometry']['location']['lat']
    Coordinates_2 = GeocodeResult[0]['geometry']['location']['lng']

    Coordinates_3 = GeocodeResult[0]['geometry']['viewport']['northeast']['lat']

    Coordinates_4 = GeocodeResult[0]['geometry']['viewport']['northeast']['lng']
    Coordinates_5 = GeocodeResult[0]['geometry']['viewport']['southwest']['lat']
    Coordinates_6 = GeocodeResult[0]['geometry']['viewport']['southwest']['lng']
    LocationType = GeocodeResult[0]['geometry']['location_type']

    AddressComponentsLongName = GeocodeResult[0]['address_components'][0]['long_name']
    AddressComponentsTypes = ','.join(GeocodeResult[0]['address_components'][0]['types'])
    AddressComponentsShortName = GeocodeResult[0]['address_components'][0]['short_name']

    AddressComponentsLongName_1 = GeocodeResult[0]['address_components'][1]['long_name']
    AddressComponentsTypes_1 = ','.join(GeocodeResult[0]['address_components'][1]['types'])
    AddressComponentsShortName_1 = GeocodeResult[0]['address_components'][1]['short_name']

    AddressComponentsLongName_2 = GeocodeResult[0]['address_components'][2]['long_name']
    AddressComponentsTypes_2 = ','.join(GeocodeResult[0]['address_components'][2]['types'])
    AddressComponentsShortName_2 = GeocodeResult[0]['address_components'][2]['short_name']

    AddressComponentsLongName_3 = GeocodeResult[0]['address_components'][3]['long_name']
    AddressComponentsTypes_3 = ','.join(GeocodeResult[0]['address_components'][3]['types'])
    AddressComponentsShortName_3 = GeocodeResult[0]['address_components'][3]['short_name']

    AddressComponentsLongName_4 = GeocodeResult[0]['address_components'][4]['long_name']
    AddressComponentsTypes_4 = ','.join(GeocodeResult[0]['address_components'][4]['types'])
    AddressComponentsShortName_4 = GeocodeResult[0]['address_components'][4]['short_name']

    AddressComponentsLongName_5 = GeocodeResult[0]['address_components'][5]['long_name']
    AddressComponentsTypes_5 = ','.join(GeocodeResult[0]['address_components'][5]['types'])
    AddressComponentsShortName_5 = GeocodeResult[0]['address_components'][5]['short_name']

    try:
        AddressComponentsLongName_6 = GeocodeResult[0]['address_components'][6]['long_name']
    except:
        AddressComponentsLongName_6 = 'None'
    try:
        AddressComponentsTypes_6 = ','.join(GeocodeResult[0]['address_components'][6]['types'])
    except:
        AddressComponentsTypes_6  = 'None'
    try:
        AddressComponentsShortName_6 = GeocodeResult[0]['address_components'][6]['short_name']
    except:
        AddressComponentsShortName_6 = 'None'
    PlaceId = GeocodeResult[0]['place_id']
    FormattedAddress = GeocodeResult[0]['formatted_address']
    Types = ','.join(GeocodeResult[0]['types'])

    Headers = "Coordinates_1	Coordinates_2	Coordinates_3	Coordinates_4	Coordinates_5	Coordinates_6	LocationType	AddressComponentsLongName	AddressComponentsTypes	AddressComponentsShortName	AddressComponentsLongName_1	AddressComponentsTypes_1	AddressComponentsShortName_1	AddressComponentsTypes_2	AddressComponentsShortName_2	AddressComponentsLongName_3	AddressComponentsTypes_3	AddressComponentsShortName_3	AddressComponentsLongName_4	AddressComponentsTypes_4	AddressComponentsShortName_4	AddressComponentsLongName_5	AddressComponentsTypes_5	AddressComponentsShortName_5	AddressComponentsLongName_6	AddressComponentsTypes_6	AddressComponentsShortName_6	PlaceId	FormattedAddress	Types"
    data = '{0} \t  {1} \t {2}  \t  {3} \t {4} \t {5} \t {6} \t {7} \t {8} \t {9} \t {10} \t {11} \t {12} \t {13} \t {14} \t {15} \t {16} \t {17} \t {18} \t {19} \t {20} \t {21} \t {22} \t {23} \t {24} \t {25} \t {26} \t {27}'.format(Coordinates_1,Coordinates_2,Coordinates_3,Coordinates_4,Coordinates_5,Coordinates_6,LocationType,AddressComponentsLongName,AddressComponentsTypes,AddressComponentsShortName,AddressComponentsLongName_1,AddressComponentsTypes_1,AddressComponentsShortName_1,AddressComponentsTypes_2,AddressComponentsShortName_2,AddressComponentsLongName_3,AddressComponentsTypes_3,AddressComponentsShortName_3,AddressComponentsLongName_4,AddressComponentsTypes_4,AddressComponentsShortName_4,AddressComponentsLongName_5,AddressComponentsTypes_5,AddressComponentsShortName_5,AddressComponentsLongName_6,AddressComponentsTypes_6,AddressComponentsShortName_6,PlaceId,FormattedAddress,Types)
    print data
'''





'''
test = gmaps. places_autocomplete_query(input_text=u'Озера',location='50.401699,30.252512',radius='50000',language='ru')
for i in test:
    data = str(i['terms']) + '\t' + str(i['description']) + '\t'  + str(i['place_id'])  + '\t' + str(i['id'])  + '\t' + str(i['types'])
    #print  str(i['description']) + '\t' + str(i['types'])
    #print i['description'
'''
'''
for file in open(r'Lac_Name.txt'):
    file = file.split('	')
    ColResult = str(file[0])
    Coordinates = str(file[1])
    file = file[4].strip()

    PlaceIdInfo = gmaps.place(place_id=file, language='fr')
    PlaceIdInfo = PlaceIdInfo['result']
    try:
        WebSite = PlaceIdInfo['website']
    except:
        WebSite = 'None'
    try:
        Rating = PlaceIdInfo['rating']
    except:
        Rating = 'None'
    try:
        UtcOffset = PlaceIdInfo['utc_offset']
    except:
        UtcOffset = 'None'
    Name = PlaceIdInfo['name']

    Reference = PlaceIdInfo['reference']
    try:
        Photos = PlaceIdInfo['photos'][0]['photo_reference']
    except:
        Photos = 'None'
    GeometryLocationCordinates_1 = PlaceIdInfo['geometry']['location']['lat']
    GeometryLocationCordinates_2 = PlaceIdInfo['geometry']['location']['lng']
    GeometryLocationCordinates_3 = PlaceIdInfo['geometry']['viewport']['northeast']['lat']
    GeometryLocationCordinates_4 = PlaceIdInfo['geometry']['viewport']['northeast']['lng']
    GeometryLocationCordinates_5 = PlaceIdInfo['geometry']['viewport']['southwest']['lat']
    GeometryLocationCordinates_6 = PlaceIdInfo['geometry']['viewport']['southwest']['lng']
    AdrAddress = PlaceIdInfo['adr_address']
    PlaceID = PlaceIdInfo['place_id']
    try:
        PhoneNumber = PlaceIdInfo['international_phone_number']
    except:
        PhoneNumber = 'None'
    try:
        Vicinity = PlaceIdInfo['vicinity']
    except:
        Vicinity = 'None'
    try:
        Reviews = str(PlaceIdInfo['reviews'])
    except:
        Reviews = 'None'
    Url = PlaceIdInfo['url']
    Score = PlaceIdInfo['scope']
    AddressComponentsLongName = PlaceIdInfo['address_components'][0]['long_name']
    AddressComponentsTypes = ','.join(PlaceIdInfo['address_components'][0]['types'])
    AddressComponentsShortName = PlaceIdInfo['address_components'][0]['short_name']
    try:
        AddressComponentsLongName_1 = PlaceIdInfo['address_components'][1]['long_name']
    except:
        AddressComponentsLongName_1 = 'None'
    try:
        AddressComponentsTypes_1 = ','.join(PlaceIdInfo['address_components'][1]['types'])
    except:
        AddressComponentsTypes_1 = 'None'
    try:
        AddressComponentsShortName_1 = PlaceIdInfo['address_components'][1]['short_name']
    except:
        AddressComponentsShortName_1 = 'None'
    try:
        AddressComponentsLongName_2 = PlaceIdInfo['address_components'][2]['long_name']
    except:
        AddressComponentsLongName_2 = 'None'
    try:
        AddressComponentsTypes_2 = ','.join(PlaceIdInfo['address_components'][2]['types'])
    except:
        AddressComponentsTypes_2 = 'None'
    try:
        AddressComponentsShortName_2 = PlaceIdInfo['address_components'][2]['short_name']
    except:
        AddressComponentsShortName_2 = 'None'
    try:
        AddressComponentsLongName_3 = PlaceIdInfo['address_components'][3]['long_name']
    except:
        AddressComponentsLongName_3 = 'None'

    try:
        AddressComponentsTypes_3 = ','.join(PlaceIdInfo['address_components'][3]['types'])
    except:
        AddressComponentsTypes_3 = 'None'
    try:
        AddressComponentsShortName_3 = PlaceIdInfo['address_components'][3]['short_name']
    except:
        AddressComponentsShortName_3 = 'None'

    try:
        AddressComponentsLongName_4 = PlaceIdInfo['address_components'][4]['long_name']
    except:
        AddressComponentsLongName_4 = 'None'

    try:
        AddressComponentsTypes_4 = ','.join(PlaceIdInfo['address_components'][4]['types'])
    except:
        AddressComponentsTypes_4 = 'None'
    try:
        AddressComponentsShortName_4 = PlaceIdInfo['address_components'][4]['short_name']
    except:
        AddressComponentsShortName_4 = 'None'
    try:
        AddressComponentsLongName_5 = PlaceIdInfo['address_components'][5]['long_name']
    except:
        AddressComponentsLongName_5 = 'None'
    try:
        AddressComponentsTypes_5 = ','.join(PlaceIdInfo['address_components'][5]['types'])
    except:
        AddressComponentsTypes_5 = 'None'
    try:
        AddressComponentsShortName_5 = PlaceIdInfo['address_components'][5]['short_name']
    except:
        AddressComponentsShortName_5 = 'None'
    FormattedAddress = PlaceIdInfo['formatted_address']
    GoogleId = PlaceIdInfo['id']
    Type = ','.join(PlaceIdInfo['types'])
    Icon = PlaceIdInfo['icon']

    Header = 'WebSite	Rating	UtcOffset	Name	Reference	Photos	GeometryLocationCordinates_1	GeometryLocationCordinates_2	GeometryLocationCordinates_3	GeometryLocationCordinates_4	GeometryLocationCordinates_5	GeometryLocationCordinates_6	AdrAddress	PlaceID	PhoneNumber	Vicinity	Reviews	Url	Score	AddressComponentsLongName	AddressComponentsTypes	AddressComponentsShortName	AddressComponentsLongName_1	AddressComponentsTypes_1	AddressComponentsShortName_1	AddressComponentsLongName_2	AddressComponentsTypes_2	AddressComponentsShortName_2	AddressComponentsLongName_3	AddressComponentsTypes_3	AddressComponentsShortName_3	AddressComponentsLongName_4	AddressComponentsTypes_4	AddressComponentsShortName_4	AddressComponentsLongName_5	AddressComponentsTypes_5	AddressComponentsShortName_5	FormattedAddress	GoogleId	Type	Icon CoordinatesRadios ColResult'
    data = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}\t{30}\t{31}\t{32}\t{33}\t{34}\t{35}\t{36}\t{37}\t{38}\t{39}\t{40}\t{41}\t{42}'.format(WebSite,Rating,UtcOffset,Name,Reference,Photos,GeometryLocationCordinates_1,GeometryLocationCordinates_2,GeometryLocationCordinates_3,GeometryLocationCordinates_4,GeometryLocationCordinates_5,GeometryLocationCordinates_6,AdrAddress,PlaceID,PhoneNumber,Vicinity,Reviews,Url,Score,AddressComponentsLongName,AddressComponentsTypes,AddressComponentsShortName,AddressComponentsLongName_1,AddressComponentsTypes_1,AddressComponentsShortName_1,AddressComponentsLongName_2,AddressComponentsTypes_2,AddressComponentsShortName_2,AddressComponentsLongName_3,AddressComponentsTypes_3,AddressComponentsShortName_3,AddressComponentsLongName_4,AddressComponentsTypes_4,AddressComponentsShortName_4,AddressComponentsLongName_5,AddressComponentsTypes_5,AddressComponentsShortName_5,FormattedAddress,GoogleId,Type,Icon,Coordinates,ColResult)
    print data
    text_file = open("Lack_name_07_06_17.txt", "a")
    text_file.write(data +'\n')
text_file.close()
'''



'''

listData = []
ListMyKeyWords = [u'lac',u'loch',u'étang',u'rivière',u'fleuve',u'baie',u'golfe',u'Laquet',u'laquette']
for file in open(r'Radius_10kmFR'):
    File = file.split(',')
    Coordinates_1 = File[0]
    Coordinates_2 = File[1]
    Coordinates = Coordinates_1,Coordinates_2
    test = gmaps.places_radar(location=Coordinates, radius=10000, name=u'fleuve')
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
    PlaceId = data[4].strip()
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
    text_file = open("1_fleuve_Name.txt", "a")
    text_file.write(MYdata +'\n')
text_file.close()
'''

'''
test = gmaps.places(query="natural_feature",location='50.7303727,1.5711146',radius=50000,language='fr')


for i in test['results']:
    Name  = i['name']
    Coordinates_1 = i['geometry']['location']['lat']
    Coordinates_2 = i['geometry']['location']['lng']
    Adress = i['formatted_address']
    types = (',').join(i['types'])
    place_id = i['place_id']
    Date = Name + '\t' + str(Coordinates_1) + '\t'  + str(Coordinates_2) + '\t' + str(Adress) + '\t' + types + '\t' + place_id
    #print Date

'''
