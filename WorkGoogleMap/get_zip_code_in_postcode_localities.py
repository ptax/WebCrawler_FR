# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import Utils.SaveAndLoadDictFile
import random

import WorkGoogleMap.GetDataInCommune


def up_not_equal_zip_code():
    listStat = []
    LoadDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/23_07_17_Up_Zip_Code')
    WorkDict = LoadDict.copy()
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            W_CodePostal = int(str(Data['W_CodePostal'].replace(',', '')))
        except:
            W_CodePostal = 'W_None'
        try:
            G_postal_code_short_name = int(Data['G_postal_code_short_name'])
        except:
            G_postal_code_short_name = 'G_None'
        try:
            G_Locality_short_name = Data['G_Locality_short_name']
        except:
            G_Locality_short_name = 'G_None_locality'

        if G_postal_code_short_name != W_CodePostal:
            listStat.append(Keys)

            if u'W_None' not in str(W_CodePostal):
                c += 1
                # print G_postal_code_short_name,W_CodePostal
                inquiry = str(W_CodePostal).replace(',', '') + ',' + u'France'
                '''
                ApikeyList = ['AIzaSyBZVOSPh0Z4mv9jljJWzZNSug6upuec7Sg','AIzaSyAeaWLxSHFEdwWEVVYajslt7R9eP0ZpLXQ','AIzaSyARBYHwwK5uPoNuS2iN3UOg8fQGRgHLz78','AIzaSyDpkHWwId9J1mMCqu9mirXPEwpM3XTs0GU','AIzaSyAIAT5ptZVJqiFiTQZxAXp6KT8jREfKidU','AIzaSyDXBLyip9Go5V4COM2w-ELE-oV1Zm8EQRk','AIzaSyDBA9EWB_zNWC6XjDu9mGyIuuV6QSL_ABM','AIzaSyD_YqB4d_-xKcmNP9jJCiPkJYDS8J3f6pI','AIzaSyAAqEuv_SHtc0ByecPXSQiKH5f2p2t5oP4']
                ApiKey = random.choice(ApikeyList)
                GoogleResult = WorkGoogleMap.GetDataInCommune.GetDataInAddress(inquiry,ApiKey)
                ListLocation =  WorkGoogleMap.GetDataInCommune.stucture_postcode_localities(GoogleResult)
                for Name in ListLocation:
                    if G_Locality_short_name in Name:
                        UpData = {'G_postal_code_long_name':str(W_CodePostal).replace(',',''),'G_postal_code_short_name':str(W_CodePostal).replace(',','')}
                        print c,Keys,W_CodePostal,Data['InseeXls_NameCommune'],G_Locality_short_name,Name
                        WorkDict[Keys].update(UpData)
                    else:
                        pass
                '''


            else:
                pass

        else:
            pass
    # name_dict = '../WorkBaseFile/23_07_17_Up_Zip_Code'
    #Utils.SaveAndLoadDictFile.SaveDict(WorkDict,name_dict)
    print len(listStat)


if __name__ == '__main__':
    up_not_equal_zip_code()