# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

import csv
import Utils.SaveAndLoadDictFile
import DataStructure.FirstColumHeader
import urllib
import re
import ClearName
import Utils.convert_to_latin
import Utils.GetListInFile


def ReplaceCooma(Str):
    Str = re.sub(",$", '', str(Str))
    Str = re.sub("^,", '', str(Str))
    return str(Str).strip()


def UrlWikiConverName(Url):
    Url = urllib.unquote(Url)
    Url = Url.replace('/wiki/', '')
    Url = re.sub('_\(.*', '', Url)

    return Url.replace(u'_', ' ')


if __name__ == '__main__':

    list_del_commune = Utils.GetListInFile.Run('../WorkBaseFile/del_list')

    list_ne_sovpal = []
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/18_07_17_Update_street_address_3')
    WorkDict = LoadMyDict.copy()
    MyDict = {}
    print len(WorkDict)
    for i in list_del_commune:
        try:
            del WorkDict[i]
        except:
            pass
    NameDict = '../WorkBaseFile/23_07_17_Del_Change_Commune'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, NameDict)
    print len(LoadMyDict)
    print len(WorkDict)

    '''
    for Data,Keys in zip(WorkDict.values(),WorkDict.keys()):
        InseeXls_NameCommune = str(Data['InseeXls_NameCommune']).replace("L' ","L'")
        Wiki_UrlInCommuneSnipet = UrlWikiConverName(str(Data['Wiki_UrlInCommuneSnipet']))
        try:
            ColResul = int(Data['ColResultInSnipet'])
        except:
            ColResul = 1


        if ColResul >=	2:
            print InseeXls_NameCommune,Wiki_UrlInCommuneSnipet
            list_ne_sovpal.append(Keys)
            MyDate = {Keys:Data}
            MyDict.update(MyDate)
        else:
            pass
    NameDict = '../WorkBaseFile/19_08_17_snippet_2'
    Utils.SaveAndLoadDictFile.SaveDict(MyDict,NameDict)
    print len(WorkDict)

    print len(WorkDict)
    print len(list_ne_sovpal)
    print len(MyDict)
    '''


