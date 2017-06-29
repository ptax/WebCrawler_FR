
# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

import os
'''
NameMyFile = 'Forec_Bois.txt'
SaveFileName = 'Foret_Boois_02_06_17.txt'
SaveFilePath =  os.path.abspath('../BasePlaces/' + str(SaveFileName))
PathFile = os.path.abspath('../BasePlaces/' + str(NameMyFile))
'''

'''
ListMydata = open(PathFile).read().split('\n')
ListMydata = [x for x in ListMydata if x]



MyDict = {}
for i in ListMydata:
    PlaceId = i.split('\t')[13].strip()
    MyDict[PlaceId] = i



print len(ListMydata)
print len(MyDict)


for mydata in MyDict.values():
    text_file = open(SaveFilePath, "a")
    text_file.write(mydata +'\n')
text_file.close()


print len(ListMydata)
print len(MyDict)

'''
'''
    Del Object Dublicate in old files
'''

'''

NameMyFile = 'Plage_2.txt'
SaveFileName = 'Foret_Boois_02_06_17.txt'
SaveFilePath =  os.path.abspath('../BasePlaces/' + str(SaveFileName))
PathFile = os.path.abspath('../BasePlaces/' + str(NameMyFile))
'''

NameChengeFile = os.path.abspath('../BasePlaces/Lack_name_07_06_17.txt')



NameRemoveFile =  os.path.abspath('../BasePlaces/Lack.txt')


NameSaveFile = os.path.abspath('../BasePlaces//Lack_name_07_06_17_.txt')


ListCheckPlaceIdToRemove = open(NameRemoveFile).read().split('\n')
ListCheckPlaceIdToRemove = [x for x in ListCheckPlaceIdToRemove if x]
ListMyDataFile = open(NameChengeFile).read().split('\n')
ListMyDataFile = [x for x in ListMyDataFile if x]


DictFileDelId = {}
for i in ListCheckPlaceIdToRemove:
    PlaceId = i.split('\t')[13].strip()
    DictFileDelId[PlaceId] = PlaceId

DictMyFiles = {}
for i in ListMyDataFile:
    PlaceId = i.split('\t')[13].strip()
    DictMyFiles[PlaceId] = i

for KeyPlace in DictFileDelId.values():
    try:
        del DictMyFiles[KeyPlace]
    except:
        pass


for i in DictMyFiles.values():
    text_file = open(NameSaveFile, "a")
    text_file.write(i +'\n')
text_file.close()


print 'DictFileDelId + \t' + str(len(DictFileDelId))
print 'ListMyDataFile + \t' + str(len(DictMyFiles))
print 'DictMyFiles + \t' + str(len(DictMyFiles))