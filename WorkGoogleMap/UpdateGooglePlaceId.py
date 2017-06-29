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
        '''
        LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/GoogleDataPage_12_06_17')

        print len(LoadMyDict)
        WorkDict = LoadMyDict.copy()

        c = 0
        for data in WorkDict.values():
            c +=1

            try:
                PlaceId = str(data['G_PlaceId']).strip()
            except KeyError:
                PlaceId = 'None'
            if PlaceId == 'None':
                try:
                    FR = str(data['W_Pays']).strip()
                    CodeCommene = str(data['InseeXls_CodeCommune']).strip()
                    NameCommune = str(data['InseeXls_NameCommune']).strip()



                    Cordinates = str(data['W_Cordommees']).replace('ou,','S').split(',')
                    Cordinat_1 = Utils.ConvertCordinates.dms2dec(Cordinates[0])
                    Cordinat_2 = Utils.ConvertCordinates.dms2dec(Cordinates[1])

                    GoogleResult = GetDataInCommune.GetDataInCordinates(str(Cordinat_1),str(Cordinat_2))
                    DictGoogle = GetDataInCommune.DataStructure(GoogleResult)
                    print c,NameCommune,CodeCommene,DictGoogle['G_AddressComponents_locality_ShortName'],Cordinat_1,Cordinat_2,DictGoogle['G_PlaceId']

                    WorkDict[CodeCommene].update(DictGoogle)
                    DataInSaveFile = '{' + "'"+  str(CodeCommene) + "':" + str(DictGoogle)  + '}'
                    text_file = open("../WorkBaseFile/GoogleDataUpdate_String_Dict_3.txt", "a")
                    text_file.write(str(DataInSaveFile) +'\n')
                except:
                    pass
            else:
                pass





        NameDict = '../WorkBaseFile/GoogleDataPageUpdate_13_06_17_2'
        Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
        print len(WorkDict)
        '''

        LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/1_UpdateSendCoordinates_14_06_17_3')
        WorkDict = LoadMyDict.copy()



        for CordinatesDict in open('../WorkBaseFile/1_Update_Cordinates.txt'):


            CordinatesDict = str(CordinatesDict).strip()
            print CordinatesDict

            Data = {"How_Get_GooglePlaceID":'SendCoordinates'}
            WorkDict[CordinatesDict].update(Data)


        NameDict = '../WorkBaseFile/1_UpdateSendCoordinates_14_06_17_3'
        Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
        print len(LoadMyDict['46134'])
        print len(WorkDict['46134'])
        print WorkDict['46134']

        '''
        c = 0
        listCordinate = []
        for data in LoadMyDict.values():
            c +=1
            try:
                PlaceId = str(data['G_PlaceId']).strip()
            except KeyError:
                PlaceId = 'None'
            if PlaceId == 'None':
                CodeCommene = str(data['InseeXls_CodeCommune']).strip()
                NameCommune = str(data['InseeXls_NameCommune']).strip()

                listCordinate.append(c)


                print c,NameCommune,CodeCommene

                #DataInSaveFile = '{' + "'"+  str(CodeCommene) + "':" + str(DictGoogle)  + '}'
                text_file = open("../WorkBaseFile/1_Update_Cordinates.txt", "a")
                text_file.write(str(CodeCommene) +'\n')
        print len(listCordinate)

        '''