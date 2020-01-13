# Generated by Django 2.2 on 2020-01-10 09:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0015_auto_20200110_1737'),
    ]

    operations = [
        migrations.CreateModel(
            name='Files',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_column='name', max_length=255)),
                ('datasetId', models.IntegerField(db_column='datasetId')),
                ('environmentId', models.IntegerField(db_column='environmentId')),
                ('softwareId', models.IntegerField(db_column='softwareId')),
                ('imageMetaId', models.IntegerField(db_column='imageMetaId')),
                ('iecMetaId', models.IntegerField(db_column='iecMetaId')),
                ('sampleId', models.IntegerField(db_column='sampleId')),
                ('fileName', models.CharField(db_column='fileName', max_length=255)),
                ('rowKey', models.CharField(db_column='rowKey', max_length=255)),
            ],
            options={
                'db_table': 'files',
                'managed': False,
            },
        ),
    ]
