# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os

import csv
import Utils.SaveAndLoadDictFile
import DataStructure.FirstColumHeader_1
import urllib
import re
import ClearName
import Utils.convert_to_latin
from Utils.distance_coordinates import haversine

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


def ConvertCSVFirstData():
    NameSaveFile = os.path.abspath('../WorkBaseFile/08_09_17_not_in_locality_Update.txt')
    HeaderLine = DataStructure.FirstColumHeader_1.GetHeader_2('\t')
    text_file = open(NameSaveFile, "a")
    text_file.write(HeaderLine + '\n')
    DictFile = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/08_09_17_not_in_locality_Update')
    print len(DictFile)

    w_rigion_mini = [u'Martinique', u'Guadeloupe']
    for Data, Keys in zip(DictFile.values(), DictFile.keys()):

        try:
            W_Region = Data['W_Region']
        except KeyError:
            W_Region = 'None'

        try:
            W_CodePostal = str(Data['W_CodePostal']).replace(',', '')
        except:
            W_CodePostal = 'None'
            pass
        try:
            G_postal_code_short_name = str(Data['G_postal_code_short_name'])
        except:
            G_postal_code_short_name = 'None'
        try:
            G_Types = str(Data['G_Types'])
        except:
            G_Types = 'None'

        if W_Region:
            # print DictFile[Keys]
            #print Data['InseeXls_CodeCommune']
            try:
                ColResultInSnipet = Data['ColResultInSnipet']
            except:
                ColResultInSnipet = 'None'
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

                F_ComunName_Comprasions = Utils.convert_to_latin.comun_name_wiki_google_comparisons(
                    ClearName.Run(Wiki_NameSnipet), G_Locality_short_name)
                Wiki_NameSnipet_lower = F_ComunName_Comprasions['Wiki_NameSnipet_lower']
                G_Locality_short_name_lower = F_ComunName_Comprasions['G_Locality_short_name_lower']
                F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally = F_ComunName_Comprasions[
                    'F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally']
                F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage = F_ComunName_Comprasions[
                    'F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage']
                F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80 = F_ComunName_Comprasions[
                    'F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80']

            except:
                Wiki_NameSnipet_lower = 'None'
                G_Locality_short_name_lower = 'None'
                F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage = 'None'
                F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80 = 'None'

            try:
                W_Departement_status = Data['W_Departement_status']
            except:
                W_Departement_status = 'None'

            try:
                W_Arrondissement_status = Data['W_Arrondissement_status']
            except:
                W_Arrondissement_status = 'None'

            try:
                W_Canton_status = Data['W_Canton_status']
            except:
                W_Canton_status = 'None'

            try:
                W_cord = W_Cordommees_Convert.split(',')
                Distance = round(haversine(float(W_cord[0]), float(W_cord[1]), float(G_Coordinates_location_Lat_3),
                                           float(G_Coordinates_location_Lng_3)), 2)
            except:
                Distance = False

            gen_address = str(InseeXls_NameCommune).strip() + ',' + str(W_Region).strip() + ',' + str(
                W_Departement).strip() + ',' + 'France'
            gen_address = gen_address.replace(' ', '-')
            Google_Link_NP_Name = 'https://www.google.com.ua/maps/place/' + str(gen_address)
            Google_Ling_Search_Coordinates = 'https://www.google.com.ua/search?site=&source=hp&q=' + str(
                G_Coordinates_location_Lat_3) + '%2C' + str(G_Coordinates_location_Lng_3)
            Google_Link_Distance = "https://www.google.com.ua/maps/dir/'" + str(W_Cordommees_Convert) + "'/'" + str(
                G_Coordinates_location_Lat_3) + ',' + str(G_Coordinates_location_Lng_3) + "'/@12z/"



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

                        F_Compare_InseeXls_CodeCommune_W_CodeCommune,
                        F_Compare_InseeXls_NameCommune_Wiki_Url,
                        F_Compare_InseeXls_NameCommune_G_Locality_long_name,
                        urllib.unquote(str(Wiki_UrlInCommuneSnipet)).decode('utf8'),
                        ClearName.Run(Wiki_NameSnipet),
                        urllib.unquote(str(Wiki_Old_UrlInCommune)).decode('utf8'),
                        ClearName.Run(Wiki_Old_NameSnipet),
                        ColResultInSnipet,
                        Wiki_NameSnipet_lower,
                        G_Locality_short_name_lower,
                        F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally,
                        F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage,
                        F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80,
                        W_Departement_status,
                        W_Arrondissement_status,
                        W_Canton_status,
                        Distance,
                        Google_Link_NP_Name,
                        Google_Ling_Search_Coordinates,
                        Google_Link_Distance
                        ]

            #DataInSaveFile = '{' + "'" + str(InseeXls_CodeCommune) + "':" + str(Data) + '}'
            #text_file = open("../WorkBaseFile/16_07_17.txt", "a")
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