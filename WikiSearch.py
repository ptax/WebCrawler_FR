# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from bs4 import BeautifulSoup
import urllib2


def GetList(FileName):
    ListMyData = []
    OpenDictFile = open(FileName).read().split('\n')
    for i in OpenDictFile:
        ListMyData.append(i.split('$'))
    return ListMyData

def GetSearchResult(CodeCommune):
    wiki = "https://fr.wikipedia.org/w/index.php?search=%22Code+commune+"+ CodeCommune + "%22&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    SearchResult = soup.find("ul", { "class" : "mw-search-results" })
    return SearchResult


FileName = r'Lang_FR.txt'
for i in GetList(FileName):
    NameComuneFile = str(i[1]).strip()
    CodeCommune = str(i[0]).strip()
    SearchResult = GetSearchResult(CodeCommune)
    Sarchsnippet = SearchResult.find("div", { "class" : "searchresult" }).findAll("span", { "class" : "searchmatch" })[2]
    if CodeCommune in Sarchsnippet:
        Mylink = SearchResult.find("div", { "class" : "mw-search-result-heading" }).findAll("a")[0]
        Url = Mylink.get('href')
        Titel = Mylink.get('title')
        Titel = Titel.replace('(Pas-de-Calais)','').strip()

        if Titel == NameComuneFile:
            data =  CodeCommune + '$' + Url + '$' + Titel + '$' + NameComuneFile
            print data

        else:
            MyError = 'Error'
            data =  CodeCommune + '$' + Url + '$' + Titel + '$' + NameComuneFile + '$' + MyError
            print data




    else:
        print 'Not FaundCodeCummune'

