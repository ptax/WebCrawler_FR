# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
from GetDataInWikiTable import GetHtml, GetInformation_departements, WikiNameCommune, GetLanguages, FilterLanguages, \
    wiki_coordinates
import Utils.SaveAndLoadDictFile
import urllib


def get_info(url):
    dict_info = {}
    html = GetHtml(url)
    href_lang = html[1]
    table_info = html[0]
    Coordinates = wiki_coordinates(table_info)
    dict_info.update({'Wiki_name_departement': WikiNameCommune(table_info)})
    dict_info.update(GetInformation_departements(table_info))
    dict_info.update(FilterLanguages(GetLanguages(href_lang)))
    return dict_info


def get_cards():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Departements_28_08_17_insee_snippet_1')
    work_dict = LoadMyDict.copy()
    c = 0
    for data in work_dict.values():
        try:
            W_pays = data['W_Pays']
        except:
            W_pays = 'None'
        if W_pays == 'None':

            try:

                c += 1
                code_canton = data['I_Code_departament']
                url = 'https://fr.wikipedia.org' + urllib.unquote(data['Wiki_Url']).decode('utf8').strip()
                dict_info = get_info(url)
                work_dict[code_canton].update(dict_info)
                print c, code_canton, url, dict_info['Wiki_name_departement'], dict_info['W_Pays']
            except KeyError:
                print 'Err', url, KeyError

        else:
            pass

    NameDict = '../WorkBaseFile/Departements_28_08_17_cards'

    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


def up_region():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_25_08_17_cards_up_2')
    work_dict = LoadMyDict.copy()

    for data in work_dict.values():
        W_pays = data['W_Pays']
        code_canton = data['I_Code_departament']
        my_data = {'W_Pays': 'France'}

        work_dict[code_canton].update(my_data)
    NameDict = '../WorkBaseFile/arrondissements_25_08_17_cards_up_3'

    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


if __name__ == '__main__':
    url = 'https://fr.wikipedia.org/wiki/Ain_(d%C3%A9partement)'
    # print get_info(url)

    #get_cards()
    #up_region()

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Departements_28_08_17_cards')
    print len(LoadMyDict)
    test_dict = LoadMyDict['01']
    print test_dict

    for i in LoadMyDict.values():
        try:
            print i['I_Code_departament'], i['Wiki_Url'], i['W_Pays'].strip(), i['W_Creation_du_departementt'].strip()

        except:
            print 'Erro', i['I_Code_departament'], i['Wiki_Url']
            pass

