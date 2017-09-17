# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

import csv
import Utils.SaveAndLoadDictFile
import DataStructure.FirstColumHeader
import urllib
import re
import ClearName
import Utils.convert_to_latin


def ReplaceCooma(Str):
    Str = re.sub(",$", '', str(Str))
    Str = re.sub("^,", '', str(Str))
    return str(Str).strip()


def UrlWikiConverName(Url):
    Url = urllib.unquote(Url)
    Url = Url.replace('/wiki/', '')
    Url = re.sub('_\(.*', '', Url)
    return Url


def NameWinkiConvertUrl(Name):
    Name = Name.replace(' ', '_')
    return Name


def SaveCsv():
    ListNone = []
    NameSaveFile = os.path.abspath('../WorkBaseFile/arrondissements_25_08_17_cards.csv')
    HeaderLine = DataStructure.FirstColumHeader.GetHeader('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_25_08_17_cards_up_3')
    print len(DictFile)
    for Data in DictFile.values():
        WikiUrl = str(Data['Wiki_Url'])
        Data = Data['InseeXls_CodeCommune'] + '\t' + Data['InseeXls_NameCommune'] + '\t' + Data[
            'InseeXls_Population'] + '\t' + Data['Wiki_Url']
        if u'Faund' in WikiUrl:
            ListNone.append('Not')
        # Data = {'{0}\t{1}\t{2}\t{3}'}.format(Data['InseeXls_CodeCommune'],Data['InseeXls_NameCommune'],Data['InseeXls_Population'],Data['Wiki_Url'])
        print Data
        text_file = open(NameSaveFile, "a")
        text_file.write(Data + '\n')
    text_file.close()
    print 'Commune Not Faund\t' + str(len(ListNone))


def ConvertCSVFirstData():
    NameSaveFile = os.path.abspath('../WorkBaseFile/arrondissements_25_08_17_cards.txt')
    HeaderLine = DataStructure.FirstColumHeader.GetHeader_Arrondissements('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/arrondissements_25_08_17_cards_up_3')
    print len(DictFile)

    w_rigion_mini = [u'Martinique', u'Guadeloupe']
    for Data, Keys in zip(DictFile.values(), DictFile.keys()):
        I_Code_Arrondissements = str(Keys).strip()
        I_Region = Data['I_Region'].strip()
        I_Dep = Data['I_Dep'].strip()
        I_Ar = Data['I_Ar'].strip()
        I_Cheflieu = Data['I_Cheflieu'].strip()
        I_Tncc = Data['I_Tncc']
        I_Artmaj = Data['I_Artmaj'].strip()
        I_Ncc = Data['I_Ncc'].strip()
        I_Armin = Data['I_Armin'].strip()
        I_Nccent = Data['I_Nccent'].strip()

        ColResultInSnipet = Data['ColResultInSnipet']

        Wiki_Url = urllib.unquote(Data['Wiki_Url']).decode('utf8')
        Wiki_Name_Snipet = str(Data['Wiki_Name_Snipet']).strip()
        try:
            Wiki_name_arrondissement = str(Data['Wiki_name_arrondissement'].replace('\n', ' ')).strip()
        except:
            Wiki_name_arrondissement = 'None'

        try:
            Wiki_Coordinates_lat = str(Data['Wiki_Coordinates_lat']).strip()
            Wiki_Coordinates_lon = str(Data['Wiki_Coordinates_lon']).strip()
        except:
            Wiki_Coordinates_lat = 'None'
            Wiki_Coordinates_lon = 'None'

        try:
            W_Pays = Data['W_Pays'].strip()
        except:
            W_Pays = 'None'
        try:
            W_Region = Data['W_Region'].strip()
        except:
            W_Region = 'None'
        try:
            W_Departement = Data['W_Departement'].strip()
        except:
            W_Departement = 'None'
        try:
            W_Chef_lieu = Data['W_Chef-lieu'].strip()
        except:
            W_Chef_lieu = 'None'
        try:
            W_Code_arrondissement = Data['W_Code_arrondissement'].strip()
        except:
            W_Code_arrondissement = 'None'
        try:
            W_Population = Data['W_Population'].strip()
        except:
            W_Population = 'None'
        try:
            W_Densite = Data['W_Densite'].strip()
        except:
            W_Densite = 'None'
        try:
            W_Superficie = Data['W_Superficie'].strip()
        except:
            W_Superficie = 'None'
        try:
            W_Cantons = Data['W_Cantons'].replace('\n', ' ').strip()
        except:
            W_Cantons = 'None'
        try:
            W_Communes = Data['W_Communes'].replace('\n', ' ').strip()
        except:
            W_Cantons = 'None'

        if W_Region:
            try:
                W_Name_ru = Data['W_Name_ru']
            except KeyError:
                W_Name_ru = 'None'
            try:
                W_Name_uk = Data['W_Name_uk']
            except KeyError:
                W_Name_uk = 'None'
            try:
                W_Name_en = Data['W_Name_en']
            except KeyError:
                W_Name_en = 'None'
            try:
                W_Name_de = Data['W_Name_de']
            except KeyError:
                W_Name_de = 'None'
            try:
                W_Name_pl = Data['W_Name_pl']
            except KeyError:
                W_Name_pl = 'None'
            try:
                W_Name_es = Data['W_Name_es']
            except KeyError:
                W_Name_es = 'None'
            try:
                W_Name_pt = Data['W_Name_pt']
            except KeyError:
                W_Name_pt = 'None'
            try:
                W_Name_it = Data['W_Name_it']
            except KeyError:
                W_Name_it = 'None'
            try:
                W_Name_nl = Data['W_Name_nl']
            except KeyError:
                W_Name_nl = 'None'
            try:
                W_Name_da = Data['W_Name_da']
            except KeyError:
                W_Name_da = 'None'
            try:
                W_Name_no = Data['W_Name_no']
            except KeyError:
                W_Name_no = 'None'
            try:
                W_Name_sv = Data['W_Name_sv']
            except KeyError:
                W_Name_sv = 'None'
            try:
                W_Name_cs = Data['W_Name_cs']
            except KeyError:
                W_Name_cs = 'None'
            try:
                W_Name_ro = Data['W_Name_ro']
            except KeyError:
                W_Name_ro = 'None'
            try:
                W_Name_bg = Data['W_Name_bg']
            except KeyError:
                W_Name_bg = 'None'
            try:
                W_Name_hu = Data['W_Name_hu']
            except KeyError:
                W_Name_hu = 'None'
            try:
                W_Name_sk = Data['W_Name_sk']
            except KeyError:
                W_Name_sk = 'None'
            try:
                W_Name_sl = Data['W_Name_sl']
            except KeyError:
                W_Name_sl = 'None'
            try:
                W_Name_sh = Data['W_Name_sh']
            except KeyError:
                W_Name_sh = 'None'
            try:
                W_Name_hr = Data['W_Name_hr']
            except KeyError:
                W_Name_hr = 'None'
            try:
                W_Url_ru = Data['W_Url_ru']
            except KeyError:
                W_Url_ru = 'None'
            try:
                W_Url_uk = Data['W_Url_uk']
            except KeyError:
                W_Url_uk = 'None'
            try:
                W_Url_en = Data['W_Url_en']
            except KeyError:
                W_Url_en = 'None'
            try:
                W_Url_de = Data['W_Url_de']
            except KeyError:
                W_Url_de = 'None'
            try:
                W_Url_pl = Data['W_Url_pl']
            except KeyError:
                W_Url_pl = 'None'
            try:
                W_Url_es = Data['W_Url_es']
            except KeyError:
                W_Url_es = 'None'
            try:
                W_Url_pt = Data['W_Url_pt']
            except KeyError:
                W_Url_pt = 'None'
            try:
                W_Url_it = Data['W_Url_it']
            except KeyError:
                W_Url_it = 'None'
            try:
                W_Url_nl = Data['W_Url_nl']
            except KeyError:
                W_Url_nl = 'None'
            try:
                W_Url_da = Data['W_Url_da']
            except KeyError:
                W_Url_da = 'None'
            try:
                W_Url_no = Data['W_Url_no']
            except KeyError:
                W_Url_no = 'None'
            try:
                W_Url_sv = Data['W_Url_sv']
            except KeyError:
                W_Url_sv = 'None'
            try:
                W_Url_cs = Data['W_Url_cs']
            except KeyError:
                W_Url_cs = 'None'
            try:
                W_Url_ro = Data['W_Url_ro']
            except KeyError:
                W_Url_ro = 'None'
            try:
                W_Url_bg = Data['W_Url_bg']
            except KeyError:
                W_Url_bg = 'None'
            try:
                W_Url_hu = Data['W_Url_hu']
            except KeyError:
                W_Url_hu = 'None'
            try:
                W_Url_sk = Data['W_Url_sk']
            except KeyError:
                W_Url_sk = 'None'
            try:
                W_Url_sl = Data['W_Url_sl']
            except KeyError:
                W_Url_sl = 'None'
            try:
                W_Url_sh = Data['W_Url_sh']
            except KeyError:
                W_Url_sh = 'None'
            try:
                W_Url_hr = Data['W_Url_hr']
            except KeyError:
                W_Url_hr = 'None'

            DataSave = [I_Code_Arrondissements,
                        I_Region,
                        I_Dep,
                        I_Ar,
                        I_Cheflieu,
                        I_Tncc,
                        I_Artmaj,
                        I_Ncc,
                        I_Armin,
                        I_Nccent,
                        ColResultInSnipet,
                        Wiki_Url,
                        Wiki_Name_Snipet,
                        Wiki_name_arrondissement,
                        Wiki_Coordinates_lat,
                        Wiki_Coordinates_lon,
                        W_Pays,
                        W_Region,
                        W_Departement,
                        W_Chef_lieu,
                        W_Code_arrondissement,
                        W_Population,
                        W_Densite,
                        W_Superficie,
                        W_Cantons,
                        W_Communes,
                        W_Name_ru,
                        W_Name_uk,
                        W_Name_en,
                        W_Name_de,
                        W_Name_pl,
                        W_Name_es,
                        W_Name_pt,
                        W_Name_it,
                        W_Name_nl,
                        W_Name_da,
                        W_Name_no,
                        W_Name_sv,
                        W_Name_cs,
                        W_Name_ro,
                        W_Name_bg,
                        W_Name_hu,
                        W_Name_sk,
                        W_Name_sl,
                        W_Name_sh,
                        W_Name_hr,
                        W_Url_ru,
                        W_Url_uk,
                        W_Url_en,
                        W_Url_de,
                        W_Url_pl,
                        W_Url_es,
                        W_Url_pt,
                        W_Url_it,
                        W_Url_nl,
                        W_Url_da,
                        W_Url_no,
                        W_Url_sv,
                        W_Url_cs,
                        W_Url_ro,
                        W_Url_bg,
                        W_Url_hu,
                        W_Url_sk,
                        W_Url_sl,
                        W_Url_sh,
                        W_Url_hr,
                        ]

            # DataInSaveFile = '{' + "'" + str(InseeXls_CodeCommune) + "':" + str(Data) + '}'
            # text_file = open("../WorkBaseFile/16_07_17.txt", "a")
            #text_file.write(str(DataInSaveFile) + '\n')


            DataSave = '\t'.join(str(v) for v in DataSave)

            #DataSave = '\t'.join(DataSave)
            text_file = open(NameSaveFile, "a")
            text_file.write(DataSave + '\n')
        else:
            pass

    text_file.close()


if __name__ == '__main__':
    ConvertCSVFirstData()

    '''
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/WikiDataPage_11_06_17')
    print len(LoadMyDict)
    for i in LoadMyDict.values():
        try:
            print i['InseeXls_CodeCommune'],i['W_Pays'],i['W_Url_en'],i['W_Name_en']
        except:
            pass
    '''