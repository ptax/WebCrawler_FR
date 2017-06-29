# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

import Utils.SaveAndLoadDictFile
import GetDataInWikiTable
if __name__ == '__main__':

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/26_06_17_1')
    WorkDict = LoadMyDict.copy()

    c = 0
    for Data in WorkDict.values():
        c +=1
        try:
            CodeCommune = Data['InseeXls_CodeCommune']
            Url = 'https://fr.wikipedia.org' + str(Data['Wiki_Url'])

            print c,CodeCommune,Url

            LangHref = GetDataInWikiTable.GetHtml(Url)[1]
            ListLanguages = GetDataInWikiTable.GetLanguages(LangHref)
            DictLang = GetDataInWikiTable.FilterLanguages(ListLanguages)
            WorkDict[CodeCommune].update(DictLang)
            DataInSaveFile = '{' + "'"+  str(CodeCommune) + "':" + str(DictLang)  + '}'
            text_file = open("../WorkBaseFile/26_06_17_2.txt", "a")
        except:
            pass

    NameDict = '../WorkBaseFile/26_06_17_3'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
    print len(WorkDict)

    '''
    c = 0

    ListNone = []
    for Data in WorkDict.values():
        c +=1
        try:

            CodeCommune = Data['InseeXls_CodeCommune']
            #print Data['Wiki_Old_UrlInCommune']
            #print c,CodeCommune,Data['W_Departement'],Data['G_PlaceId'],Data['Wiki_Old_NameSnipet'],Data['Wiki_NameSnipet'],Data['Wiki_UrlInCommuneSnipet']
            if u'None' in str(Data['Wiki_UrlInCommuneSnipet']):
                ListNone.append(CodeCommune)
                #print c,CodeCommune, Data['Wiki_UrlInCommune']
            else:
                pass
        except:
            pass
    print ListNone
    print len(ListNone)
    '''
    #LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/26_06_17')

    #T = LoadMyDict['63024']
    #T = LoadMyDict['89370']
    #print T['Wiki_Url']
    #print T['W_Name_uk'],T['Wiki_Url'],T['W_Url_uk'],T['W_Url_en']

