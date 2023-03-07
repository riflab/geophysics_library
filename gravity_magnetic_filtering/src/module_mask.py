import numpy as np

def mask_area(grid_grav, gridx, gridy):
    # mask = (gridx > 768400) & (gridy > 9206800)
    # grid_grav[mask] = np.nan

    # mask = (gridx > 770300) & (gridy > 9206300)
    # grid_grav[mask] = np.nan

    # mask = (gridx < 763700) & (gridy < 9209300)
    # grid_grav[mask] = np.nan

    # mask = (gridx > 767300) & (gridy > 9209500)
    # grid_grav[mask] = np.nan

    return grid_grav

def mask_area2(grid_grav, gridx, gridy):
    mask = (gridx > 107.43021) & (gridy > -7.16952)
    grid_grav[mask] = np.nan

    mask = (gridx > 107.44743) & (gridy > -7.17395)
    grid_grav[mask] = np.nan

    mask = (gridx < 107.38757) & (gridy < -7.14715)
    grid_grav[mask] = np.nan

    mask = (gridx > 107.42013) & (gridy > -7.14517)
    grid_grav[mask] = np.nan

    return grid_grav
