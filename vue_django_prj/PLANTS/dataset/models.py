# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class Files(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(db_column='name', max_length=255)
    datasetId = models.IntegerField(db_column='datasetId')
    environmentId = models.IntegerField(db_column='environmentId')
    softwareId = models.IntegerField(db_column='softwareId')
    imageMetaId = models.IntegerField(db_column='imageMetaId')
    iecMetaId = models.IntegerField(db_column='iecMetaId')
    sampleId = models.IntegerField(db_column='sampleId')
    fileName = models.CharField(db_column='fileName', max_length=255)
    rowKey = models.CharField(db_column='rowKey', max_length=255)

    def __str__(self):
        return self.id

    class Meta:
        managed = False
        db_table = 'files'
