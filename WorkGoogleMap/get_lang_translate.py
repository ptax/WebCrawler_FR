# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import Utils.SaveAndLoadDictFile


def json_google_coordinates(lat, lng, lang):
    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + lat + "," + lng + "&sensor=true&language=" + lang + "&key=AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg"
    url = urllib.unquote(url).decode('utf8')
    try:
        response = json.loads(urlopen(url).read())
        status = response["status"]
        if status == u"OK":
            results = response.get("results")
            status = u"OK"
            return results[1], status
    except:
        response = 'None'
        status = "None"
        return response, status


def debriefing_data(google_data):
    DictMyData = {
        u'G_Locality_long_name' + '_' + lang: u'None',
        u'G_AdminLevel_1_long_name' + '_' + lang: u'None',
        u'G_AdminLevel_2_long_name' + '_' + lang: u'None',
        u'G_AdminLevel_2_types' + '_' + lang: u'None',
        u'G_Country_long_name' + '_' + lang: u'None',
    }
    try:
        GoogleStatus = google_data[1]
        GoogleResult = google_data[0]
    except:
        pass
        GoogleStatus = 'None'
        GoogleResult = 'None'
    if GoogleStatus == u"OK":

        Adress = GoogleResult['address_components']
        c = 0
        for Data in Adress:

            c += 1
            types = ','.join(Data['types'])

            if u'locality,political' in types:
                DataUpdate = {u'G_Locality_long_name' + '_' + lang: Data['long_name']}
                DictMyData.update(DataUpdate)
            elif u'administrative_area_level_1,political' in types:
                DataUpdate = {u'G_AdminLevel_1_long_name' + '_' + lang: Data['long_name']}
                DictMyData.update(DataUpdate)
            elif u'administrative_area_level_2,political' in types:
                DataUpdate = {u'G_AdminLevel_2_long_name' + '_' + lang: Data['long_name']}
                DictMyData.update(DataUpdate)
            elif u'country,political' in types:
                DataUpdate = {u'G_Country_long_name' + '_' + lang: Data['long_name']}
                DictMyData.update(DataUpdate)

    return DictMyData


if __name__ == '__main__':
    '''
    lat = '42.9406517'
    lng = '1.8000263'
    lang = u'NO'
    google_data = json_google_coordinates(lat, lng, lang)
    data =  debriefing_data(google_data)
    print data
    print data['G_Locality_long_name_NO']
    '''

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/30_06_17_1')

    print len(LoadMyDict)
    WorkDict = LoadMyDict.copy()

    list_error = []
    List_Lang = [u'ru', u'uk', u'en', u'de', u'pl', u'es', u'pt', u'it']
    c = 0
    for Data in WorkDict.values():
        c += 1
        try:
            CodeCommune = Data['InseeXls_CodeCommune']
            NameCommene = Data['InseeXls_NameCommune']
            lat = str(Data['G_Coordinates_location_Lat_3'])
            lng = str(Data['G_Coordinates_location_Lng_3'])
            for lang in List_Lang:
                LangName = Data['G_Locality_long_name' + '_' + lang]
                if u'None' in str(LangName):  # Update Lang If None (if yor only new lang del this if)


                    google_data = json_google_coordinates(lat, lng, lang)
                    my_data = debriefing_data(google_data)
                    print c, CodeCommune, NameCommene, my_data['G_Locality_long_name_' + lang]
                    WorkDict[CodeCommune].update(my_data)
                    DataInSaveFile = '{' + "'" + str(CodeCommune) + "':" + str(my_data) + '}'
                    text_file = open("../WorkBaseFile/02_07_17_5_Lang_UpDate.txt", "a")
                    text_file.write(str(DataInSaveFile) + '\n')
                else:
                    pass
        except:
            list_error.append(CodeCommune)
            pass

    NameDict = '../WorkBaseFile/02_07_17'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, NameDict)

    print len(WorkDict)
    print len(list_error), 'Error'
    for CodeInseeError in list_error:
        print CodeInseeError

        # LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/30_06_17')
        # MyId = LoadMyDict['89378']
        #print MyId
        #print MyId['G_Locality_long_name_uk'], MyId['G_Locality_long_name_ru'], MyId['G_Locality_long_name_en'], MyId['InseeXls_CodeCommune'],MyId['G_Name_uk']
