# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import os
import json


test = u"""{'W_Name_it': u'Saint-Val\xe9rien (Yonne)', 'W_Url_nl': u'https://nl.wikipedia.org/wiki/Saint-Val\xe9rien_', 'W_Name_ro': u'Saint-Val\xe9rien, Yonne', u'W_CodePostal': u'89150,', 'W_Name_pt': u'Saint-Val\xe9rien', 'W_Name_ru': '', 'W_Url_de': u'https://de.wikipedia.org/wiki/Saint-Val\xe9rien_', 'W_Url_da': u'', 'W_Name_pl': u'Saint-Val\xe9rien (Yonne)', 'W_Url_bg': u'', 'W_Url_sl': u'', u'W_Cordommees': u'48\xb0\xa010\u2032\xa048\u2033\xa0, 3\xb0\xa005\u2032\xa045\u2033\xa0,', 'W_Url_ro': u'https://ro.wikipedia.org/wiki/Saint-Val\xe9rien,_Yonne', 'W_Name_es': u'Saint-Val\xe9rien (Yonne)', 'W_Url_pl': u'https://pl.wikipedia.org/wiki/Saint-Val\xe9rien_', 'W_Name_cs': '', 'W_Url_hr': u'', u'W_Altitude': u'Min.\xa0137 m\xa0\u2013 Max.\xa0181 m,', u'W_CodeCommune': u'89370,', u'W_Region': u'Bourgogne-Franche-Comt\xe9,', 'W_Url_it': u'https://it.wikipedia.org/wiki/Saint-Val\xe9rien_', u'W_Intercommunalite': u'Communaut\xe9 de communes du G\xe2tinais en Bourgogne,', u'W_Superficie': u'22,31 km2,', 'W_Url_ru': u'', 'W_Url_pt': u'https://pt.wikipedia.org/wiki/Saint-Val\xe9rien', 'W_Name_en': u'Saint-Val\xe9rien, Yonne', 'W_Name_hr': '', 'W_Url_cs': u'', 'W_Url_es': u'https://es.wikipedia.org/wiki/Saint-Val\xe9rien_', 'W_Name_hu': u'Saint-Val\xe9rien (Yonne)', 'W_Name_sl': '', 'W_Name_uk': u"\u0421\u0435\u043d-\u0412\u0430\u043b\u0435\u0440'\u044f\u043d (\u0419\u043e\u043d\u043d\u0430)", 'W_Name_sk': u'Saint-Val\xe9rien (Yonne)', 'W_Name_no': '', 'W_Name_nl': u'Saint-Val\xe9rien (Yonne)', 'W_Name_sv': u'Saint-Val\xe9rien, Yonne', u'W_Arrondissement': u'Sens,', 'W_Name_sh': '', 'W_Url_en': u'https://en.wikipedia.org/wiki/Saint-Val\xe9rien,_Yonne', u'W_Population': u',1\xa0690 hab. (2014),', 'W_Url_sh': u'', 'W_Url_sk': u'https://sk.wikipedia.org/wiki/Saint-Val\xe9rien_', u'W_Canton': u'G\xe2tinais en Bourgogne,', 'W_Url_uk': u"https://uk.wikipedia.org/wiki/\u0421\u0435\u043d-\u0412\u0430\u043b\u0435\u0440'\u044f\u043d_", u'W_Pays': u'France,', 'W_Name_bg': '', u'W_Departement': u'Yonne,', 'W_Url_hu': u'https://hu.wikipedia.org/wiki/Saint-Val\xe9rien_', 'W_Url_sv': u'https://sv.wikipedia.org/wiki/Saint-Val\xe9rien,_Yonne', 'W_Name_de': u'Saint-Val\xe9rien (Yonne)', u'W_Densite': u'76 hab./km2,', 'W_Url_no': u'', 'W_Name_da': ''}"""
Dict =  eval(test)
print Dict['']
