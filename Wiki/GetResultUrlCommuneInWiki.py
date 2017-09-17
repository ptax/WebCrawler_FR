# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

import Utils.GetListInFile

from bs4 import BeautifulSoup
import urllib2


def Run(NameCommune,CodeCommune):
    CodeCommune = str(CodeCommune).strip()
    DictCommune = {'Wiki_UrlInCommune':None,
                   'Wiki_NameSnipet':None,
                   'Wiki_Old_UrlInCommune':None,
                   'Wiki_Old_NameSnipet':None,
                   'ColResultInSnipet':None
                   }
    wiki = "https://fr.wikipedia.org/w/index.php?search=%22Code+commune+"+ CodeCommune + "%22&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    SearchResult = soup.find("ul", { "class" : "mw-search-results" })
    ColResult =   str(SearchResult).replace('<ul class="mw-search-results">','').split('<li>')
    ColResult = [x for x in ColResult if x]
    ColResultLen = len(ColResult)
    for Result in ColResult:
        ResultObjet = BeautifulSoup(Result)
        ThemeCodeCommuneInSnipent = '<span class="searchmatch">' + str(CodeCommune) + '</span>'
        if ThemeCodeCommuneInSnipent in Result:
            Titel = ResultObjet.find("div", { "class" : "mw-search-result-heading" }).findAll("a")[0].text
            Url = ResultObjet.find("div", { "class" : "mw-search-result-heading" }).findAll("a")[0].get('href')
            if NameCommune in  Titel:
                DictCommune.update({'Wiki_UrlInCommune':Url,'Wiki_NameSnipet':Titel,'ColResultInSnipet':ColResultLen})
            else:
                DictCommune.update({'Wiki_Old_UrlInCommune':Url,'Wiki_Old_NameSnipet':Titel,'ColResultInSnipet':ColResultLen})
    return DictCommune




if __name__ == '__main__':
    NameComyne = u'Condette'
    CodeCommune = '62235'
    print Run(NameComyne,CodeCommune)
    #print GetUrlCommune(CodeCommune)
    #NameFile = r'../Wiki/BaseCommune'
    #print len((Utils.GetListInFile.Run(NameFile)))
    #DictInOpen = open('TestDict').read()
    #print DictInOpen