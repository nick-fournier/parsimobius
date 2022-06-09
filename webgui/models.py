from .model_base import *


class GeoBlocks_2019(Geo):
    NAME = models.CharField(max_length=10)
    UR = models.CharField(max_length=1)
    UACE = models.CharField(max_length=5, null=True, default=None)
    UATYPE = models.CharField(max_length=1, null=True, default=None)
    BLOCKCE = models.CharField(max_length=6)

class GeoBG_2019(Geo):
    NAMELSAD = models.CharField(max_length=19)
    BLKGRPCE = models.CharField(max_length=1)

class GeoTracts_2019(Geo):
    NAMELSAD = models.CharField(max_length=19)
    NAME = models.CharField(max_length=10)



class OD_MAIN_JT00_2019(OD):
    pass


class OD_AUX_JT00_2019(OD):
    pass


class WAC_S000_JT00_2019(WAC):
    pass


class RAC_S000_JT00_2019(RAC):
    pass
