# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import Wiki.GetDataInWikiTable
import Utils.SaveAndLoadDictFile
import time
import Utils.ConvertCordinates

import os

import WorkGoogleMap.GetDataInCommune
import Utils.SaveAndLoadDictFile
import time
import Utils.ConvertCordinates


if __name__ == '__main__':

    Url = "https://fr.wikipedia.org/wiki/Les_Deux_Alpes_(commune)"
    GetHtml = Wiki.GetDataInWikiTable.GetHtml(Url)
    Table = GetHtml[0]
    # print get_status(Table)

    DataDict = {}
    LangHref = GetHtml[1]
    DictTableInformation = Wiki.GetDataInWikiTable.GetInformation(Table)
    LanguagesDict = Wiki.GetDataInWikiTable.FilterLanguages(Wiki.GetDataInWikiTable.GetLanguages(LangHref))

    DictDatainWikiPage = DictTableInformation.copy()
    DictDatainWikiPage.update(LanguagesDict)

    Cordinates = str(DictDatainWikiPage['W_Cordommees']).replace('ou,', 'S').split(',')
    Cordinate = str(Utils.ConvertCordinates.dms2dec(Cordinates[0])) + ',' + str(
        Utils.ConvertCordinates.dms2dec(Cordinates[1]))
    Cordinates = Cordinate.split(',')
    Cordinat_1 = Cordinates[0]
    Cordinat_2 = Cordinates[1]


    #result = WorkGoogleMap.GetDataInCommune.GetDataInCordinates(Cordinat_1,Cordinat_2)

    Address = '14260,Ondefontaine,France'
    #Address=urllib.unquote(Address)
    #print Address

    result = WorkGoogleMap.GetDataInCommune.GetDataInAddress(Address)

    print result

    GoogleDataAdree = WorkGoogleMap.GetDataInCommune.StructureLocalType(result)

    GoogleDataCorrdinat = WorkGoogleMap.GetDataInCommune.GetCoordinatesInGoogle(result)

    DictDatainWikiPage.update(GoogleDataAdree)
    DictDatainWikiPage.update(GoogleDataCorrdinat)

    print DictDatainWikiPage
    print DictDatainWikiPage['G_FormatAddress']
    print DictDatainWikiPage['G_Types']
    print DictDatainWikiPage['G_Coordinates_northeast_Lat_1'], DictDatainWikiPage['G_Coordinates_northeast_Lng_1']
    print DictDatainWikiPage['G_Coordinates_southwest_Lat_2'], DictDatainWikiPage['G_Coordinates_southwest_Lng_2'],
    print DictDatainWikiPage['G_Coordinates_location_Lat_3'], DictDatainWikiPage['G_Coordinates_location_Lng_3']
    import pandas as pd

    data_columns = [
        'W_Pays',
        'W_Region',
        'W_Departement',
        'W_Arrondissement',
        'W_Canton',
        'W_Intercommunalite',
        'W_CodePostal',
        'W_CodeCommune',
        'W_Population',
        'W_Densite',
        'W_Cordommees',
        'W_Altitude',
        'W_Superficie',
        'W_Name_ru',
        'W_Name_uk',
        'W_Name_en',
        'W_Name_de',
        'W_Name_pl',
        'W_Name_es',
        'W_Name_pt',
        'W_Name_it',
        'W_Name_nl',
        'W_Name_da',
        'W_Name_no',
        'W_Name_sv',
        'W_Name_cs',
        'W_Name_ro',
        'W_Name_bg',
        'W_Name_hu',
        'W_Name_sk',
        'W_Name_sl',
        'W_Name_sh',
        'W_Name_hr',
        'W_Url_ru',
        'W_Url_uk',
        'W_Url_en',
        'W_Url_de',
        'W_Url_pl',
        'W_Url_es',
        'W_Url_pt',
        'W_Url_it',
        'W_Url_nl',
        'W_Url_da',
        'W_Url_no',
        'W_Url_sv',
        'W_Url_cs',
        'W_Url_ro',
        'W_Url_bg',
        'W_Url_hu',
        'W_Url_sk',
        'W_Url_sl',
        'W_Url_sh',
        'W_Url_hr',
        'G_Coordinates_northeast_Lat_1',
        'G_Coordinates_northeast_Lng_1',
        'G_Coordinates_southwest_Lat_2',
        'G_Coordinates_southwest_Lng_2',
        'G_Coordinates_location_Lat_3',
        'G_Coordinates_location_Lng_3',

        'G_Locality_long_name',
        'G_Locality_short_name',
        'G_Locality_types',
        'G_AdminLevel_1_long_name',
        'G_AdminLevel_1_short_name',
        'G_AdminLevel_1_types',
        'G_AdminLevel_2_long_name',
        'G_AdminLevel_2_short_name',
        'G_AdminLevel_2_types',
        'G_Country_long_name',
        'G_Country_short_name',
        'G_Country_types',
        'G_postal_code_long_name',
        'G_postal_code_short_name',
        'G_postal_code_types',
        'G_FormatAddress',
        'G_Types']

    MyList = []
    for i in data_columns:
        print i
        try:
            Data = str(DictDatainWikiPage[i])
            MyList.append(Data)
            print Data

        except KeyError:
            Data = None
            MyList.append(Data)

    print '\t'.join(data_columns)
    print len(MyList)
    print '\t'.join(str(n) for n in MyList)


    #NameCsv = os.path.abspath('../WorkBaseFile/14_07_17_4.csv')
    #pd.DataFrame(DictDatainWikiPage).T.reset_index().to_csv(NameCsv,  index=False,columns=data_columns,sep=b'\t')
