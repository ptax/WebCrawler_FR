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
import random


def get_google_map(address, Apikey):
    data_dict = {}
    json_result = WorkGoogleMap.GetDataInCommune.GetDataInAddress(address, Apikey)
    data_address = WorkGoogleMap.GetDataInCommune.StructureLocalType(json_result)
    data_coordinates = WorkGoogleMap.GetDataInCommune.GetCoordinatesInGoogle(json_result)
    data_dict.update(data_address)
    data_dict.update(data_coordinates)
    return data_dict


def main():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/08_09_17_not_in_locality')
    WorkDict = LoadMyDict.copy()
    c = 0
    listNoCode = []

    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        # time.sleep(1)

        try:
            G_Types = Data['G_Types']
        except KeyError:
            G_Types = None
            pass
        try:
            W_CodePostal = str(Data['W_CodePostal']).replace(',', '')
        except:
            W_CodePostal = 'None'
            pass
        try:
            InseeXls_NameCommune = Data['InseeXls_NameCommune']
        except:
            InseeXls_NameCommune = ''
        try:
            W_Region = Data['W_Region']
        except:
            W_Region = ''
        try:
            W_Departement = Data['W_Departement']
        except:
            W_Departement = ''
        #print Data['G_Types']
        if G_Types:


            #if str(W_CodePostal) != str(G_postal_code_short_name):
            c += 1

            # gen_address = str(W_CodePostal).strip() + ',' + str(Data['InseeXls_NameCommune']).strip() + ',' + 'France'
            gen_address = str(InseeXls_NameCommune).strip() + ',' + str(W_Region).strip() + ',' + str(
                W_Departement).strip() + ',' + 'France'
            gen_address = gen_address.replace(' ', '-')
            ApikeyList = ['AIzaSyBZVOSPh0Z4mv9jljJWzZNSug6upuec7Sg', 'AIzaSyAeaWLxSHFEdwWEVVYajslt7R9eP0ZpLXQ',
                          'AIzaSyARBYHwwK5uPoNuS2iN3UOg8fQGRgHLz78', 'AIzaSyDpkHWwId9J1mMCqu9mirXPEwpM3XTs0GU',
                          'AIzaSyAIAT5ptZVJqiFiTQZxAXp6KT8jREfKidU', 'AIzaSyDXBLyip9Go5V4COM2w-ELE-oV1Zm8EQRk',
                          'AIzaSyDBA9EWB_zNWC6XjDu9mGyIuuV6QSL_ABM', 'AIzaSyD_YqB4d_-xKcmNP9jJCiPkJYDS8J3f6pI',
                          'AIzaSyAAqEuv_SHtc0ByecPXSQiKH5f2p2t5oP4']
            ApiKey = random.choice(ApikeyList)
            Mydata = get_google_map(gen_address, ApiKey)
            WorkDict[Keys].update(Mydata)
            print c, Keys, gen_address, Mydata
        else:
            pass

    NameDict = '../WorkBaseFile/08_09_17_not_in_locality_Update'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, NameDict)
    print len(WorkDict)


if __name__ == '__main__':
    # address = '70360,La Neuvelle-lès-Scey,France'.replace(' ','-')
    #print address
    #print get_google_map(address)
    main()

    LoadDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/08_09_17_not_in_locality_Update')

    List_Rout = []
    for Data, Keys in zip(LoadDict.values(), LoadDict.keys()):
        try:
            G_Types = str(Data['G_Types'])
        except:
            G_Types = 'None'
            pass
        if u'locality' in str(G_Types):
            List_Rout.append(Keys)
    print 'locality', len(List_Rout)

    print len(List_Rout)