
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')


DictTypeObject = {  1:"establishment",
                    2:"point_of_interest",
                    3:"park",
                    4:"lodging",
                    5:"campground",
                    6:"amusement_park",
                    7:"food",
                    8:"restaurant",
                    9:"rv_park",
                    10:"zoo",
                    11:"health",
                    12:"store",
                    13:"real_estate_agency",
                    14:"travel_agency",
                    15:"bar",
                    16:"museum",
                    17:"pharmacy",
                    18:"parking",
                    19:"school",
                    20:"spa",
                    21:"local_government_office",
                    22:"hospital",
                    23:"transit_station",
                    24:"car_repair",
                    25:"doctor",
                    26:"general_contractor",
                    27:"natural_feature",
                    28:"bus_station",
                    29:"cafe",
                    30:"gym",
                    31:"car_dealer",
                    32:"stadium",
                    33:"place_of_worship",
                    34:"bakery",
                    35:"veterinary_care",
                    36:"finance",
                    37:"grocery_or_supermarket",
                    38:"shopping_mall",
                    39:"aquarium",
                    40:"library",
                    41:"florist",
                    42:"pet_store",
                    43:"beauty_salon",
                    44:"gas_station",
                    45:"city_hall",
                    46:"dentist",
                    47:"insurance_agency",
                    48:"bank",
                    49:"home_goods_store",
                    50:"light_rail_station",
                    51:"train_station",
                    52:"movie_theater",
                    53:"furniture_store",
                    54:"cemetery",
                    55:"night_club",
                    56:"lawyer",
                    57:"car_rental",
                    58:"meal_takeaway",
                    59:"laundry",
                    60:"premise",
                    61:"bowling_alley",
                    62:"atm",
                    63:"art_gallery",
                    64:"political",
                    65:"electronics_store",
                    66:"storage",
                    67:"hair_care",
                    68:"book_store",
                    69:"liquor_store",
                    70:"accounting",
                    71:"clothing_store",
                    72:"shoe_store",
                    73:"university",
                    74:"moving_company",
                    75:"casino"}

DictTypeRang = {  11:"natural_feature",
                  12:"rv_park",
                    13:"general_contractor",
                    14:"local_government_office",
                    15:"museum",
                    16:"place_of_worship",
                    17:"premise",
                    18:"campground",
                    19:"camping",
                    20:"zoo",
                    21:"amusement_park",
                    22:"park",
                    23:"lodging",
                    24:"travel_agency",
                    25:"transit_station",
                    26:"food",
                    27:"health",
                    28:"hospital",
                    29:"pharmacy",
                    30:"real_estate_agency",
                    31:"shopping_mall",
                    32:"store",
                  33:"point_of_interest,establishment"}


def GenDictPlace(Filename):
    DictMyPlace = {}
    for i in Filename.readlines():
        MyPlace = i.split('\t')
        PlaceID = MyPlace[13].strip()
        GoogleId = MyPlace[38].strip()

        DictMyPlace[GoogleId] = {'WebSite':MyPlace[0],
                                    'Rating':MyPlace[1],
                                    'UtcOffset':MyPlace[2],
                                    'Name':MyPlace[3],
                                    'Reference':MyPlace[4],
                                    'Photos':MyPlace[5],
                                    'GeometryLocationCordinates_1':MyPlace[6],
                                    'GeometryLocationCordinates_2':MyPlace[7],
                                    'GeometryLocationCordinates_3':MyPlace[8],
                                    'GeometryLocationCordinates_4':MyPlace[9],
                                    'GeometryLocationCordinates_5':MyPlace[10],
                                    'GeometryLocationCordinates_6':MyPlace[11],
                                    'AdrAddress':MyPlace[12],
                                    'PlaceID':PlaceID,
                                    'PhoneNumber':MyPlace[14],
                                    'Vicinity':MyPlace[15],
                                    'Reviews':MyPlace[16],
                                    'Url':MyPlace[17],
                                    'Score':MyPlace[18],
                                    'AddressComponentsLongName':MyPlace[19],
                                    'AddressComponentsTypes':MyPlace[20],
                                    'AddressComponentsShortName':MyPlace[21],
                                    'AddressComponentsLongName_1':MyPlace[22],
                                    'AddressComponentsTypes_1':MyPlace[23],
                                    'AddressComponentsShortName_1':MyPlace[24],
                                    'AddressComponentsLongName_2':MyPlace[25],
                                    'AddressComponentsTypes_2':MyPlace[26],
                                    'AddressComponentsShortName_2':MyPlace[27],
                                    'AddressComponentsLongName_3':MyPlace[28],
                                    'AddressComponentsTypes_3':MyPlace[29],
                                    'AddressComponentsShortName_3':MyPlace[30],
                                    'AddressComponentsLongName_4':MyPlace[31],
                                    'AddressComponentsTypes_4':MyPlace[32],
                                    'AddressComponentsShortName_4':MyPlace[33],
                                    'AddressComponentsLongName_5':MyPlace[34],
                                    'AddressComponentsTypes_5':MyPlace[35],
                                    'AddressComponentsShortName_5':MyPlace[36],
                                    'FormattedAddress':MyPlace[37],
                                    'GoogleId':GoogleId,
                                    'Types':MyPlace[39],
                                    'Icon':MyPlace[40],
                                    'CoordinatesRadios':MyPlace[41],
                                    'ColResult': MyPlace[42],
                                    'RankType':'None'
                                    }
    return DictMyPlace





#OpenMyPlase = open(r'Parck_2_Descr.txt')
OpenMyPlase = open(r'Parck_2_Descr.txt')

DictMyPlace = GenDictPlace(OpenMyPlase)
SortDict = {}



print 'File Dict  + \t' + str(len(DictMyPlace))
for TypeRange in DictTypeRang.items():
    RangNum = TypeRange[0]
    TypeRange = TypeRange[1].strip()
    for key in DictMyPlace.keys():
        key = key
        WordkDict = DictMyPlace.get(key)
        #print  WordkDict['Types']
        Types = WordkDict['Types']
        if TypeRange in Types:
            Data = {'RankType':TypeRange}
            WordkDict.update(Data)
            NewKey = str(RangNum).strip() + '_' + TypeRange.strip() + '_' + str(key).strip()
            SortDict[NewKey] = WordkDict
            del DictMyPlace[key]


'''
for i in DictMyPlace.keys():
    TypeRange = 'point_of_interest,establishment'
    WordkDict = DictMyPlace.get(key)
    Types = str(WordkDict['Types'].strip()).split(',')
    ListNewType = []
    for type in Types:
        if 'point_of_interest' in type:
            ListNewType.append(True)
        elif 'establishment' in type:
            ListNewType.append(True)
        if len(ListNewType) == 2:
            Data = {'RankType':TypeRange}
            WordkDict.update(Data)
            NewKey = str(33).strip() + '_' + TypeRange.strip() + '_' + str(key).strip()
            SortDict[NewKey] = WordkDict

            del DictMyPlace[key]
'''

print len(DictMyPlace)
for key in DictMyPlace.keys():
    TypeRange = 'NoneType'
    WordkDict = DictMyPlace.get(key)
    Data = {'RankType':TypeRange}
    WordkDict.update(Data)
    NewKey = str(34).strip() + '_' + TypeRange.strip() + '_' + str(key).strip()
    SortDict[NewKey] = WordkDict
    del DictMyPlace[key]







print 'Start Start Dict Finock + \t' + str(len(DictMyPlace))

print 'New Dict + \t' + str(len(SortDict))







for i in sorted(SortDict.items(), key=lambda item: item[0][:2]):
    i = i[1]
    WebSite = i['WebSite'].strip()
    Rating = i['Rating'].strip()
    UtcOffset = i['UtcOffset'].strip()
    Name = i['Name'].strip()
    Reference = i['Reference'].strip()
    Photos = i['Photos'].strip()
    GeometryLocationCordinates_1 = i['GeometryLocationCordinates_1'].strip()
    GeometryLocationCordinates_2 = i['GeometryLocationCordinates_2'].strip()
    GeometryLocationCordinates_3 = i['GeometryLocationCordinates_3'].strip()
    GeometryLocationCordinates_4 = i['GeometryLocationCordinates_4'].strip()
    GeometryLocationCordinates_5 = i['GeometryLocationCordinates_5'].strip()
    GeometryLocationCordinates_6 = i['GeometryLocationCordinates_6'].strip()
    AdrAddress = i['AdrAddress'].strip()
    PlaceID = i['PlaceID'].strip()
    PhoneNumber = i['PhoneNumber'].strip()
    Vicinity = i['Vicinity'].strip()
    Reviews = i['Reviews'].strip()
    Url = i['Url'].strip()
    Score = i['Score'].strip()
    AddressComponentsLongName = i['AddressComponentsLongName'].strip()
    AddressComponentsTypes = i['AddressComponentsTypes'].strip()
    AddressComponentsShortName = i['AddressComponentsShortName'].strip()
    AddressComponentsLongName_1 = i['AddressComponentsLongName_1'].strip()
    AddressComponentsTypes_1 = i['AddressComponentsTypes_1'].strip()
    AddressComponentsShortName_1 = i['AddressComponentsShortName_1'].strip()
    AddressComponentsLongName_2 = i['AddressComponentsLongName_2'].strip()
    AddressComponentsTypes_2 = i['AddressComponentsTypes_2'].strip()
    AddressComponentsShortName_2 = i['AddressComponentsShortName_2'].strip()
    AddressComponentsLongName_3 = i['AddressComponentsLongName_3'].strip()
    AddressComponentsTypes_3 = i['AddressComponentsTypes_3'].strip()
    AddressComponentsShortName_3 = i['AddressComponentsShortName_3'].strip()
    AddressComponentsLongName_4 = i['AddressComponentsLongName_4'].strip()
    AddressComponentsTypes_4 = i['AddressComponentsTypes_4'].strip()
    AddressComponentsShortName_4 = i['AddressComponentsShortName_4'].strip()
    AddressComponentsLongName_5 = i['AddressComponentsLongName_5'].strip()
    AddressComponentsTypes_5 = i['AddressComponentsTypes_5'].strip()
    AddressComponentsShortName_5 = i['AddressComponentsShortName_5'].strip()
    FormattedAddress = i['FormattedAddress'].strip()
    GoogleId = i['GoogleId'].strip()
    Type = i['Types'].strip()
    Icon = i['Icon'].strip()
    Coordinates = i['CoordinatesRadios'].strip()
    ColResult = i['ColResult'].strip()
    RankType  = i['RankType'].strip()
    Header = 'WebSite	Rating	UtcOffset	Name	Reference	Photos	GeometryLocationCordinates_1	GeometryLocationCordinates_2	GeometryLocationCordinates_3	GeometryLocationCordinates_4	GeometryLocationCordinates_5	GeometryLocationCordinates_6	AdrAddress	PlaceID	PhoneNumber	Vicinity	Reviews	Url	Score	AddressComponentsLongName	AddressComponentsTypes	AddressComponentsShortName	AddressComponentsLongName_1	AddressComponentsTypes_1	AddressComponentsShortName_1	AddressComponentsLongName_2	AddressComponentsTypes_2	AddressComponentsShortName_2	AddressComponentsLongName_3	AddressComponentsTypes_3	AddressComponentsShortName_3	AddressComponentsLongName_4	AddressComponentsTypes_4	AddressComponentsShortName_4	AddressComponentsLongName_5	AddressComponentsTypes_5	AddressComponentsShortName_5	FormattedAddress	GoogleId	Type	Icon CoordinatesRadios ColResult RankType'
    data = '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}\t{8}\t{9}\t{10}\t{11}\t{12}\t{13}\t{14}\t{15}\t{16}\t{17}\t{18}\t{19}\t{20}\t{21}\t{22}\t{23}\t{24}\t{25}\t{26}\t{27}\t{28}\t{29}\t{30}\t{31}\t{32}\t{33}\t{34}\t{35}\t{36}\t{37}\t{38}\t{39}\t{40}\t{41}\t{42}\t{43}'.format(WebSite,Rating,UtcOffset,Name,Reference,Photos,GeometryLocationCordinates_1,GeometryLocationCordinates_2,GeometryLocationCordinates_3,GeometryLocationCordinates_4,GeometryLocationCordinates_5,GeometryLocationCordinates_6,AdrAddress,PlaceID,PhoneNumber,Vicinity,Reviews,Url,Score,AddressComponentsLongName,AddressComponentsTypes,AddressComponentsShortName,AddressComponentsLongName_1,AddressComponentsTypes_1,AddressComponentsShortName_1,AddressComponentsLongName_2,AddressComponentsTypes_2,AddressComponentsShortName_2,AddressComponentsLongName_3,AddressComponentsTypes_3,AddressComponentsShortName_3,AddressComponentsLongName_4,AddressComponentsTypes_4,AddressComponentsShortName_4,AddressComponentsLongName_5,AddressComponentsTypes_5,AddressComponentsShortName_5,FormattedAddress,GoogleId,Type,Icon,Coordinates,ColResult,RankType)
    #print data
    text_file = open("base/Parck_7_Sorted.txt", "a")
    text_file.write(data +'\n')
text_file.close()









'''

DictPlace = {}
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
'''''