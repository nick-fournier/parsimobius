from django.db import models


class OD(models.Model):
    w_geocode = models.CharField(max_length=15)
    h_geocode = models.CharField(max_length=15)
    # year = models.IntegerField()
    createdate = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    S000 = models.IntegerField()
    SA01 = models.IntegerField()
    SA02 = models.IntegerField()
    SA03 = models.IntegerField()
    SE01 = models.IntegerField()
    SE02 = models.IntegerField()
    SE03 = models.IntegerField()
    SI01 = models.IntegerField()
    SI02 = models.IntegerField()
    SI03 = models.IntegerField()
    # table_name = models.CharField(max_length=32)

    class Meta:
        abstract = True

class RAC(models.Model):
    h_geocode = models.CharField(max_length=15)
    # year = models.IntegerField()
    createdate = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    C000 = models.IntegerField()
    CA01 = models.IntegerField()
    CA02 = models.IntegerField()
    CA03 = models.IntegerField()
    CE01 = models.IntegerField()
    CE02 = models.IntegerField()
    CE03 = models.IntegerField()
    CNS01 = models.IntegerField()
    CNS02 = models.IntegerField()
    CNS03 = models.IntegerField()
    CNS04 = models.IntegerField()
    CNS05 = models.IntegerField()
    CNS06 = models.IntegerField()
    CNS07 = models.IntegerField()
    CNS08 = models.IntegerField()
    CNS09 = models.IntegerField()
    CNS10 = models.IntegerField()
    CNS11 = models.IntegerField()
    CNS12 = models.IntegerField()
    CNS13 = models.IntegerField()
    CNS14 = models.IntegerField()
    CNS15 = models.IntegerField()
    CNS16 = models.IntegerField()
    CNS17 = models.IntegerField()
    CNS18 = models.IntegerField()
    CNS19 = models.IntegerField()
    CNS20 = models.IntegerField()
    CR01 = models.IntegerField()
    CR02 = models.IntegerField()
    CR03 = models.IntegerField()
    CR04 = models.IntegerField()
    CR05 = models.IntegerField()
    CR07 = models.IntegerField()
    CT01 = models.IntegerField()
    CT02 = models.IntegerField()
    CD01 = models.IntegerField()
    CD02 = models.IntegerField()
    CD03 = models.IntegerField()
    CD04 = models.IntegerField()
    CS01 = models.IntegerField()
    CS02 = models.IntegerField()
    # table_name = models.CharField(max_length=32)

    class Meta:
        abstract = True


class WAC(models.Model):
    w_geocode = models.CharField(max_length=15)
    # year = models.IntegerField()
    createdate = models.CharField(max_length=8)
    state = models.CharField(max_length=2)
    C000 = models.IntegerField()
    CA01 = models.IntegerField()
    CA02 = models.IntegerField()
    CA03 = models.IntegerField()
    CE01 = models.IntegerField()
    CE02 = models.IntegerField()
    CE03 = models.IntegerField()
    CNS01 = models.IntegerField()
    CNS02 = models.IntegerField()
    CNS03 = models.IntegerField()
    CNS04 = models.IntegerField()
    CNS05 = models.IntegerField()
    CNS06 = models.IntegerField()
    CNS07 = models.IntegerField()
    CNS08 = models.IntegerField()
    CNS09 = models.IntegerField()
    CNS10 = models.IntegerField()
    CNS11 = models.IntegerField()
    CNS12 = models.IntegerField()
    CNS13 = models.IntegerField()
    CNS14 = models.IntegerField()
    CNS15 = models.IntegerField()
    CNS16 = models.IntegerField()
    CNS17 = models.IntegerField()
    CNS18 = models.IntegerField()
    CNS19 = models.IntegerField()
    CNS20 = models.IntegerField()
    CR01 = models.IntegerField()
    CR02 = models.IntegerField()
    CR03 = models.IntegerField()
    CR04 = models.IntegerField()
    CR05 = models.IntegerField()
    CR07 = models.IntegerField()
    CT01 = models.IntegerField()
    CT02 = models.IntegerField()
    CD01 = models.IntegerField()
    CD02 = models.IntegerField()
    CD03 = models.IntegerField()
    CD04 = models.IntegerField()
    CS01 = models.IntegerField()
    CS02 = models.IntegerField()
    CFA01 = models.IntegerField()
    CFA02 = models.IntegerField()
    CFA03 = models.IntegerField()
    CFA04 = models.IntegerField()
    CFA05 = models.IntegerField()
    CFS01 = models.IntegerField()
    CFS02 = models.IntegerField()
    CFS03 = models.IntegerField()
    CFS04 = models.IntegerField()
    CFS05 = models.IntegerField()
    # table_name = models.CharField(max_length=32)

    class Meta:
        abstract = True

class OD_MAIN_JT00_2019(OD):
    pass

class OD_AUX_JT00_2019(OD):
    pass

class WAC_S000_JT00_2019(WAC):
    pass

class RAC_S000_JT00_2019(RAC):
    pass
