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


def open_wiki(url):
    header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(url, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    textarea = soup.findAll("textarea", {"class": "mw-editfont-default"})[0].text
    # LangHref  =  soup.findAll("textarea", { "class" : "mw-editfont-default" })
    return textarea


def get_canton(content):
    content = content.strip()
    content = content.split('\n')
    for i in content:
        # print i
        if u'canton' in i:
            canton = i.replace('| canton             = ', '').strip()
            list_canton = canton.split('|')
            for b in list_canton:
                mycanton = b.replace('[[', '').replace(']]', '')
            return mycanton

        else:
            pass


if __name__ == '__main__':


    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/27_07_17_Up_Moreration_commune')
    WorkDict = LoadMyDict.copy()
    print len(WorkDict)
    listErr = []
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        # print Data['Wiki_UrlInCommuneSnipet']
        #print Data['Wiki_UrlInCommune']
        c += 1
        try:

            W_Canton = Data['W_Canton']
        except:
            W_Canton = None

            if u'Intercommunalité' in str(W_Canton):
                try:
                    W_Url = Data['Wiki_UrlInCommune']
                except:
                    W_Url = None

                if W_Url == None:
                    try:
                        W_Url = Data['Wiki_UrlInCommuneSnipet']
                    except:
                        W_Url = None
                else:
                    W_Url = None

                wiki_url = W_Url.replace('/wiki/', '')
                url = 'https://fr.wikipedia.org/w/index.php?title=' + wiki_url + '&action=edit&section=0'.strip()

                content = open_wiki(url)
                change_name_canton = get_canton(content)

                print c, W_Canton, change_name_canton, url

                data_up = {'W_Canton': change_name_canton}

                WorkDict[Keys].update(data_up)

    name_dict = '../WorkBaseFile/27_07_17_Up_Moreration_commune_1'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


