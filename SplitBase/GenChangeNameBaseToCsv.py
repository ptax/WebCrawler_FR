# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

sys.setdefaultencoding('utf-8')
import os
from bs4 import BeautifulSoup
import urllib2
import codecs
import re
import urllib
import collections
import Utils.SaveAndLoadDictFile
import Utils.ClearName


def read_csv_change_communes_insee():
    """
        Return Dict Format Structure in data in file Code Insee in insee.fr
        You put list in tree colum and dict return
    """
    NameFile = os.path.abspath('../WorkBaseFile/ChangeName_2.csv')
    ListDataInInseeXls = Utils.GetListInFile.Run(NameFile)
    DictCommuneInsee = {}

    ListCodeCommunes = []
    for NumCodeInsee in ListDataInInseeXls:
        data = NumCodeInsee.split(';')
        InseeChange_DepComN = str(data[0]).strip()
        ListCodeCommunes.append(InseeChange_DepComN)

    ListCodeCommunes = [x for x in ListCodeCommunes if x]

    ListNumCodeInse = countDuplicatesInList(ListCodeCommunes)

    dict_num = {}
    for CodeCumene in ListNumCodeInse:
        dict_num[CodeCumene[0]] = CodeCumene[1]
    print dict_num['50487']

    c = 0
    for data in ListDataInInseeXls:
        c += 1
        data = data.split(';')
        InseeChange_DepComN = str(data[0]).strip()
        InseeChange_NomCN = str(data[1]).strip()
        InseeChange_DepComA = str(data[2]).strip()
        InseeChange_NomCA = str(data[3]).strip()
        InseeChange_ComDLG = str(data[4]).strip()
        InseeChange_Date1 = str(data[5]).strip()
        InseeChange_Date2 = str(data[6]).strip()
        InseeChange_Date3 = str(data[7]).strip()

        try:
            NumCode = dict_num[InseeChange_DepComN]
        except:
            NumCode = 0

        CodeInseeTheme = str(InseeChange_DepComN) + '_' + str(NumCode) + '_' + str(InseeChange_DepComA)
        print c, CodeInseeTheme

        DictCommuneInsee[CodeInseeTheme] = {'InseeChange_DepComN': InseeChange_DepComN,
                                            'InseeChange_NomCN': InseeChange_NomCN,
                                            'InseeChange_DepComA': InseeChange_DepComA,
                                            'InseeChange_NomCA': InseeChange_NomCA,
                                            'InseeChange_ComDLG': InseeChange_ComDLG,
                                            'InseeChange_Date1': InseeChange_Date1,
                                            'InseeChange_Date2': InseeChange_Date2,
                                            'InseeChange_Date3': InseeChange_Date3


                                            }

    name_dict = '../WorkBaseFile/12_07_17_trust_codirovka'
    Utils.SaveAndLoadDictFile.SaveDict(DictCommuneInsee, name_dict)
    print len(DictCommuneInsee)


if __name__ == '__main__':
    pass


