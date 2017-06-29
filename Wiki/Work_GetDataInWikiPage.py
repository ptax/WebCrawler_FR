# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')
import Wiki.GetDataInWikiTable
import Utils.SaveAndLoadDictFile
import time
import Utils.ConvertCordinates
class Profiler(object):
    def __enter__(self):
        self._startTime = time.time()

    def __exit__(self, type, value, traceback):
        print "Elapsed time: {:.3f} sec".format(time.time() - self._startTime)

if __name__ == '__main__':
    '''
        LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_WikiUrl_08_06_17')
        WorckDict = LoadMyDict.copy()

        listTest = ['60597','94047','60598','33064','75113','75112']
        for i in listTest:
            Data = WorckDict[i]
            UrlWiki = Data['Wiki_Url'].strip()
            CodeCommene = Data['InseeXls_CodeCommune']

            Url = 'https://fr.wikipedia.org' +  UrlWiki
            if 'Not Faund' in UrlWiki:
                print CodeCommene

                pass
            else:
                print Url,CodeCommene

                GetHtml = Wiki.GetDataInWikiTable.GetHtml(Url)

                Table = GetHtml[0]
                LangHref = GetHtml[1]

                DictTableInformation = Wiki.GetDataInWikiTable.GetInformation(Table)
                LanguagesDict = Wiki.GetDataInWikiTable.FilterLanguages(Wiki.GetDataInWikiTable.GetLanguages(LangHref))
                DictDatainWikiPage = DictTableInformation.copy()
                DictDatainWikiPage.update(LanguagesDict)
                WorckDict[CodeCommene].update(LanguagesDict)

        NameDict = '../WorkBaseFile/Dict_WikiPageData_09_06_17_2'
        Utils.SaveAndLoadDictFile.SaveDict(WorckDict,NameDict)
        print len(WorckDict)
    '''
    '''
    with Profiler() as p:
            LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_WikiPageData_09_06_17_2')
            listTest = ['60597','94047','60598','33064','75113','75112']
            print len(LoadMyDict)
            for i in listTest:
                print len(LoadMyDict[i])
                print LoadMyDict[i]
    '''

    with Profiler() as p:
        LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/Dict_WikiUrl_08_06_17')
        WorkDict = LoadMyDict.copy()
        c =0
        for data in WorkDict.values():
            c +=1

            WikiUrl = data['Wiki_Url'].strip()
            CodeCommene =data['InseeXls_CodeCommune'].strip()
            DataLog = str(c) + '\t' + str(CodeCommene) + '\t' + str(WikiUrl)
            print DataLog
            if 'Not Faund' in WikiUrl:
                pass
            else:

                Url = "https://fr.wikipedia.org" + WikiUrl
                GetHtml = Wiki.GetDataInWikiTable.GetHtml(Url)
                Table = GetHtml[0]
                LangHref = GetHtml[1]

                DictTableInformation = Wiki.GetDataInWikiTable.GetInformation(Table)

                LanguagesDict = Wiki.GetDataInWikiTable.FilterLanguages(Wiki.GetDataInWikiTable.GetLanguages(LangHref))

                DictDatainWikiPage = DictTableInformation.copy()
                DictDatainWikiPage.update(LanguagesDict)
                WorkDict[CodeCommene].update(DictDatainWikiPage)
                DataInSaveFile = '{' + "'"+  str(CodeCommene) + "':" + str(DictDatainWikiPage)  + '}'
                text_file = open("../WorkBaseFile/WikiDataPage_11_06_17_String_Dict.txt", "a")
                text_file.write(str(DataInSaveFile) +'\n')
        text_file.close()
        NameDict = '../WorkBaseFile/WikiDataPage_11_06_17'
        Utils.SaveAndLoadDictFile.SaveDict(WorkDict,NameDict)
        print len(WorkDict)

