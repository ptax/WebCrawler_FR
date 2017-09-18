# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

from Utils.GetListInFile import Run
import Utils.SaveAndLoadDictFile


def get_dict():
    list_canton = Run('../input_base/cantons_insee.csv')
    dict_canton = {}
    for line in list_canton:
        data = line.split('\t')
        if len(data[1]) == 1:
            dep = '0' + str(data[1])
        else:
            dep = data[1]
        if len(data[2]) == 1:
            canton = '0' + str(data[2])
        else:
            canton = data[2]
        code_cantone = str(dep) + ' ' + str(canton)
        dict_canton[code_cantone] = {'I_Region': data[0],
                                     'I_Dep': data[1],
                                     'I_Canton': data[2],
                                     'I_Typct': data[3],
                                     'I_Burcentral': data[4],
                                     'I_Tncc': data[5],
                                     'I_Artmaj': data[6],
                                     'I_Ncc': data[7],
                                     'I_Armin': data[8],
                                     'I_Nccent': data[9],
                                     'I_Code_canton': code_cantone
                                     }
    NameDict = '../WorkBaseFile/Cantons_18_08_17_insee'
    Utils.SaveAndLoadDictFile.SaveDict(dict_canton, NameDict)


if __name__ == '__main__':
    get_dict()
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Cantons_18_08_17_insee')
    print len(LoadMyDict)
    for test in LoadMyDict.values():
        print test['I_Nccent'].strip(), test['I_Code_canton']
