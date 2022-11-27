from webgui.models import GeoBlocks_2019, GeoTracts_2019, GeoBG_2019, OD_MAIN_JT00_2019
from haversine import inverse_haversine, Direction, Unit
from geopy.geocoders import Nominatim
from django.contrib.gis.gdal import Envelope
from django.contrib.gis.geos import Point
from django.db.models import Q

import pandas as pd
import geopandas as gpd
import osmnx as ox



def create_extent(location, distance):
    """
    Creates a bounding envelope based on a location and some distance.
    """
    geolocator = Nominatim(user_agent="Parsimobius")
    if isinstance(location, str):
        location = geolocator.geocode(location)
    coord = (location.longitude, location.latitude)

    pythag_dist = (distance**2 + distance**2)**0.5
    bounds = [inverse_haversine(coord, pythag_dist, Direction[x], unit=Unit.MILES) for x in ['SOUTHWEST', 'NORTHEAST']]
    bounds = Envelope([j for i in bounds for j in i])

    return bounds

def query_extent(location, buffer, year):
    location = 'Boston'
    buffer = 10
    year = 2019

    GeoDB = globals()['GeoBlocks_' + str(year)]
    ODDB = globals()['OD_MAIN_JT00_' + str(year)]

    # Select bound
    bounds = create_extent(location, buffer)
    geo_queryset = GeoDB.objects.filter(centroid__within=bounds.wkt).values('GEOID', 'geometry')

    # Extract GEOIDs
    geoids = [x.GEOID for x in geo_queryset]

    # Query OD table
    filt = Q(h_geocode__in=geoids) & Q(w_geocode__in=geoids)
    od_queryset = ODDB.objects.filter(filt).values('w_geocode', 'h_geocode', 'S000')

    return {'od': od_queryset, 'geo': geo_queryset}


def query_network():
    pass



if __name__ == "__main__":
    pass

