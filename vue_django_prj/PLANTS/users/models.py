# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from datetime import datetime

class Dataset(models.Model):
    id = models.BigAutoField(primary_key=True)
    author = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    datasetMetaId = models.BigIntegerField(blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    equipmentId = models.BigIntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    type = models.CharField(max_length=255)
    updatedAt = models.DateTimeField()
    userId = models.BigIntegerField()

    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'dataset'

class FilesName(models.Model):
    id = models.IntegerField(primary_key=True)
    datasetid = models.IntegerField(db_column='datasetId')  # Field name made lowercase.
    filename = models.CharField(db_column='fileName', max_length=255, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'filesname'




class DatasetMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    detail = models.CharField(max_length=255, blank=True, null=True)
    goal = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    operators = models.CharField(max_length=255, blank=True, null=True)
    paper = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    sample = models.CharField(max_length=255, blank=True, null=True)
    signalType = models.CharField(max_length=255, blank=True, null=True)
    stimulus = models.CharField(max_length=255, blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'datasetmeta'


class Environment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    humidity = models.FloatField(blank=True, null=True)
    light = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    pressure = models.FloatField(blank=True, null=True)
    temperature = models.FloatField(blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'environment'


class Equipment(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    description = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    provider = models.CharField(max_length=255, blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'equipmentId'


class IecMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    channelNum = models.SmallIntegerField(blank=True, null=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    name = models.CharField(max_length=255)
    rate = models.IntegerField(blank=True, null=True)
    recordPosition = models.CharField(max_length=255, blank=True, null=True)
    samplingRate = models.BigIntegerField(blank=True, null=True)
    signalType = models.CharField(max_length=255, blank=True, null=True)
    startAt = models.DateTimeField(blank=True, null=True)
    stimulateDetail = models.CharField(max_length=255, blank=True, null=True)
    stimulateMaterial = models.CharField(max_length=255, blank=True, null=True)
    stimulateType = models.CharField(max_length=255, blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'iecmeta'


class ImageMeta(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    duration = models.FloatField(blank=True, null=True)
    format = models.CharField(max_length=255, blank=True, null=True)
    frameRate = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=255)
    recordArea = models.CharField(max_length=255, blank=True, null=True)
    recordPosition = models.CharField(max_length=255, blank=True, null=True)
    signalType = models.CharField(max_length=255, blank=True, null=True)
    startAt = models.DateTimeField(blank=True, null=True)
    stimulateDetail = models.CharField(max_length=255, blank=True, null=True)
    stimulateMaterial = models.CharField(max_length=255, blank=True, null=True)
    stimulateType = models.CharField(max_length=255, blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'imagemeta'


class Sample(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    growth = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255)
    period = models.CharField(max_length=255, blank=True, null=True)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()

    class Meta:
        managed = False
        db_table = 'sample'


class Software(models.Model):
    id = models.BigAutoField(primary_key=True)
    createdAt = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=255)
    updatedAt = models.DateTimeField(blank=True, null=True)
    userId = models.BigIntegerField()
    version = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'software'


class User(models.Model):
    id = models.BigAutoField(primary_key=True)
    address = models.CharField(max_length=255)
    createdAt = models.DateTimeField()
    email = models.CharField(unique=True, max_length=255)
    password = models.CharField(max_length=255)
    sex = models.CharField(max_length=255)
    updatedAt = models.DateTimeField()
    username = models.CharField(unique=True, max_length=255)

    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'user'


