# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import Utils.SaveAndLoadDictFile
from bs4 import BeautifulSoup
import urllib2
import urllib


def Run(NameCommune, CodeCommune):
    listerr = []
    DictCommune = {}
    wiki = 'https://fr.wikipedia.org/w/index.php?search="Code+ISO+3166-2+FR-{0}"'.format(
        CodeCommune.replace(' ', '+').strip())
    header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    SearchResult = soup.find("ul", {"class": "mw-search-results"})
    ColResult = str(SearchResult).replace('<ul class="mw-search-results">', '').split('<li>')
    ColResult = [x for x in ColResult if x]
    ColResultLen = len(ColResult)

    for Result in ColResult:
        try:
            ResultObjet = BeautifulSoup(Result)
            Titel = ResultObjet.find("div", {"class": "mw-search-result-heading"}).findAll("a")[0].text
            Url = ResultObjet.find("div", {"class": "mw-search-result-heading"}).findAll("a")[0].get('href')

            DictCommune.update({'ColResultInSnipet': ColResultLen})
            if ColResultLen == 1:
                DictCommune.update({'Wiki_Url': Url, 'Wiki_Name_Snipet': Titel})
            else:
                pass
            if ColResultLen >= 2:
                c = 1

                c += 1
                if NameCommune in Titel:
                    DictCommune.update({'Wiki_Url': Url, 'Wiki_Name_Snipet': Titel})
                else:
                    DictCommune.update({'Wiki_Url_' + str(c): Url, 'Wiki_Name_Snipet_' + str(c): Titel})
            else:
                pass
        except:

            print 'Err', CodeCommune
            pass

    return DictCommune


def get_search():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Departements_28_08_17_insee')
    work_dict = LoadMyDict.copy()
    c = 0
    for data in work_dict.values():
        c += 1
        NameCanton = data['I_Nccenr']
        CodeCanton = data['I_Code_departament']
        dict_snippet = Run(NameCanton.strip(), CodeCanton)
        work_dict[CodeCanton].update(dict_snippet)
        print '{0},{1},{2},{3}'.format(c, NameCanton.strip(), CodeCanton, dict_snippet)
    NameDict = '../WorkBaseFile/Departements_28_08_17_insee_snippet'
    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


def get_searh_up():
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_24_08_17_insee_snippet_2')
    work_dict = LoadMyDict.copy()
    c = 0
    for data in work_dict.values():
        try:
            Wiki_Url = data['Wiki_Url']
        except:
            Wiki_Url = 'None'
        if 'None' in Wiki_Url:
            c += 1
            NameCanton = data['I_Nccent']
            CodeCanton = data['I_Code_Arrondissements']

            # dict_snippet = Run(NameCanton.strip(), str(CodeCanton).replace(' ',''))
            dict_snippet = Run(NameCanton)
            work_dict[CodeCanton].update(dict_snippet)
            print '{0},{1},{2},{3}'.format(c, NameCanton.strip(), CodeCanton, dict_snippet)
    NameDict = '../WorkBaseFile/arrondissements_24_08_17_insee_snippet_3'
    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


def one_up(CodeCantone, Url, Titel):
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Departements_28_08_17_insee_snippet_1')
    work_dict = LoadMyDict.copy()
    my_data = work_dict[CodeCantone].update({'Wiki_Url': Url, 'Wiki_name_arrondissement': Titel})
    NameDict = '../WorkBaseFile/Departements_28_08_17_insee_snippet_1'
    Utils.SaveAndLoadDictFile.SaveDict(work_dict, NameDict)


if __name__ == '__main__':

    # get_searh_up()
    Code_arrondissement = '75'
    Titel = "Paris"
    Url = '/wiki/Paris'
    one_up(Code_arrondissement, Url, Titel)


    #get_search()

    #print Run(Titel, Code_arrondissement)

    #one_up(Code_arrondissement,Url,Titel)

    #print Run_name(Titel)


    #one_up(CodeCantone,Url,Titel)
    #get_search()

    #get_searh_up()

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Departements_28_08_17_insee_snippet_1')
    print urllib.unquote(LoadMyDict['01']['Wiki_Url']).decode('utf8')
    #print urllib.unquote(LoadMyDict['46 15']['Wiki_Url']).decode('utf8')
    #print urllib.unquote(LoadMyDict['79 14']['Wiki_Url']).decode('utf8')

    print len(LoadMyDict)
    for data in LoadMyDict.values():
        try:
            print len(data), data['I_Code_departament'], data['I_Nccenr'], data['Wiki_Url']

        except:
            print 'err', data['I_Code_departament'], data['I_Nccenr']



