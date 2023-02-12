'''

This code aims to convert the GGMplus tile list to a DNRGPS format file (for polygon). So that we can convert it to *.kml, *.shp and etc.

by:
arif.darmawan@riflab.com
5 January 2023

'''

import simplekml

def draw(coordenate, name='l'):
    for i in range(len(name)):
        pol = kml.newpolygon(name=name[i])
        pol.outerboundaryis = coordenate[i]
        pol.style.polystyle.color = 'ffffff'
        pol.style.polystyle.outline = 1

def read_data(path):
    coordenate = []
    name = []
    i = 0
    while True:
        read = fo.readline()

        if i > 1:
            if read == '':
                break
            
            a = read.split("\n")[0].split(' ')
            a = list(filter(None, a))

            b = [
                (a[4], a[3]),
                (a[5], a[3]), 
                (a[5], a[2]), 
                (a[4], a[2]), 
                (a[4], a[3])
                ]

            coordenate.append(b)
            name.append(a[1])
        i+=1
    
    return coordenate, name


kml = simplekml.Kml()

# fo = open('../data/SRTM2gravity_tilelist_public.dat')
fo = open('../data/GGMplus_tilelist_public.dat')
fw = '../kml/test2.kml'

coordenate, name = read_data(fo)

draw(coordenate, name)
kml.save(fw)