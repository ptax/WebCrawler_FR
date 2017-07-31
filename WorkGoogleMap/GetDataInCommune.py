# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import Utils.SaveAndLoadDictFile
import random


def GetDataInAddress(LocationName, ApiKey):
    # url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + LocationName + "&sensor=false&language=fr&key=AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg"
    #url = "http://maps.googleapis.com/maps/api/geocode/json?address=" + LocationName + "&sensor=false&language=fr"
    url = "https://maps.googleapis.com/maps/api/geocode/json?address=" + LocationName + "&sensor=false&language=fr&key=" + str(
        ApiKey)

    url=urllib.unquote(url).decode('utf8')
    try:
        response = json.loads(urlopen(url).read())
        ResponseStatus = response["status"]
        if ResponseStatus == u"OK":
            listLang = []
            results = response.get("results")
            ResponseStatus = u"OK"
            return results[0],ResponseStatus
    except:
        response = 'None'
        ResponseStatus = "None"
        return response,ResponseStatus




def GetDataInCordinates(Cordinates_1,Cordinates_2):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + Cordinates_1 + "," + Cordinates_2 + "&sensor=false&language=fr&key=AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg"
    url=urllib.unquote(url).decode('utf8')
    try:
        response = json.loads(urlopen(url).read())
        ResponseStatus = response["status"]
        if ResponseStatus == u"OK":
            listLang = []
            results = response.get("results")
            ResponseStatus = u"OK"
            return results[0],ResponseStatus
    except:
        response = 'None'
        ResponseStatus = "None"
        return response,ResponseStatus



def DataStructure(GoogleResult):
    DictDataInGoogleResult = {}
    try:
        GoogleStatus = GoogleResult[1]
        GoogleResult = GoogleResult[0]
    except:
        pass
        GoogleStatus = 'None'
        GoogleResult = 'None'
    if GoogleStatus == u"OK":
        try:
            G_Coordinates_northeast_Lat_1 = GoogleResult['geometry']['bounds']['northeast']['lat']
        except:
            G_Coordinates_northeast_Lat_1 = "None"
        try:
            G_Coordinates_northeast_Lng_1 = GoogleResult['geometry']['bounds']['northeast']['lng']
        except:
            G_Coordinates_northeast_Lng_1 = 'None'
        try:
            G_Coordinates_southwest_Lat_2 = GoogleResult['geometry']['bounds']['southwest']['lat']
        except:
            G_Coordinates_southwest_Lat_2 = "None"
        try:
            G_Coordinates_southwest_Lng_2 = GoogleResult['geometry']['bounds']['southwest']['lng']
        except:
            G_Coordinates_southwest_Lng_2 = 'None'
        try:
            G_Coordinates_location_Lat_3 =  GoogleResult['geometry']['location']['lat']
        except:
            G_Coordinates_location_Lat_3 = "None"
        try:
            G_Coordinates_location_Lng_3 =  GoogleResult['geometry']['location']['lng']
        except:
            G_Coordinates_location_Lng_3 = 'None'



        try:
            G_AddressComponents_locality_LongName =  GoogleResult['address_components'][0]['long_name']
        except:
            G_AddressComponents_locality_LongName = "None"
        try:
            G_AddressComponents_locality_Types =  ','.join(GoogleResult['address_components'][0]['types'])
        except:
            G_AddressComponents_locality_Types = "None"
        try:
            G_AddressComponents_locality_ShortName = GoogleResult['address_components'][0]['short_name']
        except:
            G_AddressComponents_locality_ShortName = "None"
        try:
            G_AddressComponents_localityLevel_2_LongName = GoogleResult['address_components'][1]['long_name']
        except:
            G_AddressComponents_localityLevel_2_LongName = "None"
        try:
            G_AddressComponents_localityLevel_2_Types =  ','.join(GoogleResult['address_components'][1]['types'])
        except:
            G_AddressComponents_localityLevel_2_Types = 'None'
        try:
            G_AddressComponents_localityLevel_2_ShortName = GoogleResult['address_components'][1]['short_name']
        except:
            G_AddressComponents_localityLevel_2_ShortName = 'None'

        try:
            G_AddressComponents_localityLevel_1_LongName = GoogleResult['address_components'][2]['long_name']
        except:
            G_AddressComponents_localityLevel_1_LongName = "None"
        try:
            G_AddressComponents_localityLevel_1_Types =  ','.join(GoogleResult['address_components'][2]['types'])
        except:
            G_AddressComponents_localityLevel_1_Types = 'None'
        try:
            G_AddressComponents_localityLevel_1_ShortName = GoogleResult['address_components'][2]['short_name']
        except:
            G_AddressComponents_localityLevel_1_ShortName = "None"
        try:
            G_AddressComponents_localityCountry_LongName = GoogleResult['address_components'][3]['long_name']
        except:
            G_AddressComponents_localityCountry_LongName = 'None'
        try:
            G_AddressComponents_localityCountry_Types =  ','.join(GoogleResult['address_components'][3]['types'])
        except:
            G_AddressComponents_localityCountry_Types = 'None'
        try:
            G_AddressComponents_localityCountry_ShortName = GoogleResult['address_components'][3]['short_name']
        except:
            G_AddressComponents_localityCountry_ShortName = 'None'

        try:
            G_FormatAddress =GoogleResult['formatted_address']
        except:
            G_FormatAddress = "None"
        try:
            G_Types = ','.join(GoogleResult['types'])
        except:
            G_Types = "None"
        try:
            G_PlaceId = str(GoogleResult['place_id']).strip()
        except:
            G_PlaceId = "None"
        DictDataInGoogleResult ={
                                             'G_Coordinates_northeast_Lat_1':G_Coordinates_northeast_Lat_1,
                                             'G_Coordinates_northeast_Lng_1':G_Coordinates_northeast_Lng_1,
                                             'G_Coordinates_southwest_Lat_2':G_Coordinates_southwest_Lat_2,
                                             'G_Coordinates_southwest_Lng_2':G_Coordinates_southwest_Lng_2,
                                              'G_Coordinates_location_Lat_3':G_Coordinates_location_Lat_3,
                                              'G_Coordinates_location_Lng_3':G_Coordinates_location_Lng_3,
                                              'G_AddressComponents_locality_LongName':G_AddressComponents_locality_LongName,
                                              'G_AddressComponents_locality_Types':G_AddressComponents_locality_Types,
                                              'G_AddressComponents_locality_ShortName':G_AddressComponents_locality_ShortName,
                                              'G_AddressComponents_localityLevel_2_LongName':G_AddressComponents_localityLevel_2_LongName,
                                              'G_AddressComponents_localityLevel_2_Types':G_AddressComponents_localityLevel_2_Types,
                                              'G_AddressComponents_localityLevel_2_ShortName':G_AddressComponents_localityLevel_2_ShortName,
                                              'G_AddressComponents_localityLevel_1_LongName':G_AddressComponents_localityLevel_1_LongName,
                                              'G_AddressComponents_localityLevel_1_Types':G_AddressComponents_localityLevel_1_Types,
                                              'G_AddressComponents_localityLevel_1_ShortName':G_AddressComponents_localityLevel_1_ShortName,
                                             'G_AddressComponents_localityCountry_LongName':G_AddressComponents_localityCountry_LongName,
                                              'G_AddressComponents_localityCountry_Types':G_AddressComponents_localityCountry_Types,
                                             'G_AddressComponents_localityCountry_ShortName':G_AddressComponents_localityCountry_ShortName,
                                             'G_FormatAddress':G_FormatAddress,
                                             'G_Types':G_Types,
                                             'G_PlaceId':G_PlaceId

                                            }
    else:
        pass
    return DictDataInGoogleResult




def GetPlaceId(GoogleResult):
    DictDataInGoogleResult = {}
    try:
        GoogleStatus = GoogleResult[1]
        GoogleResult = GoogleResult[0]
    except:
        GoogleStatus = 'None'
        Google_Result = 'None'
    if GoogleStatus == u"OK":
        try:
            G_PlaceId = str(GoogleResult['place_id']).strip()
        except:
             G_PlaceId = "None"

        DictDataInGoogleResult ={'G_PlaceId':G_PlaceId}

    return DictDataInGoogleResult







def GetLangPlaceId(PlaceId,Lang):
    try:
        url = "https://maps.googleapis.com/maps/api/geocode/json?place_id=" + PlaceId + "&sensor=false&language="+ Lang+ "&key=AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg"
        url=urllib.unquote(url).decode('utf8')
        response = json.loads(urlopen(url).read())

        if response["status"] == u"OK":
            results = response.get("results")[0]
            print results
            KeyType = u'locality,political'
            types = ','.join(results['address_components'][0]['types'])
            if types in KeyType:
                LangName = results['address_components'][0]['long_name']
                return LangName
            else:
                LangName = 'None'
                return LangName
    except:
        LangName = 'None'
        return LangName





def GetResultInSendPlaceId(PlaceId):
    url = "https://maps.googleapis.com/maps/api/geocode/json?place_id=" + PlaceId + "&sensor=false&language="+ 'fr' + "&key=AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg"
    url=urllib.unquote(url).decode('utf8')
    response = json.loads(urlopen(url).read())
    if response["status"] == u"OK":
        url=urllib.unquote(url).decode('utf8')
        try:
            response = json.loads(urlopen(url).read())
            ResponseStatus = response["status"]
            if ResponseStatus == u"OK":
                listLang = []
                results = response.get("results")
                ResponseStatus = u"OK"
                return results[0],ResponseStatus
        except:
            response = 'None'
            ResponseStatus = "None"
            return response,ResponseStatus




def StructureLocalType(GoogleResult):
    DictMyData = {
                        u'G_Locality_long_name':'',
                        u'G_Locality_short_name':'',
                        u'G_Locality_types':'',
                        u'G_AdminLevel_1_long_name':'',
                        u'G_AdminLevel_1_short_name':'',
                        u'G_AdminLevel_1_types':'',
                        u'G_AdminLevel_2_long_name':'',
                        u'G_AdminLevel_2_short_name':'',
                        u'G_AdminLevel_2_types':'',
                        u'G_Country_long_name':'',
                        u'G_Country_short_name':'',
                        u'G_Country_types':'',
                        u'G_postal_code_long_name':'',
                        u'G_postal_code_short_name':'',
                        u'G_postal_code_types':''
                    }
    try:
        GoogleStatus = GoogleResult[1]
        GoogleResult = GoogleResult[0]
    except:
        pass
        GoogleStatus = 'None'
        GoogleResult = 'None'
    if GoogleStatus == u"OK":

        Adress =  GoogleResult['address_components']
        for Data in Adress:
            types = ','.join(Data['types'])

            if u'locality,political' in types:
                DataUpdate = {u'G_Locality_long_name':Data['long_name'],u'G_Locality_short_name':Data['short_name'],u'G_Locality_types':types}
                DictMyData.update(DataUpdate)
            elif u'administrative_area_level_1,political' in types:
                DataUpdate = {u'G_AdminLevel_1_long_name':Data['long_name'],u'G_AdminLevel_1_short_name':Data['short_name'],u'G_AdminLevel_1_types':types}
                DictMyData.update(DataUpdate)
            elif u'administrative_area_level_2,political' in types:
                DataUpdate = {u'G_AdminLevel_2_long_name':Data['long_name'],u'G_AdminLevel_2_short_name':Data['short_name'],u'G_AdminLevel_2_types':types}
                DictMyData.update(DataUpdate)
            elif u'country,political' in types:
                DataUpdate = {u'G_Country_long_name':Data['long_name'],u'G_Country_short_name':Data['short_name'],u'G_Country_types':types}
                DictMyData.update(DataUpdate)
            elif u'postal_code' in types:
                DataUpdate = {u'G_postal_code_long_name':Data['long_name'],u'G_postal_code_short_name':Data['short_name'],u'G_postal_code_types':types}
                DictMyData.update(DataUpdate)
    return DictMyData


def GetCoordinatesInGoogle(GoogleResult):

    DictDataInGoogleResult = {}
    try:
        GoogleStatus = GoogleResult[1]
        GoogleResult = GoogleResult[0]
    except:
        pass
        GoogleStatus = 'None'
        GoogleResult = 'None'
    if GoogleStatus == u"OK":
        try:
            G_Coordinates_northeast_Lat_1 = GoogleResult['geometry']['bounds']['northeast']['lat']
        except:
            G_Coordinates_northeast_Lat_1 = "None"
        try:
            G_Coordinates_northeast_Lng_1 = GoogleResult['geometry']['bounds']['northeast']['lng']
        except:
            G_Coordinates_northeast_Lng_1 = 'None'
        try:
            G_Coordinates_southwest_Lat_2 = GoogleResult['geometry']['bounds']['southwest']['lat']
        except:
            G_Coordinates_southwest_Lat_2 = "None"
        try:
            G_Coordinates_southwest_Lng_2 = GoogleResult['geometry']['bounds']['southwest']['lng']
        except:
            G_Coordinates_southwest_Lng_2 = 'None'
        try:
            G_Coordinates_location_Lat_3 =  GoogleResult['geometry']['location']['lat']
        except:
            G_Coordinates_location_Lat_3 = "None"
        try:
            G_Coordinates_location_Lng_3 =  GoogleResult['geometry']['location']['lng']
        except:
            G_Coordinates_location_Lng_3 = 'None'
        try:
            G_FormatAddress =GoogleResult['formatted_address']
        except:
            G_FormatAddress = "None"
        try:
            G_Types = ','.join(GoogleResult['types'])
        except:
            G_Types = "None"
        DictDataInGoogleResult ={
                                             'G_Coordinates_northeast_Lat_1':G_Coordinates_northeast_Lat_1,
                                             'G_Coordinates_northeast_Lng_1':G_Coordinates_northeast_Lng_1,
                                             'G_Coordinates_southwest_Lat_2':G_Coordinates_southwest_Lat_2,
                                             'G_Coordinates_southwest_Lng_2':G_Coordinates_southwest_Lng_2,
                                              'G_Coordinates_location_Lat_3':G_Coordinates_location_Lat_3,
                                             'G_Coordinates_location_Lng_3':G_Coordinates_location_Lng_3,
                                             'G_FormatAddress':G_FormatAddress,
                                             'G_Types':G_Types,
                                            }
    return DictDataInGoogleResult

def SplitGetDataInPlaceId(GoogleResult):
    GetAdressDict = GetCoordinatesInGoogle(GoogleResult)
    GetCoordimatDict = GetCoordinatesInGoogle(GoogleResult)
    Mydict = GetAdressDict.copy()

    Mydict.update(GetCoordimatDict)
    return Mydict


def stucture_postcode_localities(GoogleResult):
    try:
        GoogleStatus = GoogleResult[1]
        GoogleResult = GoogleResult[0]
    except:
        GoogleStatus = 'None'
        GoogleResult = 'None'
        pass
    if GoogleStatus == u"OK":
        try:
            postcode_localities = GoogleResult['postcode_localities']
        except:
            postcode_localities = ['None']
    else:
        postcode_localities = ['None']
    return postcode_localities



if __name__ == '__main__':
    CodeInsee = '62217'
    LocationName = '18300,France'

    ApikeyList = ['AIzaSyBZVOSPh0Z4mv9jljJWzZNSug6upuec7Sg', 'AIzaSyAeaWLxSHFEdwWEVVYajslt7R9eP0ZpLXQ',
                  'AIzaSyARBYHwwK5uPoNuS2iN3UOg8fQGRgHLz78', 'AIzaSyDpkHWwId9J1mMCqu9mirXPEwpM3XTs0GU',
                  'AIzaSyAIAT5ptZVJqiFiTQZxAXp6KT8jREfKidU', 'AIzaSyDXBLyip9Go5V4COM2w-ELE-oV1Zm8EQRk',
                  'AIzaSyDBA9EWB_zNWC6XjDu9mGyIuuV6QSL_ABM', 'AIzaSyD_YqB4d_-xKcmNP9jJCiPkJYDS8J3f6pI',
                  'AIzaSyAAqEuv_SHtc0ByecPXSQiKH5f2p2t5oP4']
    ApiKey = random.choice(ApikeyList)

    GoogleResult = GetDataInAddress(LocationName, ApiKey)

    ListLocation = stucture_postcode_localities(GoogleResult)
    for i in ListLocation:
        print i

    '''
    Test = GetDataInAddress(LocationName)
    print Test[1]
    print Test

    print DataStructure(Test)
    Cordinates_1 = '50.4775'
    Cordinates_2 = '1.85944444444'
    #Res = GetDataInCordinates(Cordinates_1,Cordinates_2)
    #print Res
    #print DataStructure(Res)
    #Lang = u'fr'



    #LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/GoogleDataPageUpdate_13_06_17_2')


    #print GetLangPlaceId(PlaceId,Lang)

    #PlaceId = 'ChIJX7UA7TFG3UcROlsxcPXIUbs'
    #print GetLangPlaceId(PlaceId,'ru'),GetLangPlaceId(PlaceId,'ua'),GetLangPlaceId(PlaceId,'fr')

    PlaceId = 'ChIJQZHKaGJI6EcREPdpgT7xCgQ'

    #GoogleResult = GetResultInSendPlaceId(PlaceId)
    #print SplitGetDataInPlaceId(GoogleResult)
    '''