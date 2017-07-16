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
    NameSaveFile = os.path.abspath('../WorkBaseFile/Wiki_Url_08_06_17.csv')
    HeaderLine = DataStructure.FirstColumHeader.GetHeader('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_WikiUrl_08_06_17_2')
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
    NameSaveFile = os.path.abspath('../WorkBaseFile/29_06_17_Occitanie.txt')
    HeaderLine = DataStructure.FirstColumHeader.GetHeader_2('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/26_06_17_5')
    print len(DictFile)

    for Data in DictFile.values():

        try:
            W_Region = Data['W_Region'].replace(',', '').replace(u'(préfecture)', '').replace(
                u'(siège du conseil régional)', '').replace(u'(siège)', '').replace(u'(Préfecture)', '').replace(
                u'(bureau centralisateur)', '').replace(u'(Champagne-Ardenne)', '').replace(u'(chef-lieu)', '').replace(
                u"Provence-Alpes-Côte d'Azur", u"Provence-Alpes-Côte d’Azur").strip()

        except KeyError:
            W_Region = 'None'
        if u'Occitanie' in W_Region:
            try:
                InseeXls_CodeCommune = ReplaceCooma(Data['InseeXls_CodeCommune'])
            except KeyError:
                InseeXls_CodeCommune = 'None'
            try:
                InseeXls_NameCommune = ReplaceCooma(Data['InseeXls_NameCommune'])
            except KeyError:
                InseeXls_NameCommune
            try:
                InseeXls_Population = ReplaceCooma(Data['InseeXls_Population'])
            except KeyError:
                InseeXls_Population = 'None'
            try:
                Wiki_Url = Data['Wiki_Url']
            except KeyError:
                Wiki_Url = 'None'
            try:
                W_Pays = ReplaceCooma(Data['W_Pays'])
            except KeyError:
                W_Pays = 'None'
            try:
                W_Region = ReplaceCooma(Data['W_Region'])
            except KeyError:
                W_Region = 'None'
            try:
                W_Departement = ReplaceCooma(Data['W_Departement'])
            except KeyError:
                W_Departement = 'None'
            try:
                W_Arrondissement = ReplaceCooma(Data['W_Arrondissement'])
            except KeyError:
                W_Arrondissement = 'None'
            try:
                W_Canton = ReplaceCooma(Data['W_Canton'])
            except KeyError:
                W_Canton = 'None'
            try:
                W_Intercommunalite = ReplaceCooma(Data['W_Intercommunalite'])
            except KeyError:
                W_Intercommunalite = 'None'
            try:
                W_CodePostal = ReplaceCooma(Data['W_CodePostal'])
            except KeyError:
                W_CodePostal = 'None'
            try:
                W_CodeCommune = ReplaceCooma(Data['W_CodeCommune'])
            except KeyError:
                W_CodeCommune = 'None'
            try:
                W_Population = ReplaceCooma(Data['W_Population'])
            except KeyError:
                W_Population = 'None'
            try:
                W_Densite = ReplaceCooma(Data['W_Densite'])
            except KeyError:
                W_Densite = 'None'
            try:
                W_Cordommees = ReplaceCooma(Data['W_Cordommees'])
            except KeyError:
                W_Cordommees = 'None'
            try:
                W_Altitude = ReplaceCooma(Data['W_Altitude'])
            except KeyError:
                W_Altitude = 'None'
            try:
                W_Superficie = ReplaceCooma(Data['W_Superficie'])
            except KeyError:
                W_Superficie = 'None'
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
                W_Cordommees_Convert = Data['W_Cordommees_Convert']
            except:
                W_Cordommees_Convert = 'None'
            try:
                G_Name_ru = Data['G_Name_ru']
            except:
                G_Name_ru = 'None'
            try:
                G_Name_uk = Data['G_Name_uk']
            except:
                G_Name_uk = 'None'
            try:
                G_Name_en = Data['G_Name_en']
            except:
                G_Name_en = 'None'

            try:
                if str(Data['InseeXls_CodeCommune']).strip() == ReplaceCooma(Data['W_CodeCommune']):
                    F_Compare_InseeXls_CodeCommune_W_CodeCommune = True
                else:
                    F_Compare_InseeXls_CodeCommune_W_CodeCommune = False
            except:
                F_Compare_InseeXls_CodeCommune_W_CodeCommune = 'None'
            try:
                if UrlWikiConverName(Data['Wiki_Url']) == NameWinkiConvertUrl(Data['InseeXls_NameCommune']):
                    F_Compare_InseeXls_NameCommune_Wiki_Url = True
                else:
                    F_Compare_InseeXls_NameCommune_Wiki_Url = False
            except:
                F_Compare_InseeXls_NameCommune_Wiki_Url = 'None'
            try:
                if Data['G_Locality_long_name'] == Data['InseeXls_NameCommune']:
                    F_Compare_InseeXls_NameCommune_G_Locality_long_name = True
                else:
                    F_Compare_InseeXls_NameCommune_G_Locality_long_name = False
            except:
                F_Compare_InseeXls_NameCommune_G_Locality_long_name = 'None'

            try:
                Wiki_UrlInCommuneSnipet = Data['Wiki_UrlInCommuneSnipet']
            except:
                Wiki_UrlInCommuneSnipet = 'None'
            try:
                Wiki_NameSnipet = Data['Wiki_NameSnipet']
            except:
                Wiki_NameSnipet = 'None'
            try:
                Wiki_Old_UrlInCommune = Data['Wiki_Old_UrlInCommune']
            except:
                Wiki_Old_UrlInCommune = 'None'
            try:
                Wiki_Old_NameSnipet = Data['Wiki_Old_NameSnipet']
            except:
                Wiki_Old_NameSnipet = 'None'
            try:
                ColResultInSnipet = Data['ColResultInSnipet']
            except:
                ColResultInSnipet = 'None'


            # print InseeXls_CodeCommune,W_Canton,W_Name_ru
            #print G_Coordinates_northeast_Lat_1,G_Coordinates_northeast_Lng_1,G_Coordinates_southwest_Lat_2,G_Coordinates_southwest_Lng_2,G_Coordinates_location_Lat_3,G_Coordinates_location_Lng_3
            DataSave = [InseeXls_CodeCommune,
                        InseeXls_NameCommune,
                        InseeXls_Population,
                        urllib.unquote(Wiki_Url).decode('utf8'),
                        W_Pays,
                        W_Region,
                        ClearName.Run(W_Departement),
                        ClearName.Run(W_Arrondissement),
                        ClearName.Run(W_Canton),
                        W_Intercommunalite,
                        W_CodePostal,
                        W_CodeCommune,
                        W_Population,
                        W_Densite,
                        W_Cordommees,
                        W_Altitude,
                        W_Superficie,
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
                        G_Coordinates_northeast_Lat_1,
                        G_Coordinates_northeast_Lng_1,
                        G_Coordinates_southwest_Lat_2,
                        G_Coordinates_southwest_Lng_2,
                        G_Coordinates_location_Lat_3,
                        G_Coordinates_location_Lng_3,
                        G_PlaceId,
                        How_Get_GooglePlaceID,
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
                        G_FormatAddress,
                        G_Types,
                        W_Cordommees_Convert,
                        G_Name_ru,
                        G_Name_uk,
                        G_Name_en,
                        F_Compare_InseeXls_CodeCommune_W_CodeCommune,
                        F_Compare_InseeXls_NameCommune_Wiki_Url,
                        F_Compare_InseeXls_NameCommune_G_Locality_long_name,
                        urllib.unquote(str(Wiki_UrlInCommuneSnipet)).decode('utf8'),
                        ClearName.Run(Wiki_NameSnipet),
                        urllib.unquote(str(Wiki_Old_UrlInCommune)).decode('utf8'),
                        ClearName.Run(Wiki_Old_NameSnipet),
                        ColResultInSnipet]

            DataInSaveFile = '{' + "'" + str(InseeXls_CodeCommune) + "':" + str(Data) + '}'
            text_file = open("../WorkBaseFile/29_06_17_base_Occitanie.txt", "a")
            text_file.write(str(DataInSaveFile) + '\n')


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