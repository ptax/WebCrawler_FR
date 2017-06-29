# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import urllib2
import urllib
wiki = "https://de.wikipedia.org/wiki/Arrondissement_Montreuil"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)


CodeInsee = ""
CantonName = ""
ColumTree = ""
ColumFor = ''

#table = soup.find("table", attrs={ "class" : "prettytable" })
table = soup.find('body').findAll('table')
table = table[1]
#f = open('Lang_DE.txt', 'w')
ListLang = []
for row in table.findAll("tr"):
    cells = row.findAll("td")

    #For each "tr", assign each "td" to a variable.
    if len(cells) == 4:
        for i in xrange(4):
            try:
                CantonName =  cells[i].findAll("a",)[0](text=True)[0]
                CodeInsee = cells[i].findAll("small",)[0](text=True)[0].replace('(','').replace(')','')
                data = str(CodeInsee).strip() + "$" + str(CantonName).strip()
                ListLang.append(data)
            except:pass
print len(ListLang)
for i in ListLang:
    print i
        #f.write(str(data)+'\n')

#f.close()
