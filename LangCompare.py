

# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
def GetList(FileName):
    ListMyData = []
    OpenDictFile = open(FileName).read().split('\n')
    for i in OpenDictFile:
        ListMyData.append(i.split('$'))
    return ListMyData





def GetLangDict(FileName):
    LangDict = {}
    for ListTable in FileName:
        if len(ListTable) !=1:
            CodeInsee =  ListTable[0]
            NameFR = ListTable[1]
            EnName = ListTable[2]
            DeName = ListTable[3]
            PlName = ListTable[3]
            EsName = ListTable[4]
            EnLog = ''
            DeLog = ''
            PlLog = ''
            EsLog = ''
            LangDict[CodeInsee] = {CodeInsee:
                                       {'CodeInsee':CodeInsee,
                                        'NameFR':NameFR,
                                        'EnName':EnName,
                                        'DeName':DeName,
                                        'PlName':PlName,
                                        'EsName':EsName,
                                        'EnLog':EnLog,
                                        'DeLog':EnLog,
                                        'PlLog':EnLog,
                                        'EsLog':EnLog,

                                        }
                                   }
    return LangDict

FileWikiLang = r'Lang_Compare.txt'
FileGoogleLang = open(r'Lang_Compare.txt').read().split('\n')




DictWiki = GetLangDict(GetList(FileWikiLang))
ListNumTrueEN = []
ListNumFalseEN = []
ListNumTrueDE = []
ListNumFalseDE = []
ListNumTruePL = []
ListNumFalsePL = []
ListNumTrueES = []
ListNumFalseES = []
for Lang in FileGoogleLang:
    Lang = Lang.split('$')


    if len(Lang) != 1:
        CodeInsee = str(Lang[0])
        NameFR = str(Lang[1]).lower()
        EnName = str(Lang[2]).lower()
        DeName = str(Lang[3]).lower()
        PlName = str(Lang[3]).lower()
        EsName = str(Lang[4]).lower()

        if DictWiki.has_key(CodeInsee) == True:
            for i in DictWiki.get(CodeInsee).items():
                if unicode(NameFR) == unicode(EnName):
                    LogError = {'EnLog':'True'}
                    i[1].update(LogError)
                    ListNumTrueEN.append(EnName)
                else:
                    LogError = {'EnLog':'False'}
                    i[1].update(LogError)
                    ListNumFalseEN.append(EnName)
                if unicode(NameFR) == unicode(DeName):
                    LogError = {'DeLog':'True'}
                    i[1].update(LogError)
                    ListNumTrueDE.append(DeName)
                else:
                    LogError = {'DeLog':'False'}
                    i[1].update(LogError)
                    ListNumFalseDE.append(DeName)
                if unicode(NameFR) == unicode(PlName):
                    LogError = {'PlLog':'True'}
                    i[1].update(LogError)
                    ListNumTruePL.append(PlName)
                else:
                    LogError = {'PlLog':'False'}
                    i[1].update(LogError)
                    ListNumFalsePL.append(PlName)
                if unicode(NameFR) == unicode(PlName):
                    LogError = {'EsLog':'True'}
                    i[1].update(LogError)
                    ListNumTrueES.append(EsName)
                else:
                    LogError = {'EsLog':'False'}
                    i[1].update(LogError)
                    ListNumFalseES.append(EsName)

print 'Name match EN \t' + str(len(ListNumTrueEN)) + '\t' + 'Name does not match EN \t' + str(len(ListNumFalseEN))
print 'Name match DE \t' + str(len(ListNumTrueDE)) + '\t' + 'Name does not match DE \t' + str(len(ListNumFalseDE))
print 'Name match PL \t' + str(len(ListNumTruePL)) + '\t' + 'Name does not match PL \t' + str(len(ListNumFalsePL))
print 'Name match ES \t' + str(len(ListNumTrueES)) + '\t' + 'Name does not match ES \t' + str(len(ListNumFalseES))



for i in DictWiki.items():
    MyData  = i[1].values()[0]
    Delimiter = '$'
    Data =  MyData.get('CodeInsee').strip() + str(Delimiter) + \
            MyData.get('NameFR').strip() + str(Delimiter) + \
            MyData.get('EnName').strip() + str(Delimiter) + \
            MyData.get('DeName').strip() + str(Delimiter) + \
            MyData.get('PlName').strip() + str(Delimiter)   + \
             MyData.get('EsName').strip() + str(Delimiter)  + \
             MyData.get('EnLog').strip() + str(Delimiter)   + \
             MyData.get('DeLog').strip() + str(Delimiter)   + \
             MyData.get('PlLog').strip() + str(Delimiter)   + \
             MyData.get('EsLog').strip() + str(Delimiter)
    print Data
