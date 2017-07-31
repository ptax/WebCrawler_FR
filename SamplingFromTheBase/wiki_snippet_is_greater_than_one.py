__author__ = 'alex'

import Utils.SaveAndLoadDictFile
import pandas

import os

if __name__ == '__main__':
    '''
    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/30_06_17_1')

    WorkDict = LoadMyDict.copy()

    c = 0
    MyDict  = {}
    MyList = []
    for Data in WorkDict.values():
        c +=1
        number_of_snippets = Data['ColResultInSnipet']
        CodeCommune = Data['InseeXls_CodeCommune']
        if number_of_snippets >= 2:
            print c,CodeCommune
            MyList.append(CodeCommune)
            MyDate = {CodeCommune:Data}
            MyDict.update(MyDate)

    NameDict = '../WorkBaseFile/03_07_17_TwoSnippetsInWili'
    Utils.SaveAndLoadDictFile.SaveDict(MyDict, NameDict)


    print len(MyDict)
    print len(MyList)
    '''

    LoadMyDict = Utils.SaveAndLoadDictFile.LoadDict('../WorkBaseFile/03_07_17_TwoSnippetsInWili')
    print len(LoadMyDict)
    # for Data in LoadMyDict.values():
    #print Data['InseeXls_CodeCommune'],Data['ColResultInSnipet'],Data['InseeXls_NameCommune'],Data['Wiki_NameSnipet'],Data['Wiki_Old_NameSnipet']
    FullName = r'../WorkBaseFile/03_07_17_TwoSnippetsInWili.pkl'
    FullName = os.path.abspath(FullName)
    WorkDict = pandas.read_pickle(FullName)
    index = 'W_Cordommees_Convert', 'W_Departement'
    test = pandas.DataFrame.from_dict(WorkDict, orient='index', dtype=None)
    print test