# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

from Utils.GetListInFile import Run
import Utils.SaveAndLoadDictFile


def get_dict():
    list_canton = Run('../input_base/arrondissements_insee.csv')
    dict_canton = {}
    for line in list_canton:
        data = line.split('\t')

        if len(data[1]) == 1:
            dep = '0' + str(data[1])
        else:
            dep = data[1]

        ar = data[2]
        code_arrondissements = str(dep) + ' ' + str(ar)
        dict_canton[code_arrondissements] = {'I_Region': data[0],
                                             'I_Dep': data[1],
                                             'I_Ar': data[2],
                                             'I_Cheflieu': data[3],
                                             'I_Tncc': data[4],
                                             'I_Artmaj': data[5],
                                             'I_Ncc': data[6],
                                             'I_Armin': data[7],
                                             'I_Nccent': data[8],
                                             'I_Code_Arrondissements': code_arrondissements
                                             }
    NameDict = '../WorkBaseFile/arrondissements_24_08_17_insee'
    Utils.SaveAndLoadDictFile.SaveDict(dict_canton, NameDict)


if __name__ == '__main__':
    get_dict()
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_24_08_17_insee')
    print len(LoadMyDict)
    for test in LoadMyDict.values():
        print test['I_Nccent'].strip(), test['I_Code_Arrondissements']

