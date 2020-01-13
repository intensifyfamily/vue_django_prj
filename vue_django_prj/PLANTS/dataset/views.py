import base64
import json
import os
from django.views import View

from PLANTS.settings import BASE_DIR
from . import models
from .for_Hbase import FileController
from .for_Zip import ZipUtilities
from datetime import datetime
from django.http import JsonResponse, FileResponse, StreamingHttpResponse


## Dataset Controller

# Get the dataset information
# Save dataset
# Modify dataset information
class DatasetView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        try:
            check_obj = models.Dataset.objects.get(userId=val['userId'], name=val['name'])
            if check_obj:
                return JsonResponse({"error": "dataset名已存在"}, status=401, reason='Unauthorized')
        except:
            pass
        try:

            obj = models.Dataset.objects.create(
                author=val['author'],
                createdAt=now,
                datasetMetaId=val['datasetMetaId'],
                description=val['description'],
                equipmentId=val['equipmentId'],
                name=val['name'],
                state=val['state'],
                type=val['type'],
                updatedAt=now,
                userId=val['userId']
            )
            val['id'] = obj.id
            return JsonResponse(val, status=200, reason='OK')
        except:
            return JsonResponse({"error": "dataset已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        number = int(request.GET.get("number"))
        size = int(request.GET.get("size"))
        # try:
        obj_val = models.Dataset.objects.all().values()
        dataset = list(obj_val)
        if dataset:
            ret = {
                "content": dataset[number * size:(number + 1) * size],
                "first": True,
                "last": False,
                "number": number,
                "numberOfElements": size,
                "size": size,
                "sort": {},
                "totalElements": len(dataset),
                "totalPages": len(dataset) / size + 1
            }
            return JsonResponse(ret, status=200, reason='OK')
        else:
            return JsonResponse({"error": "dataset为空"}, status=401, reason='Unauthorized')
        # except:
        #     return JsonResponse({"error": "查询失败"}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print(val)
        obj = models.Dataset.objects.update_or_create(
            id=val['id'],
            defaults={
                "author": val['author'],
                "createdAt": now,
                "datasetMetaId": val['datasetMetaId'],
                "description": val['description'],
                "equipmentId": val['equipmentId'],
                "name": val['name'],
                "state": val['state'],
                "type": val['type'],
                "updatedAt": now,
                "userId": val['userId']}
        )
        return JsonResponse(val, status=200, reason='OK')


# Search dataset information
class QueryView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        keyWord = request.GET.get("keyWord")
        number = int(request.GET.get("number"))
        size = int(request.GET.get("size"))
        try:
            obj_val = models.Dataset.objects.filter(name__icontains=keyWord).values()
            dataset = list(obj_val)
            if dataset:
                ret = {
                    "content": dataset[number * size:(number + 1) * size],
                    "first": True,
                    "last": True,
                    "number": number,
                    "numberOfElements": size,
                    "size": size,
                    "sort": {},
                    "totalElements": len(dataset),
                    "totalPages": len(dataset) / size + 1
                }
                return JsonResponse(ret, status=200, reason='OK')
            else:
                obj_val = models.Dataset.objects.filter(author__icontains=keyWord).values()
                dataset = list(obj_val)
                if dataset:
                    ret = {
                        "content": dataset[number * size:(number + 1) * size],
                        "first": True,
                        "last": True,
                        "number": number,
                        "numberOfElements": size,
                        "size": size,
                        "sort": {},
                        "totalElements": len(dataset),
                        "totalPages": len(dataset) / size + 1
                    }
                    return JsonResponse(ret, status=200, reason='OK')
                return JsonResponse({"error": "dataset为空"}, status=401, reason='Unauthorized')
        except:
            return JsonResponse({"error": "查询失败"}, status=401, reason='Unauthorized')


# Delete the dataset id
# Get dataset information of the id
class DealDatasetView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.Dataset.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Dataset.objects.filter(id=kwargs.get('id')).delete()
            return JsonResponse({"msg": "success!"}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')


# Get dataset information of the id
# Save the files of dataset
class DatasetFileView(View):
    def get(self, request, *args, **kwargs):
        dataset_id = kwargs.get("id")
        msg = []
        all_obj = models.Files.objects.filter(datasetId=dataset_id)
        # files_name = list(obj.fileName)
        for obj in all_obj:
            info = {
                "environmentId": obj.environmentId,
                "iecMetaId": obj.iecMetaId,
                "imageMetaId": obj.imageMetaId,
                "name": obj.name,
                "parentId": 0,  #
                "rowKey": obj.rowKey,
                "sampleId": obj.sampleId,
                "softwareId": obj.softwareId
            }
            msg.append(info)
        return JsonResponse(msg, status=200, reason='OK', safe=False)

    def post(self, request, *args, **kwargs):
        print(request.POST)
        files = request.FILES.getlist('files')
        dataset_id = kwargs.get("id")
        content = ""
        for f in files:
            file_name = dataset_id + "_" + f.name
            content = content + file_name + "@#$%"
            bs_dir = os.path.join(os.path.join(os.path.join(BASE_DIR, 'dist'), 'media'), 'files')
            with open(os.path.join(bs_dir, file_name), 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
                destination.close()
            obj = models.Dataset.objects.filter(id=dataset_id).first()
            models.Files.objects.create(
                datasetId=int(dataset_id),
                environmentId=int(request.POST.get("environmentId")),
                softwareId=int(request.POST.get("softwareId")),  #
                imageMetaId=request.POST.get("imageMetaId"),
                iecMetaId=request.POST.get("iecMetaId"),  #
                name=file_name,
                rowKey=file_name,
                sampleId=int(request.POST.get("sampleId")),  #
                fileName=file_name
            )

        # try:
        # obj = models.Dataset.objects.filter(id=dataset_id).first()
        # models.Files.objects.update_or_create(
        #     datasetId=dataset_id,
        #     defaults={
        #         "datasetId": dataset_id,
        #         "environmentId": request.POST.get("environmentId"),
        #         "softwareId": request.POST.get("softwareId"),  #
        #         "imageMetaId": request.POST.get("imageMetaId"),
        #         "iecMetaId": 0,  #
        #         "name": obj.name,
        #         "rowKey": dataset_id,
        #         "sampleId": request.POST.get("sampleId"),  #
        #         "fileName": content
        #     }
        # )

        # except:
        #     return JsonResponse({"error": "不存在!"}, status=401, reason='a')
        return JsonResponse({"msg": "sucess!"}, status=200, reason='OK')


# Download the zip of the dataset id
class DatasetZipView(View):
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        dataset_id = kwargs.get("id")
        # try:
        all_obj = models.Files.objects.filter(datasetId=dataset_id)
        files_name = []
        for obj in all_obj:
            files_name.append(obj.fileName)
        bs_dir = os.path.join(os.path.join(os.path.join(BASE_DIR, 'dist'), 'media'), 'files')
        utilities = ZipUtilities()
        for filename in files_name:
            tmp_dl_path = os.path.join(bs_dir, filename)
            utilities.toZip(tmp_dl_path, filename)
        response = StreamingHttpResponse(utilities.zip_file, content_type='application/zip')
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(dataset_id + ".zip")
        return response
        # except:
        #     return JsonResponse({"msg": "file not exit"}, status=401, reason='Unauthorized')
