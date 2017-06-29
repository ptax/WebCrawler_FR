
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import Utils.GetListInFile

import Utils.SaveAndLoadDictFile

def DictCommuneInsee(ListDataInInseeXls):
    '''
        Return Dict Format Structure in data in file Code Insee in insee.fr
        You put list in tree colum and dict return
    '''


    DictCommuneInsee = {}
    for data in ListDataInInseeXls:
        data = data.split('\t')
        InseeXls_CodeCommune = str(data[0]).strip()
        InseeXls_NameCommune = str(data[1]).strip()
        InseeXls_Population = str(data[2]).strip()
        DictCommuneInsee[InseeXls_CodeCommune] = {'InseeXls_CodeCommune':InseeXls_CodeCommune,
                                                  'InseeXls_NameCommune':InseeXls_NameCommune,
                                                  'InseeXls_Population':InseeXls_Population,
                                                  'Wiki_Url':''
                                                  }
    return DictCommuneInsee

if __name__ == '__main__':
    CodeCommune = '01039'
    #print GetUrlCommune(CodeCommune)
    NameFile = r'../Wiki/BaseCommune'
    Mydata = Utils.GetListInFile.Run(NameFile)
    Mydict =  DictCommuneInsee(Mydata)
    Mydict['01004'].update({'dada':'1221'})
    #print Mydict
    NameDict = '../Utils/TestDict'
    #Utils.WorkDict.save_obj(Mydict,NameDict)
    MyDict = Utils.SaveAndLoadDictFile.load_obj(NameDict)
    for i in MyDict.values():
        print i
