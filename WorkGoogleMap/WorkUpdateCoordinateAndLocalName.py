# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

import csv
import Utils.SaveAndLoadDictFile
import DataStructure.FirstColumHeader
import GetDataInCommune
import Utils.ConvertCordinates

import time

class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)
if __name__ == '__main__':
     with Profiler() as p:
        LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/1_UpdateSendCoordinates_14_06_17_3')
        WorkDict = LoadMyDict.copy()
        c = 0
        for data in WorkDict.values():
            c +=1

            try:
                PlaceId = str(data['G_PlaceId']).strip()

                CodeCommene = str(data['InseeXls_CodeCommune']).strip()
                NameCommune = str(data['InseeXls_NameCommune']).strip()

                Cordinates = str(data['W_Cordommees']).replace('ou,','S').split(',')
                Cordinate = str(Utils.ConvertCordinates.dms2dec(Cordinates[0])) + ',' + str(Utils.ConvertCordinates.dms2dec(Cordinates[1]))

                UpdateData = {'W_Cordommees_Convert':Cordinate}

                GoogleResult = GetDataInCommune.GetResultInSendPlaceId(PlaceId)
                DictGoogle =  GetDataInCommune.SplitGetDataInPlaceId(GoogleResult)

                print c,NameCommune,CodeCommene,PlaceId
                WorkDict[CodeCommene].update(UpdateData)
                WorkDict[CodeCommene].update(DictGoogle)

                DataInSaveFile = '{' + "'"+  str(CodeCommene) + "':" + str(DictGoogle)  + '}'
                text_file = open("../WorkBaseFile/GoogleUpdateData_15_06_17.txt", "a")
                text_file.write(str(DataInSaveFile) +'\n')
            except:
                pass



        NameDict = '../WorkBaseFile/GoogleUpdateData_15_06_17'
        Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
        print len(WorkDict)