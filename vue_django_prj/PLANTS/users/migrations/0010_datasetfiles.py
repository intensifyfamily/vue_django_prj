# Generated by Django 2.2.4 on 2019-11-19 07:51

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_delete_datasetfiles'),
    ]

    operations = [
        migrations.CreateModel(
            name='DatasetFiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datasetId', models.IntegerField()),
                ('fileNames', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'db_table': 'dataset_files',
                'managed': False,
            },
        ),
    ]
