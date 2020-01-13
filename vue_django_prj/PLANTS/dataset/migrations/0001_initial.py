# Generated by Django 2.2.4 on 2019-11-19 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dataset',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField()),
                ('datasetMetaId', models.BigIntegerField(blank=True, null=True)),
                ('description', models.CharField(blank=True, max_length=500, null=True)),
                ('equipmentId', models.BigIntegerField(blank=True, null=True)),
                ('name', models.CharField(max_length=255)),
                ('state', models.CharField(max_length=255)),
                ('type', models.CharField(max_length=255)),
                ('updatedAt', models.DateTimeField()),
                ('userId', models.BigIntegerField()),
            ],
            options={
                'db_table': 'dataset',
                'managed': False,
            },
        ),
    ]