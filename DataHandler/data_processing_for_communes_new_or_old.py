# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re
import Utils.SaveAndLoadDictFile
import pandas as pd
import Utils.GetListInFile
from sets import Set
import Wiki.GetResultUrlCommuneInWiki_2
import urllib2
from bs4 import BeautifulSoup
import urllib2
import Wiki.GetDataInWikiTable
import Utils.ConvertCordinates
import WorkGoogleMap.GetDataInCommune
import Utils.convert_to_latin
import Utils.ClearName


def export_of_changed_commune_data():
    """ Selecting all data from a common database would work with a separate set of data. """
    dict_work = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/30_06_17_1')
    # dict_work = dict_load.copy()
    dict_change_commune = {}
    c = 0
    for Data in dict_work.values():
        try:
            InseeXls_CodeCommune = Data['InseeXls_CodeCommune']
            ColResultInSnipet = Data['ColResultInSnipet']

            ColResultInSnipet = int(ColResultInSnipet)

            if ColResultInSnipet >= 2:
                c += 1
                print c, Data['ColResultInSnipet'], InseeXls_CodeCommune
                my_data = dict_work[InseeXls_CodeCommune]
                #print my_data,'wtf'
                dict_change_commune[InseeXls_CodeCommune] = my_data

            else:
                pass
        except:
            pass

    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune'
    Utils.SaveAndLoadDictFile.SaveDict(dict_change_commune, name_dict)
    print len(dict_change_commune)


def countDuplicatesInList(dupedList):
    uniqueSet = Set(item for item in dupedList)
    return [(item, dupedList.count(item)) for item in uniqueSet]


def read_csv_change_communes_insee():
    """
        Return Dict Format Structure in data in file Code Insee in insee.fr
        You put list in tree colum and dict return
    """
    NameFile = os.path.abspath('../WorkBaseFile/ChangeName_2.csv')
    ListDataInInseeXls = Utils.GetListInFile.Run(NameFile)
    DictCommuneInsee = {}

    ListCodeCommunes = []
    for NumCodeInsee in ListDataInInseeXls:
        data = NumCodeInsee.split(';')
        InseeChange_DepComN = str(data[0]).strip()
        ListCodeCommunes.append(InseeChange_DepComN)

    ListCodeCommunes = [x for x in ListCodeCommunes if x]

    ListNumCodeInse = countDuplicatesInList(ListCodeCommunes)

    dict_num = {}
    for CodeCumene in ListNumCodeInse:
        dict_num[CodeCumene[0]] = CodeCumene[1]
    print dict_num['50487']

    c = 0
    for data in ListDataInInseeXls:
        c += 1
        data = data.split(';')
        InseeChange_DepComN = str(data[0]).strip()
        InseeChange_NomCN = str(data[1]).strip()
        InseeChange_DepComA = str(data[2]).strip()
        InseeChange_NomCA = str(data[3]).strip()
        InseeChange_ComDLG = str(data[4]).strip()
        InseeChange_Date1 = str(data[5]).strip()
        InseeChange_Date2 = str(data[6]).strip()
        InseeChange_Date3 = str(data[7]).strip()

        try:
            NumCode = dict_num[InseeChange_DepComN]
        except:
            NumCode = 0

        CodeInseeTheme = str(InseeChange_DepComN) + '_' + str(NumCode) + '_' + str(InseeChange_DepComA)
        print c, CodeInseeTheme

        DictCommuneInsee[CodeInseeTheme] = {'InseeChange_DepComN': InseeChange_DepComN,
                                            'InseeChange_NomCN': InseeChange_NomCN,
                                            'InseeChange_DepComA': InseeChange_DepComA,
                                            'InseeChange_NomCA': InseeChange_NomCA,
                                            'InseeChange_ComDLG': InseeChange_ComDLG,
                                            'InseeChange_Date1': InseeChange_Date1,
                                            'InseeChange_Date2': InseeChange_Date2,
                                            'InseeChange_Date3': InseeChange_Date3


                                            }

    name_dict = '../WorkBaseFile/12_07_17_trust_codirovka'
    Utils.SaveAndLoadDictFile.SaveDict(DictCommuneInsee, name_dict)
    print len(DictCommuneInsee)


def comparison_two_dict():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_Insee_Dict_change_commune')
    dict_work = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/30_06_17_1')

    dict_snippent_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune')
    listWorkLook = []
    listErr = []
    c = 0
    for i in dict_insee_commune.items():
        c += 1
        # print i[1]['InseeChange_DepComN']
        try:
            print dict_snippent_commune[i[1]['InseeChange_DepComN']]
            listWorkLook.append(c)
        except KeyError:
            print i[1]['InseeChange_DepComN'], KeyError
            listErr.append(i[1]['InseeChange_DepComN'])

    for i in listErr:
        print i
    print len(listErr)
    try:
        print dict_work['61004']
    except:
        print '61004'
        pass
    try:
        print dict_work['61168']
    except:
        print '61168'
        pass
    print len(listWorkLook)


def looking_snipet():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_2')
    WorkDict = dict_insee_commune.copy()
    c = 0
    list_test = []
    for i in WorkDict.items():
        c += 1
        InseeChange_DepComN = i[1]['InseeChange_DepComN']
        InseeChange_DepComA = i[1]['InseeChange_DepComA']
        NumStarCommune = i[1]['InseeChange_DepComA']

        NameCommune = i[1]['InseeChange_NomCA']
        if int(InseeChange_DepComN) != int(InseeChange_DepComA):
            WikiRes = Wiki.GetResultUrlCommuneInWiki_2.Run(NameCommune, InseeChange_DepComN)
            data = {'ColResultInSnipet': WikiRes['ColResultInSnipet']}
            WorkDict[i[0]].update(data)
            print c, WikiRes['ColResultInSnipet'], InseeChange_DepComN, InseeChange_DepComA, WikiRes['Wiki_NameSnipet']
        else:
            pass
    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_3_1'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def change_key():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_1')
    WorkDict = dict_insee_commune.copy()
    MyDict = {}
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):


        if int(Data['InseeChange_DepComN']) == int(Data['InseeChange_DepComA']):
            print Keys, Data

            ColResultInSnipet = Data['ColResultInSnipet']
            print ColResultInSnipet
            c = 0
            for i in range(ColResultInSnipet):
                c += 1
                ThemeKeys = str(Keys) + '_' + str(c)
                print ThemeKeys

                MyDict[ThemeKeys] = {'InseeChange_DepComN': Data['InseeChange_DepComN'],
                                     'InseeChange_NomCN': Data['InseeChange_NomCN'],
                                     'InseeChange_DepComA': Data['InseeChange_DepComA'],
                                     'InseeChange_NomCA': Data['InseeChange_NomCA'],
                                     'InseeChange_ComDLG': Data['InseeChange_ComDLG'],
                                     'InseeChange_Date1': Data['InseeChange_Date1'],
                                     'InseeChange_Date2': Data['InseeChange_Date2'],
                                     'InseeChange_Date3': Data['InseeChange_Date3'],
                                     'ColResultInSnipet': Data['ColResultInSnipet'],
                                     'NumSnipet': c}

            try:
                del MyDict[Keys]
            except KeyError:
                pass
        else:

            MyDict[Keys] = {'InseeChange_DepComN': Data['InseeChange_DepComN'],
                            'InseeChange_NomCN': Data['InseeChange_NomCN'],
                            'InseeChange_DepComA': Data['InseeChange_DepComA'],
                            'InseeChange_NomCA': Data['InseeChange_NomCA'],
                            'InseeChange_ComDLG': Data['InseeChange_ComDLG'],
                            'InseeChange_Date1': Data['InseeChange_Date1'],
                            'InseeChange_Date2': Data['InseeChange_Date2'],
                            'InseeChange_Date3': Data['InseeChange_Date3'],
                            'ColResultInSnipet': None,

                            'NumSnipet': None}

    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_2'
    Utils.SaveAndLoadDictFile.SaveDict(MyDict, name_dict)

    print len(MyDict)


def change_key_sub_coomune():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_3')
    WorkDict = dict_insee_commune.copy()
    MyDict = {}
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        if int(Data['InseeChange_DepComN']) != int(Data['InseeChange_DepComA']):
            print Keys, Data
            ColResultInSnipetSubSnipet = Data['ColResultInSnipetSubSnipet']
            c = 0
            for i in range(ColResultInSnipetSubSnipet):
                c += 1
                ThemeKeys = str(Keys) + '_' + str(c)
                print ThemeKeys
                MyDict[ThemeKeys] = {'InseeChange_DepComN': Data['InseeChange_DepComN'],
                                     'InseeChange_NomCN': Data['InseeChange_NomCN'],
                                     'InseeChange_DepComA': Data['InseeChange_DepComA'],
                                     'InseeChange_NomCA': Data['InseeChange_NomCA'],
                                     'InseeChange_ComDLG': Data['InseeChange_ComDLG'],
                                     'InseeChange_Date1': Data['InseeChange_Date1'],
                                     'InseeChange_Date2': Data['InseeChange_Date2'],
                                     'InseeChange_Date3': Data['InseeChange_Date3'],
                                     'ColResultInSnipet': Data['ColResultInSnipet'],
                                     'NumSnipet': Data['NumSnipet'],
                                     'ColResultInSnipetSubSnipet': Data['ColResultInSnipetSubSnipet'],
                                     'NumSubSnipeet': c

                                     }
            try:
                del MyDict[Keys]
            except KeyError:
                pass
        else:
            MyDict[Keys] = {'InseeChange_DepComN': Data['InseeChange_DepComN'],
                            'InseeChange_NomCN': Data['InseeChange_NomCN'],
                            'InseeChange_DepComA': Data['InseeChange_DepComA'],
                            'InseeChange_NomCA': Data['InseeChange_NomCA'],
                            'InseeChange_ComDLG': Data['InseeChange_ComDLG'],
                            'InseeChange_Date1': Data['InseeChange_Date1'],
                            'InseeChange_Date2': Data['InseeChange_Date2'],
                            'InseeChange_Date3': Data['InseeChange_Date3'],
                            'ColResultInSnipet': Data['ColResultInSnipet'],
                            'NumSnipet': Data['NumSnipet'],
                            'ColResultInSnipetSubSnipet': None,
                            'NumSubSnipeet': None}

    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_4'
    Utils.SaveAndLoadDictFile.SaveDict(MyDict, name_dict)


def get_wiki_snippet(CodeCommune, NumSnippet):
    CodeCommune = str(CodeCommune).strip()
    DictCommune = {'Wiki_UrlCommune': None,
                   'Wiki_NameSnipet': None,

                   }
    wiki = "https://fr.wikipedia.org/w/index.php?search=%22Code+commune+" + CodeCommune + "%22&title=Sp%C3%A9cial:Recherche&profile=default&fulltext=1&searchengineselect=mediawiki&searchToken=ac9zaxa1lggzxpdhc5ukg06t6"
    header = {'User-Agent': 'Mozilla/5.0'}  # Needed to prevent 403 error on Wikipedia
    req = urllib2.Request(wiki, headers=header)
    page = urllib2.urlopen(req)
    soup = BeautifulSoup(page)
    SearchResult = soup.find("ul", {"class": "mw-search-results"})
    ColResult = str(SearchResult).replace('<ul class="mw-search-results">', '').split('<li>')
    ColResult = [x for x in ColResult if x]
    ColResultLen = len(ColResult)
    ResultObjet = BeautifulSoup(ColResult[NumSnippet])

    Titel = ResultObjet.find("div", {"class": "mw-search-result-heading"}).findAll("a")[0].text
    Url = ResultObjet.find("div", {"class": "mw-search-result-heading"}).findAll("a")[0].get('href')
    DictCommune.update({'Wiki_UrlCommune': Url, 'Wiki_NameSnipet': Titel})

    return DictCommune


def update_wiki_snippet():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_4')
    WorkDict = dict_insee_commune.copy()
    MyDict = {}
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        c += 1
        if Data['NumSnipet'] != None:
            NumSnippet = int(Data['NumSnipet']) - 1
            CodeCommune = Data['InseeChange_DepComN']
            BaseUp = get_wiki_snippet(CodeCommune, NumSnippet)
            WorkDict[Keys].update(BaseUp)
            print 'New Commune \t', c, CodeCommune, BaseUp
        elif Data['NumSubSnipeet'] != None:
            NumSubSnippet = int(Data['NumSubSnipeet']) - 1
            CodeCommune = Data['InseeChange_DepComA']
            BaseUp = get_wiki_snippet(CodeCommune, NumSubSnippet)
            WorkDict[Keys].update(BaseUp)
            print 'Old Commune \t', c, CodeCommune, BaseUp

    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_5'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def get_data_in_wiki():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_5')
    WorkDict = dict_insee_commune.copy()
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        c += 1

        WikiUrl = Data['Wiki_UrlCommune']
        Url = "https://fr.wikipedia.org" + WikiUrl
        GetHtml = Wiki.GetDataInWikiTable.GetHtml(Url)
        Table = GetHtml[0]
        LangHref = GetHtml[1]
        DictTableInformation = Wiki.GetDataInWikiTable.GetInformation(Table)
        LanguagesDict = Wiki.GetDataInWikiTable.FilterLanguages(Wiki.GetDataInWikiTable.GetLanguages(LangHref))
        WikiStatus = Wiki.GetDataInWikiTable.get_status(Table)

        WorkDict[Keys].update(DictTableInformation)
        WorkDict[Keys].update(LanguagesDict)
        WorkDict[Keys].update(WikiStatus)
        print c, WikiUrl, Keys, WikiStatus
    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_6'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def get_google_data():
    listErr = []
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_6')
    WorkDict = dict_insee_commune.copy()
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        c += 1

        try:
            Cordinates = str(Data['W_Cordommees']).replace('ou,', 'S').split(',')
            Cordinate = str(Utils.ConvertCordinates.dms2dec(Cordinates[0])) + ',' + str(
                Utils.ConvertCordinates.dms2dec(Cordinates[1]))
            Cordinates = Cordinate.split(',')

            Cordinat_1 = Cordinates[0]
            Cordinat_2 = Cordinates[1]
            # print c,Keys,Cordinat_1,Cordinat_2
            result = WorkGoogleMap.GetDataInCommune.GetDataInCordinates(Cordinat_1, Cordinat_2)
            GoogleDataAdree = WorkGoogleMap.GetDataInCommune.StructureLocalType(result)
            GoogleDataCorrdinat = WorkGoogleMap.GetDataInCommune.GetCoordinatesInGoogle(result)

            print c, Data['Wiki_UrlCommune'], Cordinat_1, Cordinat_2, GoogleDataAdree, GoogleDataCorrdinat
            WorkDict[Keys].update(GoogleDataAdree)
            WorkDict[Keys].update(GoogleDataCorrdinat)

        except KeyError:
            listErr.append(Keys)
            pass

    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_7'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)
    for i in listErr:
        print i


def data_insert_key():
    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_7')
    WorkDict = dict_insee_commune.copy()
    c = 0
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        MyData = {'KeywordId': Keys}
        WorkDict[Keys].update(MyData)
    name_dict = '../WorkBaseFile/07_07_17_dict_change_commune_8'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, name_dict)


def exsport_csv():
    import pandas as pd

    data_columns = ['KeywordId',
                    'Format_Wiki_NameSnipet',
                    'Format__NomCN',
                    'NomCN_Wiki_Name_comparisons',
                    'InseeChange_DepComN',
                    'InseeChange_NomCN',
                    'InseeChange_DepComA',
                    'InseeChange_NomCA',
                    'InseeChange_ComDLG',
                    'InseeChange_Date1',
                    'InseeChange_Date2',
                    'InseeChange_Date3',
                    'ColResultInSnipet',
                    'ColResultInSnipetSubSnipet',
                    'Wiki_UrlCommune',
                    'Wiki_NameSnipet',
                    'WikiStatus',
                    'W_Pays',
                    'W_Region',
                    'W_Departement',
                    'W_Arrondissement',
                    'W_Canton',
                    'W_Intercommunalite',
                    'W_CodePostal',
                    'W_CodeCommune',
                    'W_Population',
                    'W_Densite',
                    'W_Cordommees',
                    'W_Altitude',
                    'W_Superficie',
                    'W_Name_ru',
                    'W_Name_uk',
                    'W_Name_en',
                    'W_Name_de',
                    'W_Name_pl',
                    'W_Name_es',
                    'W_Name_pt',
                    'W_Name_it',
                    'W_Name_nl',
                    'W_Name_da',
                    'W_Name_no',
                    'W_Name_sv',
                    'W_Name_cs',
                    'W_Name_ro',
                    'W_Name_bg',
                    'W_Name_hu',
                    'W_Name_sk',
                    'W_Name_sl',
                    'W_Name_sh',
                    'W_Name_hr',
                    'W_Url_ru',
                    'W_Url_uk',
                    'W_Url_en',
                    'W_Url_de',
                    'W_Url_pl',
                    'W_Url_es',
                    'W_Url_pt',
                    'W_Url_it',
                    'W_Url_nl',
                    'W_Url_da',
                    'W_Url_no',
                    'W_Url_sv',
                    'W_Url_cs',
                    'W_Url_ro',
                    'W_Url_bg',
                    'W_Url_hu',
                    'W_Url_sk',
                    'W_Url_sl',
                    'W_Url_sh',
                    'W_Url_hr',
                    'G_Coordinates_northeast_Lat_1',
                    'G_Coordinates_northeast_Lng_1',
                    'G_Coordinates_southwest_Lat_2',
                    'G_Coordinates_southwest_Lng_2',
                    'G_Coordinates_location_Lat_3',
                    'G_Coordinates_location_Lng_3',

                    'G_Locality_long_name',
                    'G_Locality_short_name',
                    'G_Locality_types',
                    'G_AdminLevel_1_long_name',
                    'G_AdminLevel_1_short_name',
                    'G_AdminLevel_1_types',
                    'G_AdminLevel_2_long_name',
                    'G_AdminLevel_2_short_name',
                    'G_AdminLevel_2_types',
                    'G_Country_long_name',
                    'G_Country_short_name',
                    'G_Country_types',
                    'G_postal_code_long_name',
                    'G_postal_code_short_name',
                    'G_postal_code_types',
                    'G_FormatAddress',
                    'G_Types']

    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/12_07_17_up_and_change')

    NameCsv = os.path.abspath('../WorkBaseFile/12_07_17_4.csv')
    pd.DataFrame(dict_insee_commune).T.reset_index().to_csv(NameCsv, header=True, index=False, columns=data_columns,
                                                            sep=b'\t')


def UpdateName():
    import urllib

    TrustCodirovka = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/12_07_17_trust_codirovka')

    dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/07_07_17_dict_change_commune_8')
    dict_work = dict_insee_commune.copy()

    for Data, Keys in zip(dict_work.values(), dict_work.keys()):
        StarKey = str(Keys)
        StarKey = re.sub(r'_\d$', '', StarKey)
        C_InseeChange_NomCN = str(TrustCodirovka[StarKey]['InseeChange_NomCN']).decode('utf-8')
        C_InseeChange_NomCA = str(TrustCodirovka[StarKey]['InseeChange_NomCA']).decode('utf-8')
        Wiki_UrlCommune = urllib.unquote(Data['Wiki_UrlCommune']).decode('utf8')

        Format__NomCN = Utils.convert_to_latin.change_letter(str(C_InseeChange_NomCN).strip().decode(u'utf-8')).replace(
            '-', '').replace(' ', '')
        Format_Wiki_NameSnipet = Utils.convert_to_latin.change_letter(
            str(Data['Wiki_NameSnipet'].strip().decode(u'utf-8'))).replace('-', '').replace(' ', '')

        Format__NomCN = Utils.ClearName.Run_2(Format__NomCN)
        Format_Wiki_NameSnipet = Utils.ClearName.Run_2(Format_Wiki_NameSnipet)

        print Keys, Format__NomCN, Format_Wiki_NameSnipet
        if Format__NomCN == Format_Wiki_NameSnipet:
            NomCN_Wiki_Name_comparisons = True
        else:
            NomCN_Wiki_Name_comparisons = False

        UpMyData = {'InseeChange_NomCN': C_InseeChange_NomCN,
                    'InseeChange_NomCA': C_InseeChange_NomCA,
                    'Wiki_UrlCommune': Wiki_UrlCommune,
                    'Format__NomCN': Format__NomCN,
                    'Format_Wiki_NameSnipet': Format_Wiki_NameSnipet,
                    'NomCN_Wiki_Name_comparisons': NomCN_Wiki_Name_comparisons
                    }
        dict_work[Keys].update(UpMyData)
    name_dict = '../WorkBaseFile/12_07_17_up_and_change'
    Utils.SaveAndLoadDictFile.SaveDict(dict_work, name_dict)


if __name__ == '__main__':
    # data_insert_key()
    exsport_csv()

    #read_csv_change_communes_insee()
    #   UpdateName()

    #looking_snipet()
    #change_key_sub_coomune()
    #print get_wiki_snippet('49050',0)

    #update_wiki_snippet()
    #get_data_in_wiki()

    #get_google_data()

    #dict_insee_commune = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/12_07_17_up_and_change')

    #print len(dict_insee_commune)

    #for Data,Keys in zip(dict_insee_commune.values(),dict_insee_commune.keys()):
    #print dict_insee_commune['04033_2_04033_1']['InseeChange_NomCA']

