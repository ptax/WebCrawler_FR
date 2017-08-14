#-*- coding: utf-8 -*-
#-----Import python lib -------------------------
import random,imaplib
import re
import time
import locale,os,time


from sets import Set

def countDuplicatesInList(dupedList):
   uniqueSet = Set(item for item in dupedList)
   return [(item, dupedList.count(item)) for item in uniqueSet]

content = '''


'''

lst = content.split('\n')


countDuplicatesInList(lst)

for i,b in countDuplicatesInList(lst):
    data = '{0}\t{1}'.format(i,b)
    print data.decode('utf-8')
