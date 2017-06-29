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
    DictNameUpdate = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_ResultWikiUrl_21_06_17_2')
    WorkDict = DictNameUpdate.copy()
    c = 0
    DictCommune = {}
    for Data,Keys in zip(WorkDict.values(),WorkDict.keys()):
        c +=1
        try:
            DictCommune[Keys] = {'Wiki_UrlInCommuneSnipet':Data['Wiki_UrlInCommune'],
                    'Wiki_NameSnipet':Data['Wiki_NameSnipet'],
                    'Wiki_Old_UrlInCommune':Data['Wiki_Old_UrlInCommune'],
                    'Wiki_Old_NameSnipet':Data['Wiki_Old_NameSnipet'],
                    'ColResultInSnipet':Data['ColResultInSnipet']
                    }
        except:
                DictCommune[Keys] = {'Wiki_UrlInCommuneSnipet':'None',
                    'Wiki_NameSnipet':'None',
                    'Wiki_Old_UrlInCommune':'None',
                    'Wiki_Old_NameSnipet':'None',
                    'ColResultInSnipet':'None'
                    }
                pass

    NameDict = '../WorkBaseFile/Dict_ResultWikiUrl_26_06_17'
    Utils.SaveAndLoadDictFile.SaveDict(DictCommune,NameDict)
    print len(WorkDict)
    print len(DictCommune)
