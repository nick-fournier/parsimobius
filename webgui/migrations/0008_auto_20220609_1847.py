# Generated by Django 3.2.5 on 2022-06-09 18:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0007_geobg_2019_geoblocks_2019_geotracts_2019'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeoBG_2019',
        ),
        migrations.DeleteModel(
            name='GeoBlocks_2019',
        ),
        migrations.DeleteModel(
            name='GeoTracts_2019',
        ),
    ]
