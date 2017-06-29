# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os


import GetUrlCommuneInWiki
import Utils.GetListInFile
import Utils.SaveAndLoadDictFile
import DataStructure.InseeFr_Commune




if __name__ == '__main__':

    '''
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/GoogleUpdateData_15_06_17')
    WorkDict = LoadMyDict.copy()
    DictNameUpdate = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_ResultWikiUrl_26_06_17')
    DictNameUpdate_2 = DictNameUpdate.copy()

    c = 0
    for Data in WorkDict.values():
        c +=1
        #print Data

        try:
            CodeCommune = Data['InseeXls_CodeCommune']
            NameCommene = Data['InseeXls_NameCommune']

            print c, CodeCommune,NameCommene,DictNameUpdate_2[CodeCommune]['Wiki_UrlInCommuneSnipet']
            WorkDict[CodeCommune].update(DictNameUpdate_2[CodeCommune])
        except:
            pass



    NameDict = '../WorkBaseFile/UpdateName_26_06_17'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
    print len(WorkDict)
    '''
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/UpdateName_26_06_17')

    T = LoadMyDict['63024']
    print T
    print T['Wiki_Url']