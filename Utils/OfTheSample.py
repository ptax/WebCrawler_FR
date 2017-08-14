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
import Utils.GetListInFile
import Utils.convert_to_latin


def UrlWikiConverName(Url):
    Url = urllib.unquote(Url)
    Url = Url.replace('/wiki/', '')
    Url = re.sub('_\(.*', '', Url)
    return Url


def NameWinkiConvertUrl(Name):
    Name = Name.replace(' ', '_')
    return Name


def get_moderation_canton():
    Up_Commune = r'../WorkBaseFile/Up_Commune'
    Up_Commune_list = Utils.GetListInFile.Run(Up_Commune)
    print len(Up_Commune_list)
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_Up_Moreration_commune_3')
    Dict_Up_Commune = {}
    for up_key in Up_Commune_list:
        Data = load_base[up_key]
        Dict_Up_Commune[up_key] = Data

    name_dict = '../WorkBaseFile/28_07_17_Moderation_Commun_Onli'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_Up_Commune, name_dict)


def inseeName_not_egual_wiki_url():
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release_3')
    Dict_not_egual = {}
    for Data, Keys in zip(load_base.values(), load_base.keys()):

        try:
            if UrlWikiConverName(Data['Wiki_Url']) == NameWinkiConvertUrl(Data['InseeXls_NameCommune']):
                F_Compare_InseeXls_NameCommune_Wiki_Url = True
            else:
                F_Compare_InseeXls_NameCommune_Wiki_Url = False
        except:
            F_Compare_InseeXls_NameCommune_Wiki_Url = 'None'
        if F_Compare_InseeXls_NameCommune_Wiki_Url == False:
            Dict_not_egual[Keys] = Data
        else:
            pass
    name_dict = '../WorkBaseFile/02_08_17_inseeName_not_egual_wiki_url'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_not_egual, name_dict)


def inseeName_not_egual_google_name():
    load_base = Utils.SaveAndLoadDictFile.LoadDict(
        '../WorkBaseFile/01_08_17_inseeName_not_egual_google_name_UP_coodinates')
    Dict_not_egual = {}
    for Data, Keys in zip(load_base.values(), load_base.keys()):

        try:
            F_ComunName_Comprasions = Utils.convert_to_latin.comun_name_wiki_google_comparisons(
                str(Data['G_Locality_long_name']).decode('utf-8'), str(Data['InseeXls_NameCommune']).decode('utf-8'))
            NameWiki = F_ComunName_Comprasions['Wiki_NameSnipet_lower'].replace(' ', '')
            NameGoogle = F_ComunName_Comprasions['G_Locality_short_name_lower'].replace(' ', '')

            if NameWiki == NameGoogle:
                F_Compare_InseeXls_NameCommune_G_Locality_long_name = True
            else:
                F_Compare_InseeXls_NameCommune_G_Locality_long_name = False
        except:
            F_Compare_InseeXls_NameCommune_G_Locality_long_name = 'None'

        if F_Compare_InseeXls_NameCommune_G_Locality_long_name == False:
            print NameWiki, NameGoogle
            Dict_not_egual[Keys] = Data
        else:
            pass

    name_dict = '../WorkBaseFile/01_08_17_inseeName_not_egual_google_name_UP_coodinates_test'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_not_egual, name_dict)


def g_type_nonel():
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_Up_Moderation')
    print len(load_base)
    Dict_not_egual = {}
    for Data, Keys in zip(load_base.values(), load_base.keys()):
        print Keys, Data['G_Types']
        try:
            G_Types = Data['G_Types']
        except:
            G_Types = 'None'

        if G_Types in 'None':
            Dict_not_egual[Keys] = Data
        else:
            pass
    name_dict = '../WorkBaseFile/01_08_17_G_Type_none'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_not_egual, name_dict)


def southwest_and_northeast_none():
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release_2')
    print len(load_base)
    Dict_not_egual = {}
    for Data, Keys in zip(load_base.values(), load_base.keys()):
        try:
            G_Coordinates_northeast_Lat_1 = Data['G_Coordinates_northeast_Lat_1']
        except:
            G_Coordinates_northeast_Lat_1 = 'None'

        if G_Coordinates_northeast_Lat_1 == 'None':
            Dict_not_egual[Keys] = Data
        else:
            pass
    name_dict = '../WorkBaseFile/02_08_17_G_Coordinates_northeast'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_not_egual, name_dict)


def post_code_not_int():
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release_2')
    print len(load_base)
    Dict_not_egual = {}
    for Data, Keys in zip(load_base.values(), load_base.keys()):
        try:
            W_CodePostal = Data['W_CodePostal'].replace(',', '').strip()
        except:
            W_CodePostal = 'None'
        try:
            W_CodePostal = int(W_CodePostal)
        except:
            W_CodePostal = False

        if W_CodePostal == False:
            Dict_not_egual[Keys] = Data
            # print Keys,Data['W_CodePostal']
        else:
            pass
    name_dict = '../WorkBaseFile/02_08_17_wiki_post_code_not_int'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_not_egual, name_dict)


def G_type_not_locality():
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release_2')
    print len(load_base)
    Dict_not_egual = {}
    for Data, Keys in zip(load_base.values(), load_base.keys()):
        try:
            G_type = Data['G_Types']
        except:
            G_type = 'None'

        if 'locality' in str(G_type):
            pass
        else:
            Dict_not_egual[Keys] = Data

    name_dict = '../WorkBaseFile/08_09_17_not_in_locality'
    Utils.SaveAndLoadDictFile.SaveDict(Dict_not_egual, name_dict)


if __name__ == '__main__':
    # post_code_not_int()
    #G_type_not_locality()
    load_base = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/08_09_17_not_in_locality')
    print len(load_base)
    #print load_base[39177]['G_Types']
    #print load_base['70369']['Wiki_Url']
    for Data, Keys in zip(load_base.values(), load_base.keys()):
        print Data['G_Types']

