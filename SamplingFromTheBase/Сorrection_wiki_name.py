# -*- coding: utf-8 -*-

import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import Utils.SaveAndLoadDictFile
import re
from sets import Set
import Utils.ClearName


def countDuplicatesInList(dupedList):
    uniqueSet = Set(item for item in dupedList)
    return [(item, dupedList.count(item)) for item in uniqueSet]


def replace_name():
    LoadDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_UpdateCommune_5')
    WorkDict = LoadDict.copy()
    DataRe = {u"Provence-Alpes-Côte d'Azur": u"Provence-Alpes-Côte d’Azur",
              u"Rhône-Alpes": u"Auvergne-Rhône-Alpes",
              u"Champagne-Ardenne": u"Grand Est",
              u"Poitou-Charentes": u"Nouvelle-Aquitaine",
              u"Languedoc-Roussillon": u"Occitanie",
              u"Midi-Pyrénées": u"Occitanie",
              u"Lorraine": u"Grand Est",
              u"Nord-Pas-de-Calais": u"Hauts-de-France",
              u"Auvergne": u"Auvergne-Rhône-Alpes",
              u"Alsace": u"Bourgogne-Franche-Comté",
              u"Haute-Normandie": u"Normandie",
              u"Franche-Comté": u"Bourgogne-Franche-Comté"}

    c = 0
    list_err = []
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            W_Region = Data['W_Region']
        except:
            W_Region = 'None_Err'

        for GoogName, BadName in zip(DataRe.values(), DataRe.keys()):
            if W_Region == BadName:
                c += 1
                print c, Keys, W_Region, GoogName
                MyDate = {'W_Region': GoogName}

                WorkDict[Keys].update(MyDate)
        if W_Region == 'None_Err':
            list_err.append(Keys)
    print len(list_err)

    NameDict = '../WorkBaseFile/01_08_17_UpdateCommune_6'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, NameDict)


def up_status():
    LoadDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/01_08_17_UpdateCommune_4')
    WorkDict = LoadDict.copy()
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            W_Region = Data['W_Region']
        except:
            W_Region = 'None'

        looking_status = re.compile('\(.*\)')
        looking_status = looking_status.findall(W_Region)

        if looking_status:
            status = looking_status[0]
            clear_status = status.lower().replace('(', '').replace(')', '')
            W_Region = W_Region.replace(status, '').replace(u',', '').strip()
            DataUp = {'W_Region': W_Region, 'W_Region_status': clear_status}
            WorkDict[Keys].update(DataUp)
        else:
            DataUp = {'W_Region': W_Region.replace(',', '').strip(), 'W_Region_status': 'None'}
            WorkDict[Keys].update(DataUp)

        try:
            W_Departement = Data['W_Departement']
        except:
            W_Departement = 'None'

        looking_status = re.compile('\(.*\)')
        looking_status = looking_status.findall(W_Departement)

        if looking_status:
            status = looking_status[0]
            clear_status = status.lower().replace('(', '').replace(')', '')
            W_Departement = W_Departement.replace(status, '').replace(u',', '').strip()

            DataUp = {'W_Departement': W_Departement,
                      'W_Departement_status': clear_status.replace('sous préfecture', 'sous-préfecture')}
            WorkDict[Keys].update(DataUp)
        else:
            DataUp = {'W_Departement': W_Departement.replace(',', '').strip(), 'W_Departement_status': None}
            WorkDict[Keys].update(DataUp)

        try:
            W_Arrondissement = Data['W_Arrondissement']
        except:
            W_Arrondissement = 'None'

        looking_status = re.compile('\(.*\)')
        looking_status = looking_status.findall(W_Arrondissement)

        if looking_status:
            status = looking_status[0]
            clear_status = status.lower().replace('(', '').replace(')', '')
            W_Arrondissement = W_Arrondissement.replace(status, '').replace(u',', '').strip()
            DataUp = {'W_Arrondissement': Utils.ClearName.Run(W_Arrondissement),
                      'W_Arrondissement_status': clear_status.replace('sous préfecture', 'sous-préfecture').replace(
                          'chef lieu', 'chef-lieu')}
            WorkDict[Keys].update(DataUp)
        else:
            DataUp = {'W_Arrondissement': Utils.ClearName.Run(W_Arrondissement).replace(',', '').strip(),
                      'W_Arrondissement_status': None}
            WorkDict[Keys].update(DataUp)

        try:
            W_Canton = Data['W_Canton']
        except:
            W_Canton = 'None'
        if u'chef-lieu' in W_Canton:
            W_Canton = W_Canton.replace(u'(chef-lieu)', '')
            DataUp = {'W_Canton': W_Canton.strip(), 'W_Canton_status': u'chef-lieu'}
            WorkDict[Keys].update(DataUp)
        else:
            W_Canton = W_Canton.replace(u'(chef-lieu)', '')
            DataUp = {'W_Canton': W_Canton.strip(), 'W_Canton_status': u'None'}
            WorkDict[Keys].update(DataUp)

    NameDict = '../WorkBaseFile/01_08_17_UpdateCommune_5'
    Utils.SaveAndLoadDictFile.SaveDict(WorkDict, NameDict)


def stats():
    LoadDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/02_08_17_release')
    print len(LoadDict)
    WorkDict = LoadDict.copy()
    MyList = []
    StursList = []
    for Data, Keys in zip(WorkDict.values(), WorkDict.keys()):
        try:
            W_Region = Data['W_Departement']
            MyList.append(W_Region)
            StursList.append(Data['W_Region'])
        except:
            W_Region = None

    countDuplicatesInList(MyList)

    for i, b in countDuplicatesInList(MyList):
        data = '{0}\t{1}'.format(i, b)
        print data.decode('utf-8')

    print '==' * 20
    countDuplicatesInList(StursList)

    for i, b in countDuplicatesInList(StursList):
        data = '{0}\t{1}'.format(i, b)
        print data.decode('utf-8')


if __name__ == '__main__':
    # up_status()

    #replace_name()



    #replace_name()
    stats()


