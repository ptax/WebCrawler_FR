# -*- coding: utf-8 -*-

import sys
reload(sys)
sys.setdefaultencoding('utf-8')


ListMyNameObjet = open(r'Lack_Onli_Name').read().split('\n')
ListMyNameObjet = [x for x in ListMyNameObjet if x]

ListWikiFile = open(r'LackNameWiki').read().split('\n')

ListWikiFile = [x for x in ListWikiFile if x]


print 'WikiList \t'  + str(len(ListWikiFile))


print 'GoogleList \t'  + str(len(ListMyNameObjet))

CoincidenceList = []
for GoogleName in ListMyNameObjet:
    for WikiName in ListWikiFile:
        if GoogleName.strip() in WikiName.strip():
            CoincidenceList.append(GoogleName)

print len(CoincidenceList)


NotList = []
MyNameObjet = open(r'Lack_Onli_Name').read()

DictWiki = {}
for WikiName in ListWikiFile:
    DictWiki[WikiName.strip()] = {'WikiName':WikiName}


DictNameInGoogleWiki = {}
for WikiName in ListWikiFile:
    for GoogleName in ListMyNameObjet:
        if WikiName.strip() in GoogleName.strip():
            DictNameInGoogleWiki[WikiName.strip()] = {'WikiName':WikiName}

print len(DictWiki)
print len(DictNameInGoogleWiki)

for i in DictNameInGoogleWiki.keys():
    try:
        del DictWiki[i]
    except:
        pass

for i in DictWiki.values():
    print i['WikiName']