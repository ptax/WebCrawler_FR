# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os


def dict_data_card(data):
    pass


test = '''
{{Infobox Canton de France
| nom           = Canton d'Aix-en-Provence-1
| rég           = [[Provence-Alpes-Côte d'Azur]]
| dépt          = [[Bouches-du-Rhône]]
| arrt          = [[Arrondissement d'Aix-en-Provence|Aix-en-Provence]]
| nbcomm        = fraction Aix-en-Provence
| insee         = 13 01
| binome        = Jean-Pierre Bouvet<br/>Brigitte Devesa
| population    = {{Dernière population de canton de France||1301}}<!-- Insertion automatique, ne pas modifier -->
| année_pop     = {{Dernière population de canton de France|date|1301}}<!-- Insertion automatique, ne pas modifier -->
| superficie    =
| bureau        = [[Aix-en-Provence]]
| dates         = [[2015]]-[[2021]]
| imageloc      = Canton Aix-en-Provence 1 (2014).svg
| date de création = 22 mars 2015<ref name="Décret2014"/>
}}
'''

if __name__ == '__main__':
    list = test.split('\n')
    print list
    genList = []
    for i in list:
        if '|' in i:
            i = i.strip()
            razd = i.split('=')
            # print razd[0]
            key = razd[0].replace('|', '').strip()
            content = razd[1].strip()
            print key, content

            genList.append(i)

    print genList
