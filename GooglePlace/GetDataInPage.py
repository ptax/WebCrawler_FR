# -*- coding: utf-8 -*-

import urllib2
import re
import urllib

from bs4 import BeautifulSoup


def GetCoordinates():
    coordinates = soup.findAll("span", { "class" : "h-geo geo-dms" })
    latitude =  coordinates[0].findAll("data", { "class" : "p-latitude" })
    longitude =  coordinates[0].findAll("data", { "class" : "p-longitude" })
    return latitude[0]['value'],longitude[0]['value']

def getLanguages():
    Languages = soup.findAll("li", { "class" : "interlanguage-link" })
    #print 'GET languages' + '\t' + str(len(Languages))
    ListLanguages = []
    for i in xrange(len(Languages)):
        '''Tut razdelitel   '''
        Titel = Languages[i].findAll("a",)[0]['title'].split(u'— ')
        Link = urllib.unquote(Languages[i].findAll("a",)[0]['href'])
        HrefLang = Languages[i].findAll("a",)[0]['hreflang']
        Anchor = Languages[i].findAll("a",)[0].text
        LanguagesData = Link,HrefLang,Anchor,Titel[0]
        ListLanguages.append(LanguagesData)
    return ListLanguages



def FilterLanguages(ListLanguages):
    #LangNameDict = {1:('ru',''),2:('uk',''),3:('en',''),4:('de',''),5:('pl',''),6:('es',''),7:('pt',''),8:('it',''),9:('nl',''),10:('da',''),11:('no',''),12:('sv',''),13:('cs',''),14:('ro',''),15:('bg',''),16:('hu',''),17:('sk',''),18:('sl',''),19:('sh',''),20:('hr','')}
    LangNameDict = {1:('ru','',''),2:('uk','',''),3:('en','',''),4:('de','',''),5:('pl','',''),6:('es','',''),7:('pt','',''),8:('it','',''),9:('nl','',''),10:('da','',''),11:('no','',''),12:('sv','',''),13:('cs','',''),14:('ro','',''),15:('bg','',''), 16:('hu','',''), 17:('sk','',''),18:('sl','',''),19:('sh','',''),20:('hr','','')}
    for Languages in ListLanguages:
        for DictKey,LangDictValue in LangNameDict.items():
            if LangDictValue[0] ==  Languages[1]:
                UrlLang = re.sub('\(.*', '', Languages[0]).strip()

                #print LangDictValue[0]
                data = LangDictValue[0],Languages[3],UrlLang.decode('utf8')
                LangNameDict[DictKey] = data
            else:
                pass
    ListNameDict = []
    for DictKey,LangDictValue in LangNameDict.items():
        data = LangDictValue[1],LangDictValue[2]
        data =  '$'.join(data)
        ListNameDict.append(data)


    return '$'.join(ListNameDict)

def GetPopulation():
    tables = soup.findAll("table", { "class" : "infobox_v2" })
    for tn in range(len(tables)):
        table=tables[tn]
        GetTh=table.findAll("tr")
        for NumTH in xrange(len(GetTh)):
            if 'Population' in GetTh[NumTH].text:
                Population = GetTh[NumTH].text.replace('Population','').replace('municipale','').strip()
                return Population
            else:
                pass






def GetCodeCommune():
    tables = soup.findAll("table", { "class" : "infobox_v2" })
    for tn in range(len(tables)):
        table=tables[tn]
        #GetTh=table.findAll("th")
        GetTh=table.findAll("tr")
        for NumTH in xrange(len(GetTh)):
            if 'Code commune' in GetTh[NumTH].text:
                CodeCommune = GetTh[NumTH].text.replace('Code commune','').strip()

                return CodeCommune
            else:
                pass


from GooglePlace import ProcessingTable

FileName = r'base/output_Liste_des_communes_du_Pas-de-Calais_t0.csv'
DictTable = ProcessingTable.ProcessingTable(FileName)

print len(DictTable)
FirstColum ='UrlCommune,NameCommune,CodeInseeTable,CodePostal,ArrondissementUrl,ArrondissementName,CantonUrl,CantonName,IntercommunaliteUrl,IntercommunaliteName,Superficie,PopulationTable,Densite,Maire,AltitudeMini,AltitudeMax,CodeCommunePage,Coordinates_1,Coordinates_2,PopulationPage,RuName,RuUrl,UkName,UkUrl,EnName,EnUrl,DeName,DeUrl,PlName,PlUrl,EsName,EsUrl,PtName,PtUrl,ItName,ItUrl,NlName,NlUrl,DaName,DaUrl,NoName,NoUrl,SvName,SvUrl,CsName,CsUrl,RoName,RoUrl,BgName,BgUrl,HuName,HuUrl,SkName,SkUrl,SlName,SlUrl,ShName,ShUrl,HrName,HrUrl,CodeInseTableVSCodeIncePage'
for NumDict in xrange(len(DictTable)):

    '''Data in File Table'''
    UrlCommune = DictTable.get(NumDict).get('UrlCommune').strip().decode('utf8')
    NameCommune = DictTable.get(NumDict).get('NameCommune').strip().decode('utf8')
    CodeInseeTable = DictTable.get(NumDict).get('CodeInsee').strip().decode('utf8')
    CodePostal = DictTable.get(NumDict).get('CodePostal').strip().decode('utf8')
    ArrondissementUrl = DictTable.get(NumDict).get('ArrondissementUrl').strip().decode('utf8')
    ArrondissementName = DictTable.get(NumDict).get('ArrondissementName').strip().decode('utf8')
    CantonUrl = DictTable.get(NumDict).get('CantonUrl').strip().decode('utf8')
    CantonName = DictTable.get(NumDict).get('CantonName').strip().decode('utf8')
    IntercommunaliteUrl = DictTable.get(NumDict).get('IntercommunaliteUrl').strip().decode('utf8')
    IntercommunaliteName = DictTable.get(NumDict).get('IntercommunaliteName').strip().decode('utf8')
    Superficie = DictTable.get(NumDict).get('Superficie').strip().decode('utf8')
    PopulationTable = DictTable.get(NumDict).get('Population').strip().decode('utf8')
    Densite = DictTable.get(NumDict).get('Densite').strip().decode('utf8')
    Maire = DictTable.get(NumDict).get('Maire').strip().decode('utf8')
    AltitudeMini = DictTable.get(NumDict).get('AltitudeMini').strip().decode('utf8')
    AltitudeMax = DictTable.get(NumDict).get('AltitudeMax').strip().decode('utf8')



    wiki = "https://fr.wikipedia.org" + str(UrlCommune)
    header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki,headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)

    '''Data in Page Wiki'''
    CodeCommunePage = GetCodeCommune().replace("'",'')
    Coordinates= GetCoordinates()
    Coordinates_1 = Coordinates[0]
    Coordinates_2 = Coordinates[1]
    PopulationPage = GetPopulation().strip()

    Languages = FilterLanguages(getLanguages()).strip()



    if CodeInseeTable != CodeCommunePage:
        CodeInseTableVSCodeIncePage = 'Error'
    else:
        CodeInseTableVSCodeIncePage = ''
    data = UrlCommune + '$', \
           NameCommune + '$', \
           CodeInseeTable + '$', \
           CodePostal + '$', \
           ArrondissementUrl + '$', \
           ArrondissementName + '$', \
           CantonUrl + '$', \
           CantonName + '$', \
           IntercommunaliteUrl + '$', \
           IntercommunaliteName + '$', \
           Superficie + '$', \
           PopulationTable + '$', \
           Densite + '$', \
           Maire + '$', \
           AltitudeMini + '$', \
           AltitudeMax + '$', \
           CodeCommunePage + '$', \
           Coordinates_1 + '$', \
           Coordinates_2 + '$', \
           PopulationPage + '$', \
           Languages + '$', \
           CodeInseTableVSCodeIncePage







    #data = str(wiki)+ ',' ,MyError+ ',' ,CodeCommune +',' ,CodeCommuneinFile  +',' ,Coordinates[0]+',',Coordinates[1]+',', Population+',',Languages
    data = u''.join(data).encode('utf-8').strip()

    print data


    text_file = open("base/PageWiki.txt", "a")
    text_file.write(data +'\n')
text_file.close()

'''
wiki = "https://fr.wikipedia.org/wiki/B%C3%A9thune"
#wiki = "https://fr.wikipedia.org/wiki/Bailleulmont"

header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)

CodeCommune = GetCodeCommune()
Population = GetPopulation().strip()
Coordinates= GetCoordinates()
Languages = FilterLanguages(getLanguages()).strip()
print Population

data = CodeCommune +',' ,Coordinates[0].replace('.',',')+',',Coordinates[1].replace('.',',')+',', Population+',',Languages
data = u''.join(data).encode('utf-8').strip()
'''
'''
Code commune	latitude	longitude	Population municipale	ru	uk	en	de	pl	es	pt	it	nl	da	no	sv	cs	ro	bg	hu	sk	sh	hr
'''