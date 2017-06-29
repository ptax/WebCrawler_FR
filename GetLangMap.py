# -*- coding: utf-8 -*-

from urllib2 import urlopen
import csv
import json
from time import sleep

def GetList(FileName):
    ListMyData = []
    OpenDictFile = open(FileName).read().split('\n')
    for i in OpenDictFile:
        ListMyData.append(i.split('$'))
    return ListMyData


def GetLangName(Cordinates_1,Cordinates_2,Lang):

    url = "https://maps.googleapis.com/maps/api/geocode/json?latlng=" + Cordinates_1 + "," + Cordinates_2 + "&sensor=false&language=" + Lang + '&key=AIzaSyAyuipQcvRBCoJDNBvt4b0jDmd7NECfOmg'
    response = json.loads(urlopen(url).read())
    if response["status"] == u"OK":
        listLang = []
        results = response.get("results")[1]
        for i in results['address_components']:
            if i['types'][0] == u'locality':
                return unicode(i['long_name'])






FileName = r'base/11_05_17.txt'
FileList = GetList(FileName)

f = open('Lang_De_Google.txt', 'w')
for i in FileList:
    #sleep(5)
    CodeInsee = i[2]
    Coordinates_1 = str(i[17])
    Coordinates_2 = str(i[18])
    Lang = u'de'
    LangName = GetLangName(Coordinates_1,Coordinates_2,Lang)
    data = str(CodeInsee).strip() + "$" + str(LangName.encode('utf-8')).strip()
    print data
    f.write(str(data)+'\n')

f.close()

