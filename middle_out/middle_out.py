import itertools
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import geopandas as gpd
from matplotlib import cm
from lodes_star.fetch import fetch_lodes, fetch_geo
from lodes_star.state_codes import Geographies
from scipy.interpolate import RBFInterpolator, Rbf
import xalglib
from geopy.distance import geodesic
import tqdm

### TESTING
Geographies.list()

center = [42.35902563608491, -71.06099989756845]
maxrad = 100

lodes_df = fetch_lodes(state='ma', year='2019')
geo_df = fetch_geo(state='ma', geography='BG', year='2019')

# Extract key cols
od_df = lodes_df['ma_od_main_JT00_2019']

# Remove water
geo_df = geo_df[geo_df.ALAND > 0]

#Convert to numeric
geo_df[['y', 'x']] = geo_df[['INTPTLAT', 'INTPTLON']].astype(float)

# Get distance
#geo_df['distance'] = [geodesic([v['y'], v['x']], center).km for k, v in geo_df.iterrows()]
#geo_df = geo_df[geo_df['distance'] <= maxrad]

# Truncate GEOID
od_df['w_bg'] = od_df.w_geocode.str.slice(0, len(geo_df.GEOID.loc[0]))
od_df['h_bg'] = od_df.h_geocode.str.slice(0, len(geo_df.GEOID.loc[0]))


# Merge on GEOID
odxy = od_df.merge(geo_df.rename(columns={'GEOID': 'w_bg', 'x': 'w_x', 'y': 'w_y'}), on='w_bg')
odxy = odxy.merge(geo_df.rename(columns={'GEOID': 'h_bg', 'x': 'h_x', 'y': 'h_y'}), on='h_bg')
odxy = odxy[['h_geocode', 'h_x', 'h_y', 'S000']]

# Sum up any duplicates (since we're just testing O(x,y) not OD(x1,y1,x2,y2)
odxy_agg = odxy.groupby(['h_x', 'h_y']).sum().reset_index()


#ALGLIB
# model = xalglib.rbfcreate(3, 2)
# xyz = [odxy_agg.h_x.to_list(), odxy_agg.h_y.to_list(), odxy_agg.S000.to_list()]
# xalglib.rbfsetpoints(model, xyz)
# xalglib.rbfsetalgohierarchical(model, 1.0, 3, 0.0)
# rep = xalglib.rbfbuildmodel(model)


# Interp
# rbfi = Rbf(odxy_agg.h_x, odxy_agg.h_y, odxy_agg.S000, function='gaussian', norm=euclidean_norm_numpy)
rbfi = RBFInterpolator(odxy_agg[['h_x', 'h_y']], odxy_agg.S000, kernel='thin_plate_spline')

# Dense extents meshgrid
x_dense = np.linspace(odxy.h_x.min(), odxy.h_x.max(), 100)
y_dense = np.linspace(odxy.h_y.min(), odxy.h_y.max(), 100)
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



def middle_out(state, year):
    pass





