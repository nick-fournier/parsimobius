# Generated by Django 3.2.5 on 2022-06-08 16:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0002_geobg_geoblocks_geotracts'),
    ]

    operations = [
        migrations.DeleteModel(
            name='GeoBG',
        ),
        migrations.DeleteModel(
            name='GeoBlocks',
        ),
        migrations.DeleteModel(
            name='GeoTracts',
        ),
    ]
