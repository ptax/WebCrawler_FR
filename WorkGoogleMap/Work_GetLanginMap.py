# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

import csv
import Utils.SaveAndLoadDictFile
import DataStructure.FirstColumHeader
import GetDataInCommune


if __name__ == '__main__':

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/GoogleDataPageUpdate_13_06_17_2')

    print len(LoadMyDict)
    WorkDict = LoadMyDict.copy()

    c = 0
    for Data in WorkDict.values():
        c +=1
        try:
            CodeCommune = Data['InseeXls_CodeCommune']
            NameCommene = Data['InseeXls_NameCommune']
            PlaceId = Data['G_PlaceId']
            G_Name_ru = GetDataInCommune.GetLangPlaceId(PlaceId,u'ru')
            G_Name_uk = GetDataInCommune.GetLangPlaceId(PlaceId,u'uk')
            G_Name_en = GetDataInCommune.GetLangPlaceId(PlaceId,u'en')
            DictLangGoogleName = {'G_Name_ru':G_Name_ru,
                        'G_Name_uk':G_Name_uk,
                        'G_Name_en':G_Name_en
                    }


            print c,CodeCommune,NameCommene,G_Name_ru,G_Name_uk,G_Name_en

            WorkDict[CodeCommune].update(DictLangGoogleName)
            DataInSaveFile = '{' + "'"+  str(CodeCommune) + "':" + str(DictLangGoogleName)  + '}'
            text_file = open("../WorkBaseFile/DictLangGoogleName_13_06_17.txt", "a")
            text_file.write(str(DataInSaveFile) +'\n')
        except:
            pass

    NameDict = '../WorkBaseFile/GoogleLangFirstThree_14_06_17'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
    print len(WorkDict)

    #LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/GoogleLangFirstThree_14_06_17')
    #print LoadMyDict['88395']

