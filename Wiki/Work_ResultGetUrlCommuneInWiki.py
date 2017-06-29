# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os


import GetResultUrlCommuneInWiki
import Utils.GetListInFile
import Utils.SaveAndLoadDictFile
import DataStructure.InseeFr_Commune


if __name__ == '__main__':

    ListCommuneInInseeFr = Utils.GetListInFile.Run('../WorkBaseFile/BaseCommuneInInseeFR')
    print len(ListCommuneInInseeFr)
    DictCommuneInInseeFr =  DataStructure.InseeFr_Commune.DictCommuneInsee(ListCommuneInInseeFr)
    c = 0
    for Data in DictCommuneInInseeFr.values():
        c += 1
        try:

            CodeCommune = Data['InseeXls_CodeCommune']
            NameCommune = Data['InseeXls_NameCommune']
            Wiki_Url = GetResultUrlCommuneInWiki.Run(NameCommune,CodeCommune)
            print  c,Data['InseeXls_CodeCommune'], Data['InseeXls_NameCommune'], Wiki_Url

            DictCommuneInInseeFr[CodeCommune].update(Wiki_Url)


            DataInSaveFile = '{' + "'"+  str(CodeCommune) + "':" + str(Wiki_Url)  + '}'
            text_file = open("../WorkBaseFile/Dict_ResultWikiUrl_21_96_17.txt", "a")
            text_file.write(str(DataInSaveFile) +'\n')
        except:
            pass


    NameDict = '../WorkBaseFile/Dict_ResultWikiUrl_21_06_17_2'
    Utils.SaveAndLoadDictFile.SaveDict(DictCommuneInInseeFr,NameDict)
    print len(DictCommuneInInseeFr)

    #LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_ResultWikiUrl_21_06_17_2')
    #print LoadMyDict['91137']