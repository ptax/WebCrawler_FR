# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import Utils.SaveAndLoadDictFile
import GetDataInCommune



def StructurCordinates(GoogleResult):
    DictMyData = {
                        u'G_Coordinates_northeast_Lat_1':'None',
                        u'G_Coordinates_northeast_Lng_1':'None',
                        u'G_Coordinates_southwest_Lat_2':'None',
                        u'G_Coordinates_southwest_Lng_2':'None',
                        u'G_Coordinates_location_Lat_3':'None',
                        u'G_Coordinates_location_Lng_3':'None'

                    }
    try:
        GoogleStatus = GoogleResult[1]
        GoogleResult = GoogleResult[0]
    except:
        pass
        GoogleStatus = 'None'
        GoogleResult = 'None'
    if GoogleStatus == u"OK":
        Geometry =  GoogleResult['geometry']
        for Key,Data in zip(Geometry.keys(),Geometry.values()):
            try:
                #print Key,Data
                if u'location' in Key:
                    #print str(Data['lat']),str(Data['lng'])
                    DataUpdate = {u'G_Coordinates_location_Lat_3' :Data['lat'],
                                  u'G_Coordinates_location_Lng_3':Data['lng']
                                  }

                    DictMyData.update(DataUpdate)
                elif u'viewport' in Key:
                    DataUpdate = {
                                    u'G_Coordinates_northeast_Lat_1':Data['northeast']['lat'],u'G_Coordinates_northeast_Lng_1':Data['northeast']['lng'],
                                    u'G_Coordinates_southwest_Lat_2':Data['southwest']['lat'],u'G_Coordinates_southwest_Lng_2':Data['southwest']['lng']
                                    }
                    DictMyData.update(DataUpdate)
                else:pass
            except:pass
    return DictMyData







if __name__ == '__main__':

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/26_06_17_3')
    WorkDict = LoadMyDict.copy()

    c = 0
    for Data in WorkDict.values():
        c +=1
        try:
            if u'None' in str(Data['G_Coordinates_northeast_Lat_1']):
                CodeCommune = Data['InseeXls_CodeCommune']
                W_Cordommees_Convert = Data['W_Cordommees_Convert'].split(',')

                Cordinat_1 = W_Cordommees_Convert[0]
                Cordinat_2 = W_Cordommees_Convert[1]
                GoogleResult = GetDataInCommune.GetDataInCordinates(Cordinat_1,Cordinat_2)
                UpdateCordinate = StructurCordinates(GoogleResult)
                WorkDict[CodeCommune].update(UpdateCordinate)
                print c,CodeCommune,Cordinat_1



                DataInSaveFile = '{' + "'"+  str(CodeCommune) + "':" + str(UpdateCordinate)  + '}'
                text_file = open("../WorkBaseFile/UpdateCordinate_26_06_17.txt", "a")
                text_file.write(str(DataInSaveFile) +'\n')
            else:
                pass
        except:pass

    NameDict = '../WorkBaseFile/26_06_17_5'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
    print len(WorkDict)