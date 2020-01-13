import csv
import json
import os
from django.views import View
from django.http import JsonResponse, FileResponse
from . import models
from PLANTS.settings import BASE_DIR
from .for_Hbase import FileController
from datetime import datetime
# Create your views here.

## Hbase File Controller

# Delete multiply files in HBase
class ForDeleteView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        data = json.loads(request.body.decode('utf-8'))
        for rowKey in data:
            obj = models.Files.objects.filter(rowKey=rowKey).delete()
        return JsonResponse({}, status=200, reason='OK', safe=False)


# Find the picture in HBase
class FindPictureView(View):
    def get(self, request, *args, **kwargs):
        bs_dir = os.path.join(os.path.join(os.path.join(BASE_DIR, 'dist'), 'media'), 'files')
        rowKey = kwargs.get("rowKey")
        obj = models.Files.objects.filter(rowKey=rowKey).first()
        filename = obj.fileName
        file = open(os.path.join(bs_dir, filename), "rb")
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename='+filename
        return response


# Delete the file in HBase
# Find the file with content in HBase
class ForFileView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        data = json.loads(request.body.decode('utf-8'))
        for rowKey in data:
            obj = models.Files.objects.filter(rowKey=rowKey).delete()
        return JsonResponse({}, status=200, reason='OK', safe=False)
    def get(self, request, *args, **kwargs):
        bs_dir = os.path.join(os.path.join(os.path.join(BASE_DIR, 'dist'), 'media'), 'files')
        rowKey = kwargs.get("rowKey")
        obj = models.Files.objects.filter(rowKey=rowKey).first()
        filename = obj.fileName
        with open(os.path.join(bs_dir, filename), "r") as csvfile:
            rows = csv.reader(csvfile)
            str = ""
            for row in rows:
                print(row)
                for i in range(len(row)):
                    if i != len(row)-1:
                        str = str + row[i] + ","
                    else:
                        str = str + row[i]
                str = str + "\n"

        msg = {
            "content": str,
            "rowKey": rowKey
        }
        return JsonResponse(msg, status=200, reason='OK')






