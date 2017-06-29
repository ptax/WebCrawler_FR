# -*- coding: utf-8 -*-

import os
import re



def GetList(FileName):
    ListMyData = []
    OpenDictFile = open(FileName).read().split('\n')
    for i in OpenDictFile:
        ListMyData.append(i.split('$'))
    return ListMyData

def GenDict(FileList):


    DictTable = {}

    for ListTable in FileList:
            if len(ListTable) !=1:
                UrlCommune = ListTable[0]
                NameCommune = ListTable[1]
                CodeInsee = ListTable[2]
                CodePostal = ListTable[3]
                ArrondissementUrl = ListTable[4]
                ArrondissementName = ListTable[5]
                CantonUrl = ListTable[6]
                CantonName = ListTable[7]
                IntercommunaliteUrl = ListTable[8]
                IntercommunaliteName = ListTable[9]
                Superficie = ListTable[10]
                Population = ListTable[11]
                Densite = ListTable[12]
                Maire = ListTable[13]
                AltitudeMini = ListTable[14]
                AltitudeMax = ListTable[15]
                CodeCommunePage = ListTable[16]
                Coordinates_1 = ListTable[17]
                Coordinates_2 = ListTable[18]
                PopulationPage = ListTable[19]
                RuName = ListTable[20]
                RuUrl = ListTable[21]
                UkName  = ListTable[22]
                UkUrl = ListTable[23]
                EnName = ListTable[24]
                EnUrl = ListTable[25]
                DeName = ListTable[26]
                DeUrl = ListTable[27]
                PlName = ListTable[28]
                PlUrl = ListTable[29]
                EsName = ListTable[30]
                EsUrl = ListTable[31]
                PtName = ListTable[32]
                PtUrl = ListTable[33]
                ItName = ListTable[34]
                ItUrl = ListTable[35]
                NlName = ListTable[36]
                NlUrl = ListTable[37]
                DaName = ListTable[38]
                DaUrl = ListTable[39]
                NoName = ListTable[40]
                NoUrl = ListTable[41]
                SvName = ListTable[42]
                SvUrl = ListTable[43]
                CsName = ListTable[44]
                CsUrl = ListTable[45]
                RoName = ListTable[46]
                RoUrl = ListTable[47]
                BgName = ListTable[48]
                BgUrl = ListTable[49]
                HuName = ListTable[50]
                HuUrl = ListTable[51]
                SkName = ListTable[52]
                SkUrl = ListTable[53]
                SlName = ListTable[54]
                SlUrl = ListTable[55]
                ShName = ListTable[56]
                ShUrl = ListTable[57]
                HrName = ListTable[58]
                HrUrl = ListTable[59]
                DictTable[CodeInsee]={CodeInsee :{'UrlCommune':UrlCommune,
                                            'NameCommune':NameCommune,
                                            'CodeInsee':CodeInsee,
                                            'CodePostal':CodePostal,
                                            'ArrondissementUrl':ArrondissementUrl,
                                            'ArrondissementName':ArrondissementName,
                                            'CantonUrl':CantonUrl,
                                            'CantonName':CantonName,
                                            'IntercommunaliteUrl':IntercommunaliteUrl,
                                            'IntercommunaliteName':IntercommunaliteName,
                                            'Superficie':Superficie,
                                            'Population':Population,
                                            'Densite':Densite,
                                            'Maire':Maire,
                                            'AltitudeMini':AltitudeMini,
                                            'AltitudeMax':AltitudeMax,
                                            'CodeCommunePage':CodeCommunePage,
                                            'Coordinates_1':Coordinates_1,
                                            'Coordinates_2':Coordinates_2,
                                            'PopulationPage':PopulationPage,
                                            'RuName':RuName,
                                            'RuUrl':RuUrl,
                                            'UkName':UkName,
                                            'UkUrl':UkUrl,
                                            'EnName':EnName,
                                            'EnUrl':EnUrl,
                                            'DeName':DeName,
                                            'DeUrl':DeUrl,
                                            'PlName':PlName,
                                            'PlUrl':PlUrl,
                                            'EsName':EsName,
                                            'EsUrl':EsUrl,
                                            'PtName':PtName,
                                            'PtUrl':PtUrl,
                                            'ItName':ItName,
                                            'ItUrl':ItUrl,
                                            'NlName':NlName,
                                            'NlUrl':NlUrl,
                                            'DaName':DaName,
                                            'DaUrl':DaUrl,
                                            'NoName':NoName,
                                            'NoUrl':NoUrl,
                                            'SvName':SvName,
                                            'SvUrl':SvUrl,
                                            'CsName':CsName,
                                            'CsUrl':CsUrl,
                                            'RoName':RoName,
                                            'RoUrl':RoUrl,
                                            'BgName':BgName,
                                            'BgUrl':BgUrl,
                                            'HuName':HuName,
                                            'HuUrl':HuUrl,
                                            'SkName':SkName,
                                            'SkUrl':SkUrl,
                                            'SlName':SlName,
                                            'SlUrl':SlUrl,
                                            'ShName':ShName,
                                            'ShUrl':ShUrl,
                                            'HrName':HrName,
                                            'HrUrl':HrUrl
                                    }}
    return DictTable










FileName = r'base/11_05_17.txt'

LangFile = open(r'Lang_DE.txt').read().split('\n')





FileList = GetList(FileName)
DictTable =  GenDict(FileList)



for Lang in LangFile:
    Lang = Lang.split('$')
    if len(Lang) != 1:
        CodeInsee = str(Lang[0])
        UpdateData = {'DeName':str(Lang[1])}
        if DictTable.has_key(CodeInsee) == True:
            for i in DictTable.get(CodeInsee).items():
                i[1].update(UpdateData)



'''Save File '''
for i in DictTable.items():
    MyData  = i[1].values()[0]
    Delimiter = '$'
    Data =  MyData.get('UrlCommune').strip() + str(Delimiter) + \
            MyData.get('NameCommune').strip() + str(Delimiter) + \
            MyData.get('CodeInsee').strip() + str(Delimiter) + \
            MyData.get('CodePostal').strip() + str(Delimiter) + \
            MyData.get('ArrondissementUrl').strip() + str(Delimiter) + \
            MyData.get('ArrondissementName').strip() + str(Delimiter) + \
            MyData.get('CantonUrl').strip() + str(Delimiter) + \
            MyData.get('CantonName').strip() + str(Delimiter) + \
            MyData.get('CantonName').strip() + str(Delimiter) + \
            MyData.get('IntercommunaliteName').strip() + str(Delimiter) + \
            MyData.get('Superficie').strip() + str(Delimiter) + \
            MyData.get('Population').strip() + str(Delimiter) + \
            MyData.get('Densite').strip() + str(Delimiter) + \
            MyData.get('Maire').strip() + str(Delimiter) + \
            MyData.get('AltitudeMini').strip() + str(Delimiter) + \
            MyData.get('AltitudeMax').strip() + str(Delimiter) + \
            MyData.get('CodeCommunePage').strip() + str(Delimiter) + \
            MyData.get('Coordinates_1').strip() + str(Delimiter) + \
            MyData.get('Coordinates_2').strip() + str(Delimiter) + \
            MyData.get('PopulationPage').strip() + str(Delimiter) + \
            MyData.get('RuName').strip() + str(Delimiter) + \
            MyData.get('RuUrl').strip() + str(Delimiter) + \
            MyData.get('UkName').strip() + str(Delimiter) + \
            MyData.get('UkUrl').strip() + str(Delimiter) + \
            MyData.get('EnName').strip() + str(Delimiter) + \
            MyData.get('EnUrl').strip() + str(Delimiter) + \
            MyData.get('DeName').strip() + str(Delimiter) + \
            MyData.get('DeUrl').strip() + str(Delimiter) + \
            MyData.get('PlName').strip() + str(Delimiter) + \
            MyData.get('PlUrl').strip() + str(Delimiter) + \
            MyData.get('EsName').strip() + str(Delimiter) + \
            MyData.get('EsUrl').strip() + str(Delimiter) + \
            MyData.get('PtName').strip() + str(Delimiter) + \
            MyData.get('PtUrl').strip() + str(Delimiter) + \
            MyData.get('ItName').strip() + str(Delimiter) + \
            MyData.get('ItUrl').strip() + str(Delimiter) + \
            MyData.get('NlName').strip() + str(Delimiter) + \
            MyData.get('NlUrl').strip() + str(Delimiter) + \
            MyData.get('DaName').strip() + str(Delimiter) + \
            MyData.get('DaUrl').strip() + str(Delimiter) + \
            MyData.get('NoName').strip() + str(Delimiter) + \
            MyData.get('NoUrl').strip() + str(Delimiter) + \
            MyData.get('SvName').strip() + str(Delimiter) + \
            MyData.get('SvUrl').strip() + str(Delimiter) + \
            MyData.get('CsName').strip() + str(Delimiter) + \
            MyData.get('CsUrl').strip() + str(Delimiter) + \
            MyData.get('RoName').strip() + str(Delimiter) + \
            MyData.get('RoUrl').strip() + str(Delimiter) + \
            MyData.get('BgName').strip() + str(Delimiter) + \
            MyData.get('BgUrl').strip() + str(Delimiter) + \
            MyData.get('HuName').strip() + str(Delimiter) + \
            MyData.get('HuUrl').strip() + str(Delimiter) + \
            MyData.get('SkName').strip() + str(Delimiter) + \
            MyData.get('SkUrl').strip() + str(Delimiter) + \
            MyData.get('SlName').strip() + str(Delimiter) + \
            MyData.get('SlUrl').strip() + str(Delimiter) + \
            MyData.get('ShName').strip() + str(Delimiter) + \
            MyData.get('ShUrl').strip() + str(Delimiter) + \
            MyData.get('HrName').strip() + str(Delimiter) + \
            MyData.get('HrUrl').strip() + str(Delimiter)
    print Data
    text_file = open("base/UpdataData.txt", "a")
    text_file.write(Data +'\n')
text_file.close()


'''
for DictFile in OpenDictFile:

    DictFile = DictFile.split('$')
    if len(DictFile) != 1:
        CodeInseeDict = DictFile[2]

        for Lang in LangFile:
            Lang = Lang.split('$')
            if len(Lang) != 1:
                CodeInseeLang = Lang[0]
                LangName = Lang[1]
                if CodeInseeLang == CodeInseeDict:
                    print CodeInseeLang,LangName,DictFile[1],CodeInseeDict
'''