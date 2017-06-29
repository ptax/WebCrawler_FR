# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
from bs4 import BeautifulSoup
import urllib2
import urllib
wiki = "https://ru.wikipedia.org/wiki/%D0%9A%D0%BE%D0%BC%D0%BC%D1%83%D0%BD%D1%8B_%D0%B4%D0%B5%D0%BF%D0%B0%D1%80%D1%82%D0%B0%D0%BC%D0%B5%D0%BD%D1%82%D0%B0_%D0%9F%D0%B0-%D0%B4%D0%B5-%D0%9A%D0%B0%D0%BB%D0%B5"
header = {'User-Agent': 'Mozilla/5.0'} #Needed to prevent 403 error on Wikipedia
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)





CodeInsee = ""
CatonName = ""


table = soup.find("table", { "class" : "wikitable sortable" })
f = open('output_1.csv', 'w')
for row in table.findAll("tr"):
    cells = row.findAll("td")
    #For each "tr", assign each "td" to a variable.
    if len(cells) == 6:
        CodeInsee = cells[0].find(text=True)
        CatonName = cells[3].findAll(text=True)[0]
    for x in range(len(CodeInsee)):
        data = str(CodeInsee).strip() + "$" + str(CatonName).strip()
        f.write(str(data)+'\n')

f.close()