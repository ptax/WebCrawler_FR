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
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/26_06_17')
    WorkDict = LoadMyDict.copy()

    c = 0
    for Data in WorkDict.values():
        c +=1
        try:
            CodeCommune = Data['InseeXls_CodeCommune']
            NameCommene = Data['InseeXls_NameCommune']
            if int(Data['ColResultInSnipet']) == 1:
                if u'None' in str(Data['Wiki_UrlInCommuneSnipet']):
                    print CodeCommune,Data['Wiki_Old_UrlInCommune']
                    MyData = {'Wiki_UrlInCommuneSnipet':Data['Wiki_Old_UrlInCommune'],
                              'Wiki_NameSnipet':Data['Wiki_Old_NameSnipet'],
                              'Wiki_Old_UrlInCommune':'None',
                              'Wiki_Old_NameSnipet':'None'
                              }
                    WorkDict[CodeCommune].update(MyData)
                else:pass
            else:pass
        except:pass
    NameDict = '../WorkBaseFile/26_06_17_1'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
    print len(WorkDict)
    '''
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/26_06_17_1')

    T = LoadMyDict['93039']
    print T
    print T['Wiki_Url'],T['Wiki_UrlInCommuneSnipet'],T['Wiki_NameSnipet'],T['Wiki_Old_UrlInCommune'],T['Wiki_Old_NameSnipet']
