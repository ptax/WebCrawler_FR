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


def dict_key_change():
    DictMyData = {
        u'G_Locality_long_name': '',
        u'G_Locality_short_name': '',
        u'G_Locality_types': '',
        u'G_AdminLevel_1_long_name': '',
        u'G_AdminLevel_1_short_name': '',
        u'G_AdminLevel_1_types': '',
        u'G_AdminLevel_2_long_name': '',
        u'G_AdminLevel_2_short_name': '',
        u'G_AdminLevel_2_types': '',
        u'G_Country_long_name': '',
        u'G_Country_short_name': '',
        u'G_Country_types': '',
        u'G_postal_code_long_name': '',
        u'G_postal_code_short_name': '',
        u'G_postal_code_types': ''
    }


if __name__ == '__main__':
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/03_07_17')
    WorkDict = LoadMyDict.copy()
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        pass




