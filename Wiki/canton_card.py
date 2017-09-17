# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
from GetDataInWikiTable import GetHtml, GetInformation_canton, WikiNameCommune, GetLanguages, FilterLanguages
import Utils.SaveAndLoadDictFile
import urllib


def get_info(url):
    dict_info = {}
    html = GetHtml(url)
    href_lang = html[1]
    table_info = html[0]
    dict_info.update({'Wiki_name_canton': WikiNameCommune(table_info)})
    dict_info.update(GetInformation_canton(table_info))
    # print FilterLanguages(GetLanguages(href_lang))
    dict_info.update(FilterLanguages(GetLanguages(href_lang)))
    return dict_info


def get_cards():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_24_08_17_insee_snippet_3')
    work_dict = LoadMyDict.copy()
    c = 0
    for data in work_dict.values():
        c += 1
        code_canton = data['I_Code_canton']
        url = 'https://fr.wikipedia.org' + urllib.unquote(data['Wiki_Url']).decode('utf8').strip()
        dict_info = get_info(url)
        work_dict[code_canton].update(dict_info)
        print c, code_canton, url, dict_info['Wiki_name_canton'], dict_info['W_Pays']
    NameDict = '../WorkBaseFile/arrondissements_24_08_17_cards'
    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


if __name__ == '__main__':
    url = 'https://fr.wikipedia.org/wiki/Canton_d%27Aix-en-Provence-1'
    # dict_info = get_info(url)
    #print dict_info
    #get_cards()
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Cantons_20_08_17_cards')
    print len(LoadMyDict)
    test_dict = LoadMyDict['13 09']
    print test_dict
    print len(test_dict)
    print test_dict['W_Code_Canton'], test_dict['I_Code_canton'], test_dict['Wiki_Url'], test_dict['W_Pays']
