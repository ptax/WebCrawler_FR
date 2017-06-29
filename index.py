# -*- coding: utf-8 -*-


for file in open(r'coordinat'):
    Cordinat = file.split('\t')
    Cordinat_1 = Cordinat[0].strip()
    Cordinat_2 = Cordinat[1].strip()
    print Cordinat_2