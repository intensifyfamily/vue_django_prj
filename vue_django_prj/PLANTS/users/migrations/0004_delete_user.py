# Generated by Django 2.2.4 on 2019-11-16 02:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]
