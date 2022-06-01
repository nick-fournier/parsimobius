import itertools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from matplotlib import cm
from lodes_star.fetch import fetch_lodes, fetch_geoblocks
from scipy.interpolate import RBFInterpolator, Rbf

### TESTING
def middle_out(state, year):
    lodes_df = fetch_lodes(state='ma', year='2019')
    blocks_df = fetch_geoblocks(state='ma', year='2019')

    # Extract key cols
    od_df = lodes_df['ma_od_main_JT00_2019']

    # Remove water
    blocks_df = blocks_df[blocks_df.ALAND10 > 0]

    #Convert to numeric
    blocks_df[['y', 'x']] = blocks_df[['INTPTLAT10', 'INTPTLON10']].astype(float)

    # Merge on GEOID
    odxy = od_df.merge(blocks_df.rename(columns={'GEOID10': 'w_geocode', 'x': 'w_x', 'y': 'w_y'}), on='w_geocode')
    odxy = odxy.merge(blocks_df.rename(columns={'GEOID10': 'h_geocode', 'x': 'h_x', 'y': 'h_y'}), on='h_geocode')
    odxy = odxy[['h_geocode', 'h_x', 'h_y', 'S000']]

    # Sum up any duplicates (since we're just testing O(x,y) not OD(x1,y1,x2,y2)
    odxy_agg = odxy.groupby(['h_x', 'h_y']).sum().reset_index()

    # Interp
    # rbfi = Rbf(odxy_agg.h_x, odxy_agg.h_y, odxy_agg.S000, function='gaussian', norm=euclidean_norm_numpy)
    rbfi = RBFInterpolator(odxy_agg[['h_x', 'h_y']], odxy_agg.S000, epsilon=1, kernel='gaussian', neighbors=10000)

    # Dense extents meshgrid
    x_dense = np.linspace(odxy.h_x.min(), odxy.h_x.max(), 10)
    y_dense = np.linspace(odxy.h_y.min(), odxy.h_y.max(), 10)
    xx, yy = np.meshgrid(x_dense, y_dense)

    # recreate dense matrix for plotting
    # rbfi(pd.DataFrame({'x': [-69.939364], 'y': [42.885948]}))
    dense = pd.DataFrame({'x': np.reshape(xx, np.product(xx.shape)), 'y': np.reshape(yy, np.product(yy.shape))})
    dense['z'] = rbfi(dense)
    dense.z[dense.z < 0] = 0
    zz = dense['z'].to_numpy().reshape(xx.shape)
    print('done')

    # plot the result
    plt.rcParams['figure.dpi'] = 600
    plt.subplot(1, 1, 1)
    plt.pcolor(xx, yy, zz, cmap=cm.jet)
    # sns.scatterplot(data=odxy.sample(100000), x='h_x', y='h_y', hue='S000', s=1)
    plt.scatter(odxy_agg.h_x, odxy_agg.h_y, 0.1, odxy_agg.S000, alpha=0.25, cmap=cm.jet)
    plt.colorbar()
    plt.show()





