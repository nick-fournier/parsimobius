from webgui.models import *
from lodes_star.fetch import fetch_geo
from lodes_star.state_codes import Geographies, State
from django.contrib.gis.gdal import DataSource
from django.contrib.gis.geos import GEOSGeometry
from shapely.geometry.multipolygon import MultiPolygon
from shapely.geometry.polygon import Polygon


def store_geo(df_dict):
    #TODO place fetch in the loop, check if state has been stored, if not download it.
    for table_name, gdf in df_dict.items():
        if 'Blocks' in table_name:
            gdf.rename(columns={n: n.replace('10', '') for n in gdf.columns}, inplace=True)

        # Convert Polygon to MultiPolygon. DB is strict about only one or other.
        gdf["geometry"] = [MultiPolygon([feature]) if isinstance(feature, Polygon) else feature for feature in gdf["geometry"]]

        # Convert to SQL friendly Polygon format
        gdf['geometry'] = [GEOSGeometry(str(g)) for g in gdf.geometry]

        if globals()[table_name].objects.filter(STATEFP=gdf.STATEFP[0]).count() == 0:
            print('Storing ' + table_name)
            objs = [globals()[table_name](**row.to_dict()) for index, row in gdf.iterrows()]
            globals()[table_name].objects.bulk_create(objs)
        else:
            print('Skipping ' + table_name + '. Already contains data!')



if __name__ == "__main__":
    states = [x for x in State.abb2name.keys() if x not in ['AS', 'GU', 'MP', 'PR', 'VI', 'UM']]
    cache_dir = '/home/nick/clones/parsimobius/data_io/cache'
    for state in states:
        geo_dict = {
            'GeoBlocks_2019': fetch_geo(state=state, geography='TABBLOCK', year='2019', cache=cache_dir),
            'GeoBG_2019': fetch_geo(state=state, geography='BG', year='2019', cache=cache_dir),
            'GeoTracts_2019': fetch_geo(state=state, geography='TRACT', year='2019', cache=cache_dir)
         }
        store_geo(geo_dict)
