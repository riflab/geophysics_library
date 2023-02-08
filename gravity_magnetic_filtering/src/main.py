import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import rasterio
from scipy.interpolate import griddata
from rasterio.transform import Affine
from rasterio.crs import CRS
import interpies

data_file = '../data/data.xlsx'
file_output = 'patuha_grav.tiff'

df = pd.read_excel(data_file, header=0)

points = list(zip(df['X'], df['Y']))
values = df['CBA_2.20'].values

min_x = df['X'].min()
max_x = df['X'].max()
min_y = df['Y'].min()
max_y = df['Y'].max()

res1 = (max_x - min_x)/1000
res2 = (max_y - min_y)/1000

xrange = np.arange(min_x, max_x + res1, res1)
yrange = np.arange(min_y, max_y + res2, res2)
gridx, gridy = np.meshgrid(xrange, yrange)
grid_grav = griddata(points, values, (gridx, gridy), method='cubic', fill_value=np.nan)

mask = (gridx > 768400) & (gridy > 9206800)
grid_grav[mask] = np.nan

mask = (gridx > 770300) & (gridy > 9206300)
grid_grav[mask] = np.nan

mask = (gridx < 763700) & (gridy < 9209300)
grid_grav[mask] = np.nan

fig, ax = plt.subplots()
im = ax.imshow(grid_grav, extent=(min_x, max_x, min_y, max_y), origin='lower')
ax.plot(df['X'], df['Y'], 'bo')
ax.ticklabel_format(useOffset=False, style='plain')

rasterCRS = CRS.from_epsg(32748)
transform = Affine.translation(gridx[0][0]-res1/2, gridy[0][0]-res2/2)*Affine.scale(res1, res2)

rasterfile = rasterio.open(
                            file_output, 'w', 
                            driver='GTiff',
                            dtype=grid_grav.dtype, 
                            count=1, 
                            width=grid_grav.shape[1], 
                            height=grid_grav.shape[0],
                            transform=transform,
                            crs=rasterCRS
                        )

rasterfile.write(grid_grav, indexes=1)
rasterfile.close()

grid1 = interpies.open(file_output)
ax1 = grid1.show(cmap_norm='equalize', contours=True)
# ax1.plot(df['X'], df['Y'], 'bo')
# ax.invert_xaxis()
ax1.invert_yaxis()
ax1.ticklabel_format(useOffset=False, style='plain')
