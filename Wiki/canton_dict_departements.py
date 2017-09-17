# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

from Utils.GetListInFile import Run
import Utils.SaveAndLoadDictFile


def get_dict():
    list_canton = Run('../input_base/cantons_departements.csv')
    dict_canton = {}
    for line in list_canton:
        data = line.split('\t')
        if len(data[1]) == 1:
            dep = '0' + str(data[1])
        else:
            dep = data[1]
        code_departement = str(dep)
        dict_canton[code_departement] = {'I_Region': data[0],
                                         'I_Dep': data[1],
                                         'I_Chefleeu': data[2],
                                         'I_Tncc': data[3],
                                         'I_Ncc': data[4],
                                         'I_Nccenr': data[5],
                                         'I_Code_departament': code_departement
                                         }
    NameDict = '../WorkBaseFile/Departements_28_08_17_insee'
    Utils.SaveAndLoadDictFile.SaveDict(dict_canton, NameDict)


if __name__ == '__main__':
    get_dict()
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Departements_28_08_17_insee')
    print len(LoadMyDict)
    for test in LoadMyDict.values():
        print test['I_Nccenr'].strip(), test['I_Code_departament']

