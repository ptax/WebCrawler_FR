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
import Utils.ClearName


def open_wiki(url):
    header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    textarea = soup.findAll("textarea", {"class": "mw-editfont-default"})[0].text
    # LangHref  =  soup.findAll("textarea", { "class" : "mw-editfont-default" })
    return textarea


def get_region(content):
    content = content.strip()
    content = content.split('\n')
    for i in content:
        # print i
        if u'région' in i:
            canton = i.replace('région', '').replace('=', '').replace('               ', '').strip()
            list_canton = canton.split('|')
            for b in list_canton:
                mycanton = b.replace('[[', '').replace(']]', '')
            return mycanton.strip()

        else:
            pass


if __name__ == '__main__':

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_Up_Moreration_commune_1')
    WorkDict = LoadMyDict.copy()
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            W_Region = Data['W_Region']
        except:
            W_Region = None
        if u'Intercommunalité' in str(W_Region):
            print W_Region
            try:
                W_Url = Data['Wiki_UrlInCommune']
            except:
                W_Url = None

            wiki_url = W_Url.replace('/wiki/', '')

            url = 'https://fr.wikipedia.org/w/index.php?title=' + wiki_url + '&action=edit&section=0'.strip()
            content = open_wiki(url)
            New_Region = get_region(content)
            c += 1
            W_RegionUP = {'W_Region': New_Region}
            WorkDict[Keys].update(W_RegionUP)

            print c, Keys, W_Region, 'New_region \t', New_Region
        else:
            pass
    name_dict = '../WorkBaseFile/27_07_17_Up_Moreration_commune_2'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)




