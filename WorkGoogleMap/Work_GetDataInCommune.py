# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import GetDataInCommune
import Utils.SaveAndLoadDictFile
import time
import Utils.ConvertCordinates
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)


if __name__ == '__main__':

    with Profiler() as p:
        LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/WikiDataPage_11_06_17_2')

        print len(LoadMyDict)
        WorkDict = LoadMyDict.copy()

        c = 0
        for data in WorkDict.values():
            c +=1

            try:
                CodeCommene = str(data['InseeXls_CodeCommune']).strip()
                CodePostal= str(data['W_CodePostal']).strip()
                NameCommune = str(data['InseeXls_NameCommune']).strip()
                FR = str(data['W_Pays']).strip()
                LocationName = CodePostal + NameCommune + ',' + FR.replace(',','')

                GoogleResult = GetDataInCommune.GetDataInAddress(LocationName)


                DictGoogle = GetDataInCommune.DataStructure(GoogleResult)
                print c,CodeCommene,NameCommune,DictGoogle['G_PlaceId']



                WorkDict[CodeCommene].update(DictGoogle)

                DataInSaveFile = '{' + "'"+  str(CodeCommene) + "':" + str(DictGoogle)  + '}'
                text_file = open("../WorkBaseFile/GoogleData_String_Dict_2.txt", "a")
                text_file.write(str(DataInSaveFile) +'\n')
            except KeyError:
                pass





        NameDict = '../WorkBaseFile/GoogleDataPage_12_06_17'
        Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
        print len(WorkDict)
    '''

    #LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/WikiDataPage_11_06_17_2')

    #print LoadMyDict['53131']['W_Cordommees']
    Cordinates = u'48° 26′ 28″ , 0° 48′ 16″ ou,'.replace('ou,','').split(',')
    Cordinat_1 = Utils.ConvertCordinates.dms2dec(Cordinates[0])
    Cordinat_2 = Utils.ConvertCordinates.dms2dec(Cordinates[1])
    print Cordinat_1,Cordinat_2
    '''
