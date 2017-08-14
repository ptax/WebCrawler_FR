# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

import GetUrlCommuneInWiki
import Utils.GetListInFile
import Utils.SaveAndLoadDictFile
import DataStructure.InseeFr_Commune

import Wiki.GetDataInWikiTable
import time
import Utils.ConvertCordinates

import os

import urllib2
import WorkGoogleMap.GetDataInCommune
import random


def gen_dict_in_file():
    NameFile = r'../WorkBaseFile/Up_Date_Coomune_3'

    MyDict = {}
    for i in Utils.GetListInFile.Run(NameFile):
        i = i.split('\t')
        InseeXls_CodeCommune = i[0]
        InseeXls_NameCommune = i[1]
        InseeXls_Population = i[2]
        Wiki_UrlInCommune = i[3]
        MyDict[InseeXls_CodeCommune] = {'InseeXls_CodeCommune': InseeXls_CodeCommune,
                                        'InseeXls_NameCommune': InseeXls_NameCommune,
                                        'InseeXls_Population': InseeXls_Population.strip(),
                                        'Wiki_UrlInCommune': Wiki_UrlInCommune}
    name_dict = '../WorkBaseFile/01_08_17_UpdateCommune'
    Utils.SaveAndLoadDictFile.SaveDict(MyDict, name_dict)


def up_wiki():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_UpdateCommune')
    WorkDict = LoadMyDict.copy()

    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            Url = 'https://fr.wikipedia.org' + str(Data['Wiki_UrlInCommune'])

            GetHtml = Wiki.GetDataInWikiTable.GetHtml(Url)
            Table = GetHtml[0]

            DataDict = {}
            LangHref = GetHtml[1]
            DictTableInformation = Wiki.GetDataInWikiTable.GetInformation(Table)
            LanguagesDict = Wiki.GetDataInWikiTable.FilterLanguages(Wiki.GetDataInWikiTable.GetLanguages(LangHref))

            print Keys, Url

            WorkDict[Keys].update(DictTableInformation)
            WorkDict[Keys].update(LanguagesDict)
        except:
            pass

    name_dict = '../WorkBaseFile/01_08_17_UpdateCommune_1'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def up_w_code_coommune():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_UP_Moderation_Data_2_1')
    WorkDict = LoadMyDict.copy()

    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            Data['W_CodeCommune']
        except KeyError:
            c += 1

            if u'arrondissement' in Data['Wiki_UrlInCommune']:
                print Data['Wiki_UrlInCommune']
                data = {'W_CodeCommune': Data['InseeXls_CodeCommune']}
                WorkDict[Keys].update(data)

    name_dict = '../WorkBaseFile/27_07_17_UP_Moderation_Data_2_2'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)

    print len(LoadMyDict)


def up_hand():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/23_07_17_UP_Moderation_Data_5')
    WorkDict = LoadMyDict.copy()
    data = {'W_CodePostal': '97133', 'W_CodeCommune': '97701', 'W_Cordommees': '17° 55′ 0″ N, 62° 52′ 0″ W'}

    WorkDict['97701'].update(data)
    name_dict = '../WorkBaseFile/23_07_17_UP_Moderation_Data_6'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def get_google_map(address, Apikey):
    data_dict = {}
    json_result = WorkGoogleMap.GetDataInCommune.GetDataInAddress(address, Apikey)
    data_address = WorkGoogleMap.GetDataInCommune.StructureLocalType(json_result)
    data_coordinates = WorkGoogleMap.GetDataInCommune.GetCoordinatesInGoogle(json_result)
    data_dict.update(data_address)
    data_dict.update(data_coordinates)
    return data_dict


def up_google_data_in_post_code():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_inseeName_not_egual_google_name')
    WorkDict = LoadMyDict.copy()
    # del WorkDict['97801']
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            W_CodePostal = Data['W_CodePostal']
        except:
            W_CodePostal = 'None'
        gen_address = str(W_CodePostal).strip().replace(',', '') + ',' + str(
            Data['InseeXls_NameCommune']).strip() + ',' + 'France'
        gen_address = gen_address.replace(' ', '-')
        ApikeyList = ['AIzaSyBZVOSPh0Z4mv9jljJWzZNSug6upuec7Sg', 'AIzaSyAeaWLxSHFEdwWEVVYajslt7R9eP0ZpLXQ',
                      'AIzaSyARBYHwwK5uPoNuS2iN3UOg8fQGRgHLz78', 'AIzaSyDpkHWwId9J1mMCqu9mirXPEwpM3XTs0GU',
                      'AIzaSyAIAT5ptZVJqiFiTQZxAXp6KT8jREfKidU', 'AIzaSyDXBLyip9Go5V4COM2w-ELE-oV1Zm8EQRk',
                      'AIzaSyDBA9EWB_zNWC6XjDu9mGyIuuV6QSL_ABM', 'AIzaSyD_YqB4d_-xKcmNP9jJCiPkJYDS8J3f6pI',
                      'AIzaSyAAqEuv_SHtc0ByecPXSQiKH5f2p2t5oP4']
        ApiKey = random.choice(ApikeyList)
        Mydata = get_google_map(gen_address, ApiKey)
        print Keys, Mydata['G_Country_long_name'], gen_address, Mydata
        WorkDict[Keys].update(Mydata)
    name_dict = '../WorkBaseFile/01_08_17_inseeName_not_egual_google_name_UP'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def up_google_coordinates():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_inseeName_not_egual_google_name_UP')
    WorkDict = LoadMyDict.copy()
    list_erro = []
    for Data, Keys in zip(LoadMyDict.values(), LoadMyDict.keys()):
        try:
            if Data['G_Coordinates_southwest_Lat_2'] == 'None':
                list_erro.append(Keys)
        except:
            list_erro.append(Keys)
    for i in list_erro:
        # print WorkDict[i]['W_Cordommees']
        Cordinates = str(WorkDict[i]['W_Cordommees']).replace('ou,', 'S').split(',')
        Cordinate = str(Utils.ConvertCordinates.dms2dec(Cordinates[0])) + ',' + str(
            Utils.ConvertCordinates.dms2dec(Cordinates[1]))
        Cordinates = Cordinate.split(',')
        Cordinat_1 = Cordinates[0]
        Cordinat_2 = Cordinates[1]
        print Cordinat_1, Cordinat_2
        result = WorkGoogleMap.GetDataInCommune.GetDataInCordinates(Cordinat_1, Cordinat_2)
        GoogleDataCorrdinat = WorkGoogleMap.GetDataInCommune.GetCoordinatesInGoogle(result)

        #print GoogleDataCorrdinat
        WorkDict[i].update(GoogleDataCorrdinat)
    name_dict = '../WorkBaseFile/01_08_17_inseeName_not_egual_google_name_UP_coodinates'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def up_google_coordinates_southwest():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_G_Coordinates_northeast_Lat_1')
    WorkDict = LoadMyDict.copy()
    list_erro = []
    for Data, Keys in zip(LoadMyDict.values(), LoadMyDict.keys()):
        # print WorkDict[i]['W_Cordommees']
        Cordinates = str(Data['W_Cordommees']).replace('ou,', 'S').split(',')
        Cordinate = str(Utils.ConvertCordinates.dms2dec(Cordinates[0])) + ',' + str(
            Utils.ConvertCordinates.dms2dec(Cordinates[1]))
        Cordinates = Cordinate.split(',')
        Cordinat_1 = Cordinates[0]
        Cordinat_2 = Cordinates[1]

        # Cordinat_1 = str(Data['G_Coordinates_location_Lat_3'])
        #Cordinat_2 = str(Data['G_Coordinates_location_Lng_3'])

        print Cordinat_1, Cordinat_2
        result = WorkGoogleMap.GetDataInCommune.GetDataInCordinates(Cordinat_1, Cordinat_2)
        GoogleDataCorrdinat = WorkGoogleMap.GetDataInCommune.GetCoordinatesInGoogle(result)
        MyDict = {'G_Coordinates_northeast_Lat_1': GoogleDataCorrdinat['G_Coordinates_northeast_Lat_1'],
                  'G_Coordinates_northeast_Lng_1': GoogleDataCorrdinat['G_Coordinates_northeast_Lng_1'],
                  'G_Coordinates_southwest_Lat_2': GoogleDataCorrdinat['G_Coordinates_southwest_Lat_2'],
                  'G_Coordinates_southwest_Lng_2': GoogleDataCorrdinat['G_Coordinates_southwest_Lng_2']
                  }

        #print GoogleDataCorrdinat
        WorkDict[Keys].update(MyDict)
    name_dict = '../WorkBaseFile/02_08_17_G_Coordinates_northeast_Lat_UpDate'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def up_data():
    MyBase = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release')

    WorkDict = MyBase.copy()
    print 'All Base', len(WorkDict)
    UpDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_UpdateCommune_7')
    NewDict = {}
    for Data, Keys in zip(UpDict.values(), UpDict.keys()):
        try:
            WorkDict[Keys].update(Data)
        except:
            print Keys
            WorkDict[Keys] = Data
    name_dict = '../WorkBaseFile/02_08_17_release_2'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def change_wiki_url():
    MyBase = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release_2')
    WorkDict = MyBase.copy()
    for Data, Keys in zip(MyBase.values(), MyBase.keys()):

        try:
            Wiki_UrlInCommune = Data['Wiki_UrlInCommune']
        except:
            Wiki_UrlInCommune = None

        if Wiki_UrlInCommune:

            print Keys, Wiki_UrlInCommune
            Mydata = {'Wiki_Url': Wiki_UrlInCommune}
            WorkDict[Keys].update(Mydata)
        else:
            pass

    name_dict = '../WorkBaseFile/02_08_17_release_3'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


if __name__ == '__main__':

    #up_wiki()





    #up_google_data_in_post_code()

    #up_google_coordinates()
    #up_data()

    #gen_dict_in_file()
    #up_wiki()
    #up_w_code_coommune()
    #up_google_data_in_post_code()

    #up_google_coordinates()

    # up_google_data_in_post_code()
    #up_google_coordinates()
    #up_google_coordinates_southwest()
    #up_data()

    change_wiki_url()


    # up_data()

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release_3')
    print 'New Base', len(LoadMyDict)
    print LoadMyDict['08311']['Wiki_UrlInCommune'], LoadMyDict['08311']['W_Canton'], LoadMyDict['08311']['Wiki_Url']
    print LoadMyDict['97612']['Wiki_UrlInCommune'], LoadMyDict['97612']['W_Canton'], LoadMyDict['97612']['Wiki_Url']

    #for Data,Keys in zip(LoadMyDict.values(),LoadMyDict.keys()):
    #print Keys,Data
    '''
    list_none = []
    for Data,Keys in zip(LoadMyDict.values(),LoadMyDict.keys()):
        G_Cord = Data['G_Coordinates_northeast_Lat_1']
        print Keys,Data['G_Types'],G_Cord
        if str(G_Cord) == 'None':
            list_none.append(Keys)
        else:pass
    print len(list_none)
    for i in list_none:
        print i
    '''
    '''

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_UP_Moderation_Data_2_3')
    print len(LoadMyDict)
    print LoadMyDict['97604']

    for Data,Keys in zip(LoadMyDict.values(),LoadMyDict.keys()):
        print Keys,Data['W_Region']


    MyBase = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/23_07_17_Del_Change_Commune')
    UpDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/23_07_17_Up_Moreration_commune')
    print MyBase['30339']
    print UpDict['30339']




        try:
            if Data['G_Coordinates_southwest_Lat_2'] == 'None':
                c+=1
                print c,Keys
        except:
              print 'err',c,Keys



    print len(LoadMyDict)
    '''
