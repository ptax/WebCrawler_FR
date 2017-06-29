

# -*- coding: utf-8 -*-

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
            LangName = ListTable[1]
            NewLangName = ''
            LogError = ''
            LangDict[CodeInsee] = {CodeInsee:
                                       {'CodeInsee':CodeInsee,
                                        'LangName':LangName,
                                        'NewLangName':NewLangName,
                                        'LogError':LogError

                                        }
                                   }
    return LangDict

FileWikiLang = r'Lang_ru.txt'
FileGoogleLang = open(r'Lang_Ru_Google.txt').read().split('\n')

DictWiki = GetLangDict(GetList(FileWikiLang))
ListNumTrue = []
ListNumFalse = []
for Lang in FileGoogleLang:
    Lang = Lang.split('$')


    if len(Lang) != 1:
        CodeInsee = str(Lang[0])
        UpdateData = {'NewLangName':str(Lang[1])}
        if DictWiki.has_key(CodeInsee) == True:
            for i in DictWiki.get(CodeInsee).items():
                i[1].update(UpdateData)
                LangName = str(i[1]['LangName']).decode('utf-8')
                NewLangName = str(Lang[1]).decode('utf-8')
                if unicode(LangName).lower() == unicode(NewLangName).lower():
                    LogError = {'LogError':'True'}
                    i[1].update(LogError)
                    ListNumTrue.append(LangName)
                else:
                    LogError = {'LogError':'False'}
                    i[1].update(LogError)
                    ListNumFalse.append(LangName)
print 'TRUE \t' + str(len(ListNumTrue)) + '\t' + 'False \t' + str(len(ListNumFalse))
for i in DictWiki.items():
    MyData  = i[1].values()[0]
    Delimiter = '$'
    Data =  MyData.get('CodeInsee').strip() + str(Delimiter) + \
            MyData.get('LangName').strip() + str(Delimiter) + \
            MyData.get('NewLangName').strip() + str(Delimiter) + \
            MyData.get('LogError').strip() + str(Delimiter)
    print Data