# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
from urllib2 import urlopen
import urllib
import json
import Utils.SaveAndLoadDictFile
import random
from GetDataInCommune import GetDataInAddress, StructureGoogleData


if __name__ == '__main__':
    '''
    CodeInsee = ''
    LocationName = 'Canton+de+Plonéour-Lanvern'

    ApikeyList = ['AIzaSyBZVOSPh0Z4mv9jljJWzZNSug6upuec7Sg', 'AIzaSyAeaWLxSHFEdwWEVVYajslt7R9eP0ZpLXQ',
                  'AIzaSyARBYHwwK5uPoNuS2iN3UOg8fQGRgHLz78', 'AIzaSyDpkHWwId9J1mMCqu9mirXPEwpM3XTs0GU',
                  'AIzaSyAIAT5ptZVJqiFiTQZxAXp6KT8jREfKidU', 'AIzaSyDXBLyip9Go5V4COM2w-ELE-oV1Zm8EQRk',
                  'AIzaSyDBA9EWB_zNWC6XjDu9mGyIuuV6QSL_ABM', 'AIzaSyD_YqB4d_-xKcmNP9jJCiPkJYDS8J3f6pI',
                  'AIzaSyAAqEuv_SHtc0ByecPXSQiKH5f2p2t5oP4']


    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Cantons_20_08_17_cards')
    work_dict = LoadMyDict.copy()
    c = 0
    for data in work_dict.values():
        c +=1

        code_canton = data['I_Code_canton']

        ApiKey = random.choice(ApikeyList)
        Wiki_Name_Snipet = str(data['Wiki_Name_Snipet'].strip().replace(' ','+')) + ',France'



        GoogleResult = GetDataInAddress(Wiki_Name_Snipet, ApiKey)
        dict_google = StructureGoogleData(GoogleResult)

        work_dict[code_canton].update(dict_google)

        print c,code_canton,(Wiki_Name_Snipet).strip(),str(len(dict_google)),str(dict_google).strip()

    NameDict = '../WorkBaseFile/Cantons_20_08_17_google'
    Utils.SaveAndLoadDictFile.SaveDict(work_dict,NameDict)
    '''

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Cantons_20_08_17_google')
    print len(LoadMyDict)
    test_dict = LoadMyDict['67 05']
    print test_dict
    print len(test_dict)
    print test_dict['I_Code_canton'], test_dict['Wiki_Url'], test_dict['W_Pays'], test_dict['G_FormatAddress'], \
    test_dict['G_Types']






