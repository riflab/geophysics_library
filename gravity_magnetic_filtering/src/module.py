# import matplotlib.pyplot as plt
# from matplotlib.pyplot import figure
import numpy as np
import rasterio
from scipy.interpolate import griddata
from rasterio.transform import Affine
from rasterio.crs import CRS
import interpies
from module_mask import mask_area2

def create_grid(i, df, file_output, X='Longitude', Y='Latitude', epsg=4326, name='Title', masking=False):
    points = list(zip(df[X], df[Y]))
    values = df[i].values
    # print(points, i)
    
    min_x = df[X].min()
    max_x = df[X].max()
    min_y = df[Y].min()
    max_y = df[Y].max()
    # print(min_x, max_x, min_y, max_y)

    res1 = (max_x - min_x)/1000
    res2 = (max_y - min_y)/1000

    xrange = np.arange(min_x, max_x + res1, res1)
    yrange = np.arange(min_y, max_y + res2, res2)
    gridx, gridy = np.meshgrid(xrange, yrange)
    
    grid_grav = griddata(points, values, (gridx, gridy), method='cubic', fill_value=np.nan, rescale=True)

    # if masking == True:
    grid_grav = mask_area2(grid_grav, gridx, gridy)
    
    # fig, ax = plt.subplots(figsize=(10, 10))
    # # im = ax.imshow(grid_grav, extent=(min_x, max_x, min_y, max_y), origin='lower')
    # ax.plot(df[X], df[Y], color='black', linestyle='None', marker='+', markersize=5, alpha=1)
    # set_map(ax, frame=True, dxdy=0.01)

    rasterCRS = CRS.from_epsg(epsg) #32748
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
    
    return grid1

def set_map(ax, frame=True, dxdy=2000):
    ax.invert_yaxis()
    # ax.set_box_aspect(1)
    ax.ticklabel_format(useOffset=False, style='plain')

    ax.xaxis.label.set_fontsize(10)
    ax.yaxis.label.set_fontsize(10)
    # ax.set_xlabel('Easting')
    # ax.set_ylabel('Northing')
    ax.set_xlabel('Longitude')
    ax.set_ylabel('Latitude')
    ax.tick_params(axis='x', labelsize=8, rotation=0)
    ax.tick_params(axis='y', labelsize=8, rotation=0)

    # start, end = ax.get_xlim()
    # print(start, end)
    # start = (round(start, -3))
    # ax.xaxis.set_ticks(np.arange(start, end, dxdy))
    
    # start, end = ax.get_ylim()
    # print(start, end)
    # start = (round(start, -3))
    # ax.yaxis.set_ticks(np.arange(start, end, dxdy))

    # PTH A
    # ax.set_xlim(107.370, 107.470)
    # ax.set_ylim(-7.20, -7.130)

    # PTH B
    # ax.set_xlim(107.210, 107.760)
    # ax.set_ylim(-7.45, -7.00)

    # PTH C
    # ax.set_xlim(107.050, 108.100)
    # ax.set_ylim(-7.750, -6.700)

    # CAN A
    ax.set_xlim(109.800, 109.88)
    ax.set_ylim(-7.22, -7.13)

    # CAN B
    # ax.set_xlim(109.775, 109.975)
    # ax.set_ylim(-7.29, -7.11)

    if frame == False:
        ax.spines['top'].set_visible(False)
        ax.spines['right'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        ax.get_xaxis().set_ticks([])
        ax.get_yaxis().set_ticks([])
        ax.set_xlabel('')
        ax.set_ylabel('')

def plot_demnas(path, df, X='Longitude', Y='Latitude', station=True):

    grid1 = interpies.open(path)
    ax1 = grid1.smooth(method='SG', deg=1, win=21, doEdges=True, sigma=1)
    ax1 = ax1.show(
                    cmap_norm='equalize', 
                    # contours=25,
                    # cb_contours=True, 
                    azdeg=315, altdeg=45, 
                    title='Topography',
                    zf=1,
                    figsize=(10, 10),
                    cmap='parula',
                    alpha=0.0, 
                    hs_contrast=1,
                    )
    ax1.invert_yaxis()
    set_map(ax1, frame=True, dxdy=0.01)

    if station == True:
        ax1.plot(df[X], df[Y], color='black', linestyle='None', marker='+', markersize=1, alpha=0.5)