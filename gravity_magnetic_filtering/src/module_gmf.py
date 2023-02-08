import numpy as np

def mask_area(grid_grav, gridx, gridy):
    mask = (gridx > 768400) & (gridy > 9206800)
    grid_grav[mask] = np.nan

    mask = (gridx > 770300) & (gridy > 9206300)
    grid_grav[mask] = np.nan

    mask = (gridx < 763700) & (gridy < 9209300)
    grid_grav[mask] = np.nan

    mask = (gridx > 767300) & (gridy > 9209500)
    grid_grav[mask] = np.nan

    return grid_grav