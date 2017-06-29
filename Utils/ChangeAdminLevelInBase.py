# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import urllib
import csv
import Utils.SaveAndLoadDictFile
import DataStructure.FirstColumHeader
import urllib
import re


def ReplaceCooma(Str):
    Str = re.sub(",$", '', Str)
    Str = re.sub("^,", '', Str)
    return Str


def UrlWikiConverName(Url):
    Url = urllib.unquote(Url)
    Url = Url.replace('/wiki/', '')
    Url = re.sub('_\(.*', '', Url)
    return Url


def NameWinkiConvertUrl(Name):
    Name = Name.replace(' ', '-')
    return Name


if __name__ == '__main__':
    t = u'Maisnil-l%C3%A8s-Ruitz'
    print urllib.unquote(t).decode('utf-8')
    # DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/GoogleUpdateData_15_06_17')
    #print DictFile['62540']
    Data = {'W_Cordommees_Convert': '50.4527777778,2.58583333333', 'W_Name_ro': u'Maisnil-l\xe8s-Ruitz',
            'G_AddressComponents_localityCountry_ShortName': u'FR', 'W_Name_ru': '',
            'G_Coordinates_northeast_Lng_1': 2.6007489, 'InseeXls_CodeCommune': '62540',
            'W_Name_es': u'Maisnil-l\xe8s-Ruitz', 'G_AddressComponents_localityCountry_LongName': u'France',
            u'W_CodeCommune': u'62540,', u'W_Region': u'Hauts-de-France,', u'G_Locality_types': u'locality,political',
            u'G_Country_types': u'country,political', u'G_AdminLevel_2_types': u'administrative_area_level_2,political',
            'W_Url_es': u'https://es.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz',
            'W_Name_uk': u'\u041c\u0435\u043d\u0456\u0439-\u043b\u0435-\u0420\u044e\u0457\u0446',
            'G_Coordinates_location_Lng_3': 2.5809669, u'W_Arrondissement': u'B\xe9thune,',
            'G_AddressComponents_locality_ShortName': u'Maisnil-l\xe8s-Ruitz',
            'W_Url_en': u'https://en.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz',
            u'G_Locality_long_name': u'Maisnil-l\xe8s-Ruitz', 'G_Coordinates_southwest_Lng_2': 2.5559339,
            u'W_Canton': u'Bruay-la-Buissi\xe8re,',
            'W_Url_uk': u'https://uk.wikipedia.org/wiki/\u041c\u0435\u043d\u0456\u0439-\u043b\u0435-\u0420\u044e\u0457\u0446',
            u'W_Pays': u'France,', 'W_Name_de': u'Maisnil-l\xe8s-Ruitz', 'G_Coordinates_northeast_Lat_1': 50.461015,
            'W_Name_da': '', 'G_Name_ru': None, 'G_Types': u'locality,political', u'W_CodePostal': u'62620,',
            'W_Name_pt': u'Maisnil-l\xe8s-Ruitz', u'G_AdminLevel_2_long_name': u'Pas-de-Calais',
            'W_Url_pl': u'https://pl.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz', 'W_Name_cs': '',
            u'W_Altitude': u'Min.\xa091 m\xa0\u2013 Max.\xa0181 m,',
            'G_AddressComponents_locality_Types': u'locality,political',
            'W_Url_pt': u'https://pt.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz',
            'W_Url_hu': u'https://hu.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz', 'W_Name_sl': '',
            'W_Name_sk': u'Maisnil-l\xe8s-Ruitz', 'W_Name_sh': '', 'W_Name_sv': u'Maisnil-l\xe8s-Ruitz',
            'G_Name_uk': None, u'W_Population': u',1\xa0604 hab. (2014),',
            u'G_AdminLevel_1_types': u'administrative_area_level_1,political',
            'G_AddressComponents_locality_LongName': u'Maisnil-l\xe8s-Ruitz', 'G_Name_en': None,
            u'G_Country_short_name': u'FR', u'G_AdminLevel_1_long_name': u'Hauts-de-France',
            u'G_postal_code_types': u'postal_code', 'W_Url_no': u'',
            'W_Url_nl': u'https://nl.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz', 'W_Name_it': u'Maisnil-l\xe8s-Ruitz',
            'W_Url_bg': u'', u'W_Cordommees': u'50\xb0\xa027\u2032\xa010\u2033\xa0, 2\xb0\xa035\u2032\xa009\u2033\xa0,',
            'W_Url_ro': u'https://ro.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz', u'G_postal_code_short_name': u'62620',
            u'G_AdminLevel_1_short_name': u'Hauts-de-France',
            'W_Url_it': u'https://it.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz',
            u'W_Intercommunalite': u"Communaut\xe9 d'agglom\xe9ration de B\xe9thune-Bruay, Artois-Lys Romane,",
            'W_Url_ru': u'', 'W_Name_hr': '', 'W_Name_hu': u'Maisnil-l\xe8s-Ruitz', u'G_Country_long_name': u'France',
            'G_AddressComponents_localityLevel_2_ShortName': u'Pas-de-Calais',
            'G_AddressComponents_localityCountry_Types': u'country,political',
            'G_PlaceId': 'ChIJeTiETMoX3UcR0ONjgT7xCgQ', 'G_FormatAddress': u'62620 Maisnil-l\xe8s-Ruitz, France',
            u'G_Locality_short_name': u'Maisnil-l\xe8s-Ruitz',
            'G_AddressComponents_localityLevel_1_Types': u'administrative_area_level_1,political', 'W_Url_hr': u'',
            u'W_Departement': u'Pas-de-Calais,', 'W_Name_en': u'Maisnil-l\xe8s-Ruitz',
            'G_Coordinates_location_Lat_3': 50.45392700000001,
            'G_AddressComponents_localityLevel_2_LongName': u'Pas-de-Calais',
            'InseeXls_NameCommune': 'Maisnil-l\xc3\xa8s-Ruitz', 'W_Name_pl': u'Maisnil-l\xe8s-Ruitz',
            'W_Url_de': u'https://de.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz', 'W_Url_da': u'',
            'Wiki_Url': '/wiki/Maisnil-l%C3%A8s-Ruitz',
            'G_AddressComponents_localityLevel_2_Types': u'administrative_area_level_2,political', 'W_Name_bg': '',
            'InseeXls_Population': '1\xc2\xa0604', u'W_Superficie': u'5,56 km2,',
            u'G_AdminLevel_2_short_name': u'Pas-de-Calais', 'W_Url_cs': u'',
            'G_Coordinates_southwest_Lat_2': 50.4331679,
            'G_AddressComponents_localityLevel_1_ShortName': u'Hauts-de-France', 'W_Name_nl': u'Maisnil-l\xe8s-Ruitz',
            'W_Name_no': '', u'G_postal_code_long_name': u'62620', 'W_Url_sh': u'',
            'W_Url_sk': u'https://sk.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz',
            'G_AddressComponents_localityLevel_1_LongName': u'Hauts-de-France', 'W_Url_sl': u'',
            'W_Url_sv': u'https://sv.wikipedia.org/wiki/Maisnil-l\xe8s-Ruitz', u'W_Densite': u'288 hab./km2,'}
    v = re.sub(",$", '', Data[u'W_Cordommees'])
    g = re.sub(",$", '', Data[u'W_Population'])
    d = re.sub("^,", '', g)

    if Data['InseeXls_CodeCommune'] == ReplaceCooma(Data['W_CodeCommune']):
        print True
    else:
        print False
    t = 'Les Junies'
    v = '/wiki/Lussan_(Gers)'
    print UrlWikiConverName(v)
    if UrlWikiConverName(Data['Wiki_Url']) == NameWinkiConvertUrl(Data['InseeXls_NameCommune']):
        print True
    else:
        print False



