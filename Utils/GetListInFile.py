# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os


def Run(FilePathName):
    '''
        This is Utils Which converts files sting in list
        You put path in file and return list
    '''
    ListFile = open(os.path.abspath(FilePathName)).read().split('\n')
    ListFile = [x for x in ListFile if x]
    return ListFile


if __name__ == '__main__':
    NameFile = r'../Wiki/BaseCommune'
    for i in Run(NameFile):
        print i[0]