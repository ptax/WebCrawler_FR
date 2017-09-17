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
    NameSaveFile = os.path.abspath('../WorkBaseFile/Wiki_Url_20_08_17.csv')
    HeaderLine = DataStructure.FirstColumHeader.GetHeader('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Cantons_20_08_17_cards')
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
    NameSaveFile = os.path.abspath('../WorkBaseFile/20_08_17_canton_google_3.txt')
    HeaderLine = DataStructure.FirstColumHeader.GetHeader_Canton('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Cantons_20_08_17_google')
    print len(DictFile)

    w_rigion_mini = [u'Martinique', u'Guadeloupe']
    for Data, Keys in zip(DictFile.values(), DictFile.keys()):
        I_Code_canton = str(Keys).strip()
        I_Region = Data['I_Region'].strip()
        I_Dep = Data['I_Dep'].strip()
        I_Canton = Data['I_Canton'].strip()
        I_Typct = Data['I_Typct'].strip()
        I_Burcentral = Data['I_Burcentral'].strip()
        I_Tncc = Data['I_Tncc'].strip()
        I_Artmaj = Data['I_Artmaj'].strip()
        I_Ncc = Data['I_Ncc'].strip()
        I_Armin = Data['I_Armin'].strip()
        I_Nccent = Data['I_Nccent'].strip()

        ColResultInSnipet = Data['ColResultInSnipet']

        Wiki_Url = urllib.unquote(Data['Wiki_Url']).decode('utf8')
        Wiki_Name_Snipet = Data['Wiki_Name_Snipet']

        try:
            Wiki_Url_2 = urllib.unquote(Data['Wiki_Url_2']).decode('utf8')
            Wiki_Name_Snipet_2 = Data['Wiki_Name_Snipet_2']
        except:
            Wiki_Url_2 = 'None'
            Wiki_Name_Snipet_2 = 'None'

        try:
            Wiki_Url_3 = urllib.unquote(Data['Wiki_Url_3']).decode('utf8')
            Wiki_Name_Snipet_3 = Data['Wiki_Name_Snipet_3']
        except:
            Wiki_Url_3 = 'None'
            Wiki_Name_Snipet_3 = 'None'

        try:
            Wiki_Url_4 = urllib.unquote(Data['Wiki_Url_4']).decode('utf8')
            Wiki_Name_Snipet_4 = Data['Wiki_Name_Snipet_4']
        except:
            Wiki_Url_4 = 'None'
            Wiki_Name_Snipet_4 = 'None'
        try:
            W_Pays = Data['W_Pays'].strip()
        except:
            W_Pays = 'None'
        try:
            W_Region = Data['W_Region'].strip()
        except:
            W_Region = 'True'
        try:
            W_Departement = Data['W_Departement'].strip()
        except:
            W_Departement = 'None'
        try:
            W_Arrondissement = Data['W_Arrondissement'].strip()
        except:
            W_Arrondissement = 'None'
        try:
            W_Bureau = Data['W_Bureau'].strip()
        except:
            W_Bureau = 'None'
        try:
            W_Code_Canton = Data['W_Code_Canton'].strip()
        except:
            W_Code_Canton = 'None'
        try:
            W_Creation = Data['W_Creation'].strip()
        except:
            W_Creation = 'None'
        try:
            W_Population = Data['W_Population'].strip()
        except:
            W_Population = 'None'
        try:
            W_Communes = Data['W_Communes'].strip()
        except:
            W_Communes = 'None'

        if W_Region:
            try:
                G_Coordinates_northeast_Lat_1 = Data['G_Coordinates_northeast_Lat_1']
            except KeyError:
                G_Coordinates_northeast_Lat_1 = 'None'
            try:
                G_Coordinates_northeast_Lng_1 = Data['G_Coordinates_northeast_Lng_1']
            except KeyError:
                G_Coordinates_northeast_Lng_1 = 'None'
            try:
                G_Coordinates_southwest_Lat_2 = Data['G_Coordinates_southwest_Lat_2']
            except KeyError:
                G_Coordinates_southwest_Lat_2 = 'None'
            try:
                G_Coordinates_southwest_Lng_2 = Data['G_Coordinates_southwest_Lng_2']
            except KeyError:
                G_Coordinates_southwest_Lng_2 = 'None'
            try:
                G_Coordinates_location_Lat_3 = Data['G_Coordinates_location_Lat_3']
            except KeyError:
                G_Coordinates_location_Lat_3 = 'None'
            try:
                G_Coordinates_location_Lng_3 = Data['G_Coordinates_location_Lng_3']
            except KeyError:
                G_Coordinates_location_Lng_3 = 'None'
            try:
                G_FormatAddress = Data['G_FormatAddress']
            except KeyError:
                G_FormatAddress = 'None'
            try:
                G_Types = Data['G_Types']
            except KeyError:
                G_Types = 'None'
            try:
                G_PlaceId = Data['G_PlaceId']
            except:
                G_PlaceId = 'None'
            try:
                How_Get_GooglePlaceID = Data['How_Get_GooglePlaceID']
            except:
                How_Get_GooglePlaceID = 'None'
            try:
                G_Locality_long_name = Data['G_Locality_long_name']
            except:
                G_Locality_long_name = 'None'
            try:
                G_Locality_short_name = Data['G_Locality_short_name']
            except:
                G_Locality_short_name = 'None'
            try:
                G_Locality_types = Data['G_Locality_types']
            except:
                G_Locality_types = 'None'
            try:
                G_AdminLevel_1_long_name = Data['G_AdminLevel_1_long_name']
            except:
                G_AdminLevel_1_long_name = 'None'
            try:
                G_AdminLevel_1_short_name = Data['G_AdminLevel_1_short_name']
            except:
                G_AdminLevel_1_short_name = 'None'
            try:
                G_AdminLevel_1_types = Data['G_AdminLevel_1_types']
            except:
                G_AdminLevel_1_types = 'None'
            try:
                G_AdminLevel_2_long_name = Data['G_AdminLevel_2_long_name']
            except:
                G_AdminLevel_2_long_name = 'None'
            try:
                G_AdminLevel_2_short_name = Data['G_AdminLevel_2_short_name']
            except:
                G_AdminLevel_2_short_name = 'None'
            try:
                G_AdminLevel_2_types = Data['G_AdminLevel_2_types']
            except:
                G_AdminLevel_2_types = 'None'
            try:
                G_Country_long_name = Data['G_Country_long_name']
            except:
                G_Country_long_name = 'None'
            try:
                G_Country_short_name = Data['G_Country_short_name']
            except:
                G_Country_short_name = 'None'
            try:
                G_Country_types = Data['G_Country_types']
            except:
                G_Country_types = 'None'
            try:
                G_postal_code_long_name = Data['G_postal_code_long_name']
            except:
                G_postal_code_long_name = 'None'
            try:
                G_postal_code_short_name = Data['G_postal_code_short_name']
            except:
                G_postal_code_short_name = 'None'
            try:
                G_postal_code_types = Data['G_postal_code_types']
            except:
                G_postal_code_types = 'None'
            try:
                G_FormatAddress = Data['G_FormatAddress']
            except:
                G_FormatAddress = 'None'
            try:
                G_FormatAddress = Data['G_FormatAddress']
            except:
                G_FormatAddress = 'None'
            try:
                G_Types = Data['G_Types']
            except:
                G_Types = 'None'
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

            DataSave = [I_Code_canton,
                        I_Region,
                        I_Dep,
                        I_Canton,
                        I_Typct,
                        I_Burcentral,
                        I_Tncc,
                        I_Artmaj,
                        I_Ncc,
                        I_Armin,
                        I_Nccent,
                        ColResultInSnipet,
                        Wiki_Url,
                        Wiki_Name_Snipet,
                        W_Pays,
                        W_Region,
                        W_Departement,
                        W_Arrondissement,
                        W_Bureau,
                        W_Code_Canton,
                        W_Creation,
                        W_Population,
                        W_Communes,
                        G_Types,
                        G_FormatAddress,
                        G_Locality_long_name,
                        G_Locality_short_name,
                        G_Locality_types,
                        G_AdminLevel_1_long_name,
                        G_AdminLevel_1_short_name,
                        G_AdminLevel_1_types,
                        G_AdminLevel_2_long_name,
                        G_AdminLevel_2_short_name,
                        G_AdminLevel_2_types,
                        G_Country_long_name,
                        G_Country_short_name,
                        G_Country_types,
                        G_postal_code_long_name,
                        G_postal_code_short_name,
                        G_postal_code_types,
                        G_Coordinates_northeast_Lat_1,
                        G_Coordinates_northeast_Lng_1,
                        G_Coordinates_southwest_Lat_2,
                        G_Coordinates_southwest_Lng_2,
                        G_Coordinates_location_Lat_3,
                        G_Coordinates_location_Lng_3,
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