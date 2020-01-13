from django.db import models

# Create your models here.
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
