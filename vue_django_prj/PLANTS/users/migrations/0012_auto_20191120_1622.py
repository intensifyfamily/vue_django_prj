# Generated by Django 2.2.7 on 2019-11-20 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_auto_20191120_1621'),
    ]

    operations = [
        migrations.CreateModel(
            name='FilesName',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('datasetid', models.IntegerField(db_column='datasetId')),
                ('filename', models.CharField(blank=True, db_column='fileName', max_length=255, null=True)),
            ],
            options={
                'db_table': 'files_name',
                'managed': False,
            },
        ),
        migrations.DeleteModel(
            name='TableName',
        ),
    ]
