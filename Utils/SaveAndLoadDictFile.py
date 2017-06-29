# -*- coding: utf-8 -*-
import sys

reload(sys)
sys.setdefaultencoding('utf-8')
import os
import pickle


def SaveDict(obj, FullName):
    FullName = os.path.abspath(FullName)
    with open(FullName + '.pkl', 'wb') as f:
        pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)


def LoadDict(FullName):
    with open(FullName + '.pkl', 'rb') as f:
        return pickle.load(f)