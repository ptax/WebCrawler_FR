# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
from bs4 import BeautifulSoup
import urllib2
import codecs
import re
import urllib
import collections
from collections import Counter
def GetHtml(Url):
    wiki = Url
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    tables = soup.findAll("table", { "class" : "infobox_v2" })[0]
    LangHref  =  soup.findAll("li", { "class" : "interlanguage-link" })
    return tables,LangHref


def WikiNameCommune(Table):
    WikiNameCommune = Table.find("td", { "class" : "entete map" }).text
    if WikiNameCommune:
         NameCommune = WikiNameCommune.strip()
    else:
        NameCommune = 'None'
    return NameCommune

def GetInformation(Table):
    DictInformationTable = {}
    DictDataInformation = {
                           1:(u'Pays',u'W_Pays'),
                           2:(u'Région',u'W_Region'),
                           3:(u'Département',u'W_Departement'),
                           4:(u'Arrondissement',u'W_Arrondissement'),
                           5:(u'Canton',u'W_Canton'),
                           6:(u'Intercommunalité',u'W_Intercommunalite'),
                           7:(u'Code postal',u'W_CodePostal'),
                           8:(u'Code commune',u'W_CodeCommune'),
                           9:(u'Population',u'W_Population'),
                           10:(u'Densité',u'W_Densite'),
                           11:(u'Coordonnées',u'W_Cordommees'),
                           12:(u'Altitude',u'W_Altitude'),
                           13:(u'Superficie',u'W_Superficie')
                        }
    DictDataInformation = collections.OrderedDict(sorted(DictDataInformation.items()))

    for Data in DictDataInformation.values():
        WikiNameInDict = Data[1]
        WikiName =  Data[0]
        for row in Table.findAll('tr'):
            if WikiName in row.text:
                #print row.text
                TableString = row.text.replace(WikiName,'').replace('municipale','').replace('\n',',').replace(',,','').replace('nord','').replace('est','').strip()
                DictInformationTable.update({WikiNameInDict:TableString})
    return DictInformationTable



def GetLanguages(LangHref):
    Languages = LangHref
    #print 'GET languages' + '\t' + str(len(Languages))
    ListLanguages = []
    for i in xrange(len(Languages)):
        Titel = Languages[i].findAll("a",)[0]['title'].split(u'— ')
        Link = urllib.unquote(Languages[i].findAll("a",)[0]['href'])
        HrefLang = Languages[i].findAll("a",)[0]['hreflang']

        Anchor = Languages[i].findAll("a",)[0].text
        LanguagesData = Link,HrefLang,Anchor,Titel[0]
        ListLanguages.append(LanguagesData)
    LangNameDict = {1:('ru','',''),2:('uk','',''),3:('en','',''),4:('de','',''),5:('pl','',''),6:('es','',''),7:('pt','',''),8:('it','',''),9:('nl','',''),10:('da','',''),11:('no','',''),12:('sv','',''),13:('cs','',''),14:('ro','',''),15:('bg','',''), 16:('hu','',''), 17:('sk','',''),18:('sl','',''),19:('sh','',''),20:('hr','','')}
    return ListLanguages



def FilterLanguages(ListLanguages):
    LangNameDict = {'ru':('ru','',''),'uk':('uk','',''),'en':('en','',''),'de':('de','',''),'pl':('pl','',''),'es':('es','',''),'pt':('pt','',''),'it':('it','',''),'nl':('nl','',''),'da':('da','',''),'no':('no','',''),'sv':('sv','',''),'cs':('cs','',''),'ro':('ro','',''),'bg':('bg','',''), 'hu':('hu','',''), 'sk':('sk','',''),'sl':('sl','',''),'sh':('sh','',''),'hr':('hr','','')}
    for Languages in ListLanguages:
        for DictKey,LangDictValue in LangNameDict.items():
            if LangDictValue[0] ==  Languages[1]:
                #UrlLang = re.sub('\(.*', '', Languages[0]).strip()
                UrlLang = Languages[0].strip()

                data = LangDictValue[0],Languages[3],UrlLang.decode('utf8')
                LangNameDict[DictKey] = data
            else:
                pass
    LangDictName = {
                    'W_Name_ru':'ru',
                    'W_Name_uk':'uk',
                    'W_Name_en':'en',
                    'W_Name_de':'de',
                    'W_Name_pl':'pl',
                    'W_Name_es':'es',
                    'W_Name_pt':'pt',
                    'W_Name_it':'it',
                    'W_Name_nl':'nl',
                    'W_Name_da':'da',
                    'W_Name_no':'no',
                    'W_Name_sv':'sv',
                    'W_Name_cs':'cs',
                    'W_Name_ro':'ro',
                    'W_Name_bg':'bg',
                    'W_Name_hu':'hu',
                    'W_Name_sk':'sk',
                    'W_Name_sl':'sl',
                    'W_Name_sh':'sh',
                    'W_Name_hr':'hr'
                    }
    LangDictUrl = {
                    'W_Url_ru':'ru',
                    'W_Url_uk':'uk',
                    'W_Url_en':'en',
                    'W_Url_de':'de',
                    'W_Url_pl':'pl',
                    'W_Url_es':'es',
                    'W_Url_pt':'pt',
                    'W_Url_it':'it',
                    'W_Url_nl':'nl',
                    'W_Url_da':'da',
                    'W_Url_no':'no',
                    'W_Url_sv':'sv',
                    'W_Url_cs':'cs',
                    'W_Url_ro':'ro',
                    'W_Url_bg':'bg',
                    'W_Url_hu':'hu',
                    'W_Url_sk':'sk',
                    'W_Url_sl':'sl',
                    'W_Url_sh':'sh',
                    'W_Url_hr':'hr'
                    }
    for LangName in LangDictName.items():
        DataName = LangName[0]
        WikiName = LangName[1]
        Data = {DataName:(LangNameDict[WikiName][1]).strip()}
        LangDictName.update(Data)
    for LangUrl in LangDictUrl.items():
        DataName = LangUrl[0]
        WikiUrl= LangUrl[1]
        url=urllib.unquote(LangNameDict[WikiUrl][2]).decode('utf8').strip()
        Data = {DataName:url}
        LangDictUrl.update(Data)


    MyLangDict = LangDictUrl.copy()
    MyLangDict.update(LangDictName)
    return MyLangDict




if __name__ == '__main__':

    Url = "https://fr.wikipedia.org/wiki/Arras"
    GetHtml = GetHtml(Url)
    Table = GetHtml[0]
    LangHref = GetHtml[1]
    #print LangHref

    DictTableInformation = GetInformation(Table)
    LanguagesDict = FilterLanguages(GetLanguages(LangHref))

    DictDatainWikiPage = DictTableInformation.copy()
    DictDatainWikiPage.update(LanguagesDict)


    #print DictDatainWikiPage['W_Url_sl'],DictDatainWikiPage['W_Name_sl'],DictDatainWikiPage['W_Pays'],DictDatainWikiPage['W_Departement']



    '''
    Table = GetTable(Url)
    #WikiNameCommune(Table)
    DictTableInformation = GetInformation(Table)
    #print DictTableInformation[u'Coordonnées'][u'Coordonnées']
    print DictTableInformation
    for i in  DictTableInformation.values():
        print i.items(),i.values()

    '''