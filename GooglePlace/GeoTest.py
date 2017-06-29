# -*- coding: utf-8 -*-

import pyproj



'''Centralinaya tocha'''
latl,longl = (50.426857, 30.237472)

geod = pyproj.Geod(ellps="WGS84")
distance = float(40*100)
'''Vniz - 255 gradusov
    Pravo - 0 ili 360 gradusov
    Vverh = 451
    Levo = 900
'''
angle = 255
newLat,newLong,invAngle = geod.fwd(latl,longl,angle, distance)
print("Cordinat Metro Micakya : {0}, {1}".format(latl, longl))

print(u"Кординаты точки в {:.2f} км. к западу от метро минская".format(distance/1000.0) + ": {0}, {1}".format(newLat, newLong))


lat2,long2 = (50.512223, 30.4923271403)
niz1,niz2 = (50.5071923029, 30.495669888)



geod = pyproj.Geod(ellps="WGS84")
anglel,angle2,distance = geod.inv(longl, latl, long2, lat2)

print distance/2
#print("{:0.2f}".format(distance))
#print("{:0.2f}".format(npts2))

'''
Centr= (50.507344, 30.498713) #GdeToTut
tochaALevoVerh = (50.528755, 30.484490)
tochaBLevoNiz = (50.492178, 30.483235)
TochaVPravoNoc = (50.490847, 30.522765)
TocchaGPravoVerh = (50.528755, 30.517536)
'''