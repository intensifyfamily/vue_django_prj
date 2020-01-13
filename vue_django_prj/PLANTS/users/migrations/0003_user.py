# Generated by Django 2.2.4 on 2019-11-16 02:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('address', models.CharField(max_length=255)),
                ('createdAt', models.DateTimeField(default=datetime.datetime.now)),
                ('email', models.CharField(max_length=255, unique=True)),
                ('password', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
                ('updatedAt', models.DateTimeField(blank=True, null=True)),
                ('username', models.CharField(max_length=255, unique=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]