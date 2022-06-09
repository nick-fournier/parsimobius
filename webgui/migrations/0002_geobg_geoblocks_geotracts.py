# Generated by Django 3.2.5 on 2022-06-08 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webgui', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='GeoBG',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_geocode', models.CharField(max_length=15)),
                ('h_geocode', models.CharField(max_length=15)),
                ('createdate', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=2)),
                ('S000', models.IntegerField()),
                ('SA01', models.IntegerField()),
                ('SA02', models.IntegerField()),
                ('SA03', models.IntegerField()),
                ('SE01', models.IntegerField()),
                ('SE02', models.IntegerField()),
                ('SE03', models.IntegerField()),
                ('SI01', models.IntegerField()),
                ('SI02', models.IntegerField()),
                ('SI03', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeoBlocks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_geocode', models.CharField(max_length=15)),
                ('h_geocode', models.CharField(max_length=15)),
                ('createdate', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=2)),
                ('S000', models.IntegerField()),
                ('SA01', models.IntegerField()),
                ('SA02', models.IntegerField()),
                ('SA03', models.IntegerField()),
                ('SE01', models.IntegerField()),
                ('SE02', models.IntegerField()),
                ('SE03', models.IntegerField()),
                ('SI01', models.IntegerField()),
                ('SI02', models.IntegerField()),
                ('SI03', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GeoTracts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('w_geocode', models.CharField(max_length=15)),
                ('h_geocode', models.CharField(max_length=15)),
                ('createdate', models.CharField(max_length=8)),
                ('state', models.CharField(max_length=2)),
                ('S000', models.IntegerField()),
                ('SA01', models.IntegerField()),
                ('SA02', models.IntegerField()),
                ('SA03', models.IntegerField()),
                ('SE01', models.IntegerField()),
                ('SE02', models.IntegerField()),
                ('SE03', models.IntegerField()),
                ('SI01', models.IntegerField()),
                ('SI02', models.IntegerField()),
                ('SI03', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]