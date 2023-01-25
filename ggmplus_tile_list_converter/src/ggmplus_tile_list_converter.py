'''

This code aims to convert the GGMplus tile list to a DNRGPS format file (for polygon). So that we can convert it to *.kml, *.shp and etc.

by:
arif.darmawan@riflab.com
5 January 2023

'''


fo = open('GGMplus_tilelist_public.dat')
fw = open('GGMplus_tilelist_public_new.txt','w')


tilename = []
min_lat = []
max_lat = []
min_lon = []
max_lon = []
data_pts = []
no_data_pts = []

i = 0
while True:
    read = fo.readline()

    if i > 1:
        if read == '':
            break
        
        a = read.split("\n")[0].split(' ')
        a = list(filter(None, a))
        tilename.append(a[1])
        min_lat.append((a[2]))
        max_lat.append((a[3]))
        min_lon.append((a[4]))
        max_lon.append((a[5]))
        data_pts.append((a[6]))
        no_data_pts.append((a[7]))
    i+=1


fw.write('type' + '\t' + 'tident'+ '\t' +'ident'+ '\t' +'Latitude'+ '\t' +'Longitude'+ '\t' +'new_trk'+ '\t' +'new_seg' + '\n')
for i in range(len(tilename)):

    fw.write('TRACK'+ '\t' + tilename[i] + '\t' + tilename[i] + '\t' + max_lat[i] + '\t' +  max_lon[i] + '\t' + 'FALSE' + '\t' +'TRUE' + '\n')
    fw.write('TRACK'+ '\t' + tilename[i] + '\t' + tilename[i] + '\t' + min_lat[i] + '\t' +  max_lon[i] + '\t' + 'FALSE' + '\t' +'FALSE' + '\n')
    fw.write('TRACK'+ '\t' + tilename[i] + '\t' + tilename[i] + '\t' + min_lat[i] + '\t' +  min_lon[i] + '\t' + 'FALSE' + '\t' +'FALSE' + '\n')
    fw.write('TRACK'+ '\t' + tilename[i] + '\t' + tilename[i] + '\t' + max_lat[i] + '\t' +  min_lon[i] + '\t' + 'FALSE' + '\t' +'FALSE' + '\n')
    fw.write('TRACK'+ '\t' + tilename[i] + '\t' + tilename[i] + '\t' + max_lat[i] + '\t' +  max_lon[i] + '\t' + 'FALSE' + '\t' +'FALSE' + '\n')

fo.close()
fw.close()
