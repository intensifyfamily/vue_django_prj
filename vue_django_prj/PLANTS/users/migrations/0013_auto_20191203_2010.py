# Generated by Django 2.2.4 on 2019-12-03 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_auto_20191120_1622'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='datasetmeta',
            table='datasetmeta',
        ),
        migrations.AlterModelTable(
            name='filesname',
            table='filesname',
        ),
        migrations.AlterModelTable(
            name='iecmeta',
            table='iecmeta',
        ),
        migrations.AlterModelTable(
            name='imagemeta',
            table='imagemeta',
        ),
    ]