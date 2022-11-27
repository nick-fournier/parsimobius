"""
Architecture:

TBM - Trip Based Model
    RBF layers:
        1. Select a location and radius extent
        2. Query census zones bases on these parameters:
            a. Hard extent based on simple distance, or
            b. Dynamic extent based on OD flows that end up in the target zone
        3. Use the zone queryset to estimate RBF OD trip layers        

    Network Paths:
        1. Query OSM network based on extent
        2. Pre-calculate k-shortest paths from pruned network nodes

    Assign Trips
        1. Calculate trips per network link


ABM - Activity Based Model
    RBF layers:
        1. Select a location and radius extent
        2. Query census zones bases on these parameters:
            a. Hard extent based on simple distance
            b. Dynamic extent based on OD flows that end up in the target zone
        3. Use the zone queryset to estimate RBF for each feature layer (trips, land use, etc.)

    Network Paths:
        1. Query OSM network based on extent
        2. [TBM] Pre-calculate k-shortest paths from pruned network nodes

    Estimate coefficients:
        1. Estimate travel coefficients using NHTS and RBF layers

    Synthetic Population:
        1. [ABM] Generate synthetic population allocated to XY coordinates within the region.

    Simulate
        1....

"""

from data_io.query import query_extent

def rbf_lodes():

    queryset = query_extent(location='Boston', buffer=10, year=2019)

    # Geo centroids
    gpd.GeoDataFrame(geo_queryset).centroid

    # Merge centroids to OD
    gpd.GeoDataFrame(od_queryset)

def k_shortest():
    """
    get k-shortest paths from each node in the network.
    Number of nodes can be pruned by closeness or shared polylines (i.e., street has a curve?)
    """
    pass






