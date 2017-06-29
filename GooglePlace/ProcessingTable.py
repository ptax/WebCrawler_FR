

import os
import re

def ProcessingTable(FileName):
    ListTable =[]
    for DataFile in open(FileName):
        DictTable = {}
        DataFile = DataFile.split('$')
        if len(DataFile) == 16:
            ListTable.append(DataFile)
        elif len(DataFile) >= 17:
            ErrorTable =  '\t'.join(DataFile).strip(),'Err'




    for numComune in xrange(len(ListTable)):
        UrlCommune = ListTable[numComune][0]
        NameCommune = ListTable[numComune][1]
        CodeInsee = ListTable[numComune][2]
        CodePostal = ListTable[numComune][3]
        ArrondissementUrl = ListTable[numComune][4]
        ArrondissementName = ListTable[numComune][5]
        CantonUrl = ListTable[numComune][6]
        CantonName = ListTable[numComune][7]
        IntercommunaliteUrl = ListTable[numComune][8]
        IntercommunaliteName = ListTable[numComune][9]
        Superficie = ListTable[numComune][10].replace(',','.')
        Population = ListTable[numComune][11].replace(',','.')
        Densite = str(ListTable[numComune][12]).replace(',','.').replace(' ','').strip()
        Maire = ListTable[numComune][13]
        AltitudeMini = ListTable[numComune][14]
        AltitudeMax = ListTable[numComune][15]
        if '<br/>' in CodePostal:
            CodePostal = CodePostal.replace('<br/>',';')
        else:
            CodePostal = CodePostal

        if '<br/>' in CantonName:
            CanronRe = CantonUrl + ';' + ';'.join(CantonName.split('<br/>')),';'.join(IntercommunaliteUrl.split('<br/>')) + ';' + IntercommunaliteName
            #CanronRe = CanronRe[0].split(';')
            listURl = []
            listName = []
            for i in CanronRe:
                i = i.split(';')
                for b in i:
                     if 'wiki' in b:
                        listURl.append(b)
                     else:
                         b = b.replace(';','')
                         listName.append(b)

            CantonName = ';'.join(listName)
            CantonUrl = ';'.join(listURl)
            IntercommunaliteUrl = ListTable[numComune][10]
            IntercommunaliteName = ListTable[numComune][11]
            if 'wiki' in IntercommunaliteUrl:
                IntercommunaliteUrl = IntercommunaliteUrl
            if not 'wiki' in IntercommunaliteName:
                 IntercommunaliteName = IntercommunaliteName
            Superficie = ListTable[numComune][12].replace(',','.')
            Population = ListTable[numComune][13].replace(',','.').replace(' ','')

            Densite = ListTable[numComune][14].replace(',','.').replace(' ','')
            if not 'wiki' in Densite:
                Densite = Densite

            Maire = ListTable[numComune][15]
            if not 'wiki' in Maire:
                Maire = Maire
            AltitudeMini = ListTable[numComune][18]
            AltitudeMax = ListTable[numComune][16]
            data = UrlCommune + '\t' + NameCommune + '\t' + CodeInsee+ '\t' + CodePostal + '\t' + ArrondissementUrl + '\t' + ArrondissementName + '\t' + CantonUrl + '\t' + CantonName + '\t' + IntercommunaliteUrl + '\t' + IntercommunaliteName + '\t' + Superficie + '\t' + Population + '\t' + Maire + '\t' + AltitudeMini + '\t' + AltitudeMax + '\t' + UrlCommune + '\t' + NameCommune + '\t' + CodeInsee + '\t' + CodePostal + '\t' + ArrondissementUrl + '\t' + ArrondissementName + '\t' + CantonUrl + '\t' + CantonName + '\t' + IntercommunaliteUrl + '\t' + IntercommunaliteName + '\t' + Superficie + '\t' + Population + '\t' + Maire + '\t' + AltitudeMini + '\t' + AltitudeMax
            print data
        #print ListTable[numComune][2],CantonName,ListTable[numComune][6],ListTable[numComune][1]
        DictTable[numComune]={'UrlCommune':UrlCommune,
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
                                'AltitudeMax':AltitudeMax
            }
    return DictTable
'''
FileName = r'output_Liste_des_communes_du_Pas-de-Calais_t0.csv'
DictTable = ProcessingTable(FileName)
print DictTable
'''
'''
for NumDict in xrange(len(DictTable)):
    data = DictTable.get(NumDict).get('UrlCommune').strip() + '\t' + \
           DictTable.get(NumDict).get('NameCommune').strip() + '\t' + \
           DictTable.get(NumDict).get('CodeInsee').strip() + '\t' + \
           DictTable.get(NumDict).get('CodePostal').strip() + '\t' + \
           DictTable.get(NumDict).get('ArrondissementUrl').strip() + '\t' + \
           DictTable.get(NumDict).get('ArrondissementName').strip() + '\t' + \
           DictTable.get(NumDict).get('CantonUrl').strip() + '\t' + \
           DictTable.get(NumDict).get('CantonName').strip() + '\t' + \
           DictTable.get(NumDict).get('IntercommunaliteUrl').strip() + '\t' + \
           DictTable.get(NumDict).get('IntercommunaliteName').strip() + '\t' + \
           DictTable.get(NumDict).get('Superficie').strip() + '\t' + \
           DictTable.get(NumDict).get('Population').strip() + '\t' + \
           DictTable.get(NumDict).get('Densite').strip() + '\t' + \
           DictTable.get(NumDict).get('Maire').strip() + '\t' + \
           DictTable.get(NumDict).get('AltitudeMini').strip() + '\t' + \
           DictTable.get(NumDict).get('AltitudeMax').strip() + '\t'
    #print data
    #text_file = open("UrlPageWikiData.txt", "a")
    #text_file.write(data +'\n')
#text_file.close()

'''

'''



for LangDictValue in DictTable.values():
    print LangDictValue[2]
'''
