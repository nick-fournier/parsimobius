# Generated by Django 3.2.5 on 2022-06-09 16:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0004_geobg_geoblocks_geotracts'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GeoBG',
            new_name='GeoBG_2019',
        ),
        migrations.RenameModel(
            old_name='GeoBlocks',
            new_name='GeoBlocks_2019',
        ),
        migrations.RenameModel(
            old_name='GeoTracts',
            new_name='GeoTracts_2019',
        ),
    ]
