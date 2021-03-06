# Generated by Django 3.2.5 on 2022-06-17 02:16

import django.contrib.gis.db.models.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0016_auto_20220609_1910'),
    ]

    operations = [
        migrations.AddField(
            model_name='geobg_2019',
            name='centroid',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='geoblocks_2019',
            name='centroid',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='geotracts_2019',
            name='centroid',
            field=django.contrib.gis.db.models.fields.PointField(null=True, srid=4326),
        ),
    ]
