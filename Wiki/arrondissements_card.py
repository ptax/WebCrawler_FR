# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
from GetDataInWikiTable import GetHtml, GetInformation_arrondissement, WikiNameCommune, GetLanguages, FilterLanguages, \
    wiki_coordinates
import Utils.SaveAndLoadDictFile
import urllib


def get_info(url):
    dict_info = {}
    html = GetHtml(url)
    href_lang = html[1]
    table_info = html[0]
    Coordinates = wiki_coordinates(table_info)
    dict_info.update({'Wiki_name_arrondissement': WikiNameCommune(table_info)})
    dict_info.update(GetInformation_arrondissement(table_info))
    dict_info.update({'Wiki_Coordinates_lat': Coordinates[0], 'Wiki_Coordinates_lon': Coordinates[1]})
    dict_info.update(FilterLanguages(GetLanguages(href_lang)))
    return dict_info


def get_cards():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_25_08_17_cards_up_2')
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
                code_canton = data['I_Code_Arrondissements']
                url = 'https://fr.wikipedia.org' + urllib.unquote(data['Wiki_Url']).decode('utf8').strip()
                dict_info = get_info(url)
                work_dict[code_canton].update(dict_info)
                print c, code_canton, url, dict_info['Wiki_name_arrondissement'], dict_info['W_Pays']
            except KeyError:
                print 'Err', url, KeyError

        else:
            pass

    NameDict = '../WorkBaseFile/arrondissements_25_08_17_cards_up_2'

    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


def up_region():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_25_08_17_cards_up_2')
    work_dict = LoadMyDict.copy()

    for data in work_dict.values():
        W_pays = data['W_Pays']
        code_canton = data['I_Code_Arrondissements']
        my_data = {'W_Pays': 'France'}

        work_dict[code_canton].update(my_data)
    NameDict = '../WorkBaseFile/arrondissements_25_08_17_cards_up_3'

    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


if __name__ == '__main__':
    url = 'https://fr.wikipedia.org/wiki/Arrondissement_de_Gex'


    # get_cards()
    #up_region()
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_25_08_17_cards_up_3')
    print len(LoadMyDict)
    test_dict = LoadMyDict['34 1']

    for i in LoadMyDict.values():
        try:
            print i['I_Code_Arrondissements'], i['Wiki_Url'], i['W_Pays'].strip()
            pass
        except:
            print i['I_Code_Arrondissements'], i['Wiki_Url']
            pass

