from webgui.models import GeoBlocks_2019, GeoTracts_2019, GeoBG_2019
from haversine import inverse_haversine, Direction, Unit
from geopy.geocoders import Nominatim
from django.contrib.gis.gdal import Envelope
from django.contrib.gis.geos import Point
import pandas as pd
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

def query_extent(extent, DBName):
    DB = globals()[DBName]
    return DB.objects.filter(centroid__within=extent.wkt)


def query_network():



if __name__ == "__main__":
    bounds = create_extent('Boston', 60)
    tmp = GeoBG_2019.objects.filter(centroid__within=bounds.wkt)
    # queryset = GeoBG_2019.objects.only('pk', 'INTPTLON', 'INTPTLAT', 'centroid')
    # for xy in queryset:
    #     xy.centroid = Point(xy.INTPTLON, xy.INTPTLAT, srid=4326)
    # GeoBG_2019.objects.bulk_update(queryset, fields=['centroid'])
