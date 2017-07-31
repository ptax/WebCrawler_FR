# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import re

from fuzzywuzzy import fuzz


def change_letter(word):
    word = word.lower()
    DictChangeLetter = {u'è': u'e',
                        u'é': u'e',
                        u'ë': u'e',
                        u'ê': u'e',
                        u"î": u"i",
                        u"û": u"u",
                        u"ô": u"o",
                        u"â": u"a",
                        u"ç": u"c",
                        u'é': u'e',
                        u'ï': u'i',
                        u'-': u' ',
                        u"'": u'',


                        }
    for key, items in DictChangeLetter.items():
        word = re.sub(key, items, word)
    return word


def comun_name_wiki_google_comparisons(Wiki_NameSnipet, G_Locality_short_name):
    Wiki_NameSnipet = change_letter(Wiki_NameSnipet)
    G_Locality_short_name = change_letter(G_Locality_short_name)
    if Wiki_NameSnipet == G_Locality_short_name:
        F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally = 'True'
    else:
        F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally = 'False'

    F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage = fuzz.ratio(Wiki_NameSnipet, G_Locality_short_name)

    if 80 <= F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage:
        F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80 = 'True'
    else:
        F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80 = 'None'

    DictCommunNameComparisons = {u'Wiki_NameSnipet_lower': change_letter(Wiki_NameSnipet),
                                 u'G_Locality_short_name_lower': change_letter(G_Locality_short_name),
                                 u'F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally': F_Compare_Wiki_NameSnipet_G_Locality_short_name_equally,
                                 u'F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage': F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage,
                                 u'F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80': F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80}
    return DictCommunNameComparisons


if __name__ == '__main__':
    Wiki_NameSnipet = (u"Saint Antoine l'Abbayeé chérisy")
    G_Locality_short_name = (u"Saint-Antoine-l'Abbaye chérisy")
    F_ComunName_Comprasions = comun_name_wiki_google_comparisons(Wiki_NameSnipet, G_Locality_short_name)
    print F_ComunName_Comprasions
    Wiki_NameSnipet_lower = F_ComunName_Comprasions['Wiki_NameSnipet_lower']
    G_Locality_short_name_lower = F_ComunName_Comprasions['G_Locality_short_name_lower']

    F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage = F_ComunName_Comprasions[
        'F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage']
    F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80 = F_ComunName_Comprasions[
        'F_Compare_Wiki_NameSnipet_G_Locality_short_name_percentage_more_or_equal_80']

