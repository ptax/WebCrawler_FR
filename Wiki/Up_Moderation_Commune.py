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
    NameFile = r'../WorkBaseFile/Up_Date_Coomune_2'

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
    name_dict = '../WorkBaseFile/27_07_17_UP_Moderation_Data_2'
    Utils.SaveAndLoadDictFile.SaveDict(MyDict, name_dict)


def up_wiki():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_UP_Moderation_Data_2')
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

    name_dict = '../WorkBaseFile/27_07_17_UP_Moderation_Data_2_1'
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
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/23_07_17_UP_Moderation_Data_5')
    WorkDict = LoadMyDict.copy()
    # del WorkDict['97801']
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        W_CodePostal = Data['W_CodePostal']
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
    name_dict = '../WorkBaseFile/27_07_17_UP_Moderation_Data_2_3'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def up_google_coordinates():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/23_07_17_UP_Moderation_Data_5')
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
    name_dict = '../WorkBaseFile/27_07_17_UP_Moderation_Data_2_3'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def up_data():
    MyBase = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/24_07_17_UP')

    WorkDict = MyBase.copy()
    print 'All Base', len(WorkDict)
    UpDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_UP_Moderation_Data_2_4')
    NewDict = {}
    for Data, Keys in zip(UpDict.values(), UpDict.keys()):
        try:
            WorkDict[Keys].update(Data)
        except:
            print Keys
            WorkDict[Keys] = Data
    name_dict = '../WorkBaseFile/27_07_17_Up_Moreration_commune'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


if __name__ == '__main__':
    # gen_dict_in_file()
    #up_wiki()
    #up_w_code_coommune()
    #up_hand()
    #up_google_data_in_post_code()

    #up_google_coordinates()
    up_data()

    #gen_dict_in_file()
    #up_wiki()
    #up_w_code_coommune()
    #up_google_data_in_post_code()

    #up_google_coordinates()

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_Up_Moreration_commune')
    print 'New Base', len(LoadMyDict)

    print LoadMyDict['97603']
    print LoadMyDict['15268']

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
