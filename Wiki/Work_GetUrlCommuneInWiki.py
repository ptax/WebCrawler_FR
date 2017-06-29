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
    ListCommuneInInseeFr = Utils.GetListInFile.Run('../WorkBaseFile/BaseCommuneInInseeFR')
    print len(ListCommuneInInseeFr)
    DictCommuneInInseeFr =  DataStructure.InseeFr_Commune.DictCommuneInsee(ListCommuneInInseeFr)
    for Data in DictCommuneInInseeFr.values():
        CodeCommune = Data['InseeXls_CodeCommune']
        Wiki_Url = GetUrlCommuneInWiki.Run(CodeCommune)
        print  Data['InseeXls_CodeCommune'], Data['InseeXls_NameCommune'], Wiki_Url

        DictCommuneInInseeFr[CodeCommune].update({'Wiki_Url':Wiki_Url})
    NameDict = '../WorkBaseFile/Dict_WikiUrl_08_06_17_2'
    Utils.SaveAndLoadDictFile.SaveDict(DictCommuneInInseeFr,NameDict)
    print len(DictCommuneInInseeFr)
