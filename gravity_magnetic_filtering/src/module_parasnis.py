'''

This code aims for density calculation using Parasnis Method

by:
arif.darmawan@riflab.com
9 February 2023

'''
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure
import pandas as pd
import numpy as np

def parasnis(Xad, Yad):

    X = Xad
    Y = Yad

    coef = np.polyfit(X, Y, 1)
    poly1d_fn = np.poly1d(coef)

    fig, ax = plt.subplots(figsize=(10, 5))
    ax.plot(X, Y, color='black', linestyle='None', marker='o', markersize=2, alpha=1)
    ax.plot(X, poly1d_fn(X), '-', label=f'$y = {coef[0]:.1f}x {coef[1]:+.1f}$')

    ax.set_title('Parasnis Chart')
    ax.set_xlabel('(0.04192 * h)') #- TC
    ax.set_ylabel('FAA')

    # ax.set_xlim([60, 100])
    # ax.set_ylim([260, 380])
    ax.legend()

if __name__ == "__main__":

    data_file = '../../../data/data_gravity/satellite_gravity_pth.xlsx'
    df = pd.read_excel(data_file, sheet_name='A', header=0, na_values=None)

    parasnis(df)

    plt.show()

