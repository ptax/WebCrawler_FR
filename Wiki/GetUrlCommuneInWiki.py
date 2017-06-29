# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os

import Utils.GetListInFile

from bs4 import BeautifulSoup
import urllib2


def Run(CodeCommune):
    '''
        This is function  which local search in wiki FR
        You give Code Insee in FR location commune
        You get in wiki url, in which full desctiption commune
    '''
    wiki = "https://fr.wikipedia.org/w/index.php?search=%22Code+commune+"+ CodeCommune + "%22&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    SearchResult = soup.find("ul", { "class" : "mw-search-results" })
    if SearchResult:
        SearchSnippet = SearchResult.find("div", { "class" : "searchresult" }).findAll("span", { "class" : "searchmatch" })[2]
        if CodeCommune in SearchSnippet:
            Url = SearchResult.find("div", { "class" : "mw-search-result-heading" }).findAll("a")[0].get('href')
        else:
            Url = 'Not Faund'
        return Url
    else:
        Url = 'Not Faund'
        return Url

if __name__ == '__main__':
    CodeCommune = '01039'
    #print GetUrlCommune(CodeCommune)
    NameFile = r'../Wiki/BaseCommune'
    #print len((Utils.GetListInFile.Run(NameFile)))
    DictInOpen = open('TestDict').read()
    print DictInOpen