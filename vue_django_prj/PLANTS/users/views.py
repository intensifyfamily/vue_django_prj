from django.views import View
from . import models
from django.http import JsonResponse
import json
from datetime import datetime


## User Controller
# Save user information
class UserInfoView(View):
    def post(self, request):
        now = datetime.now()
        ret = {}
        val = json.loads(request.body.decode('utf-8'))
        # try:
        obj = models.User.objects.create(
            address=val['address'],
            email=val['email'],
            password=val['password'],
            sex=val['sex'],
            username=val['username'],
            createdAt=now,
            updatedAt=now,
        )
        ret['id'] = obj.id
        ret['address'] = obj.address
        ret['email'] = obj.email
        ret['sex'] = obj.sex
        ret['username'] = obj.username
        return JsonResponse(ret, status=200)
        # except:
        #     return JsonResponse({"error": "用户名或邮箱已存在"},reason="Created", status=201)

    # def get(self, request, *args, **kwargs):
    #     pass


# User Login in
class UserLoginView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        print(request.POST.get("username"))
        print(request.body)
        print(kwargs)
        val = json.loads(request.body.decode('utf-8'))
        print(val['username'])
        try:
            obj = models.User.objects.filter(username=val['username'], password=val['password']).first()
            if obj:
                ret = {
                    "address": obj.address,
                    "email": obj.email,
                    "id": obj.id,
                    "sex": obj.sex,
                    "username": obj.username
                }
                return JsonResponse(ret, reason="OK", status=200)
            else:
                return JsonResponse({"error": "用户不存在"}, reason="Unauthorized", status=401)
        except:
            return JsonResponse({"error": "用户不存在"}, reason="Unauthorized", status=401)

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        pass


# Find user information by userId
class FindUserView(View):
    # def post(self, request, *args, **kwargs):
    #     pass
    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.User.objects.filter(id=kwargs.get('id')).first()
            if obj:
                ret = {
                    "address": obj.address,
                    "email": obj.email,
                    "id": obj.id,
                    "sex": obj.sex,
                    "username": obj.username
                }
                return JsonResponse(ret, status=200, reason="OK")
            else:
                return JsonResponse({"error": "用户不存在"}, reason="Unauthorized", status=401)
        except:
            return JsonResponse({}, reason="Unauthorized", status=401)


# Get dataset of the userId
# Create a dataset belong to the userId
class DataSetView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print(val)
        try:
            check_obj = models.Dataset.objects.get(userId=kwargs.get("userId"), name=val['name'])
            if check_obj:
                return JsonResponse({"error": "dataset名已存在"}, status=401, reason='Unauthorized')
        except:
            pass
        obj = models.Dataset.objects.create(
            author=val['author'],
            createdAt=now,
            datasetMetaId=val['datasetMetaId'],
            description=val['description'],
            equipmentId=val['equipmentId'],
            name=val['name'],
            state="val['state']",
            type=val['type'],
            updatedAt=now,
            userId=kwargs.get("userId")
        )
        val['userId'] = kwargs.get("userId")
        val['id'] = obj.id
        return JsonResponse(val, status=200, reason='OK')
        # except:
        #    return JsonResponse({"error": "dataset已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        number = int(request.GET.get("number"))
        size = int(request.GET.get("size"))
        # try:
        dataset = models.Dataset.objects.filter(userId=kwargs.get('userId')).all().values()
        dataset = list(dataset)
        if dataset:
            ret = {
                "content": dataset[number*size:(number+1)*size],
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
            return JsonResponse({"error": "此用户的dataset不存在1"}, status=200, reason='OK')
            # except:
            #     return JsonResponse({"error": "此用户的dataset不存在2"}, status=401, reason='Unauthorized')


## Software Controller

# Find software information by userId
# Save software information
# Update software information
class SoftwareView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        try:
            obj = models.Software.objects.create(
                createdAt=now,
                name=val['name'],
                updatedAt=now,
                userId=kwargs.get("userId"),
                version=val['version']
            )
            val['userId'] = kwargs.get("userId")
            val['id'] = obj.id
            return JsonResponse(val, status=200, reason='OK')
        except:
            return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Software.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        obj = models.Software.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                'createdAt': now,
                'updatedAt': now,
                'name': val['name'],
                'userId': val['userId'],
                'version': val['version']}
        )
        id_obj = models.Software.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete software information
# Find software information by id
class DealSoftwareView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Software.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.Software.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')


## Sample Controller

# Find sample information by userId
# Save sample information
# Update sample information
class SampleView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print(val)
        try:
            obj = models.Sample.objects.create(
                createdAt=now,
                growth=val['growth'],
                name=val['name'],  # 改过，name参数没有
                period=val['period'],
                updatedAt=now,
                userId=kwargs.get("userId"),
            )
            val['userId'] = kwargs.get("userId")
            val['id'] = obj.id
            return JsonResponse(val, status=200, reason='OK')
        except:
            return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Sample.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()

        val = json.loads(request.body.decode('utf-8'))
        obj = models.Sample.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                'createdAt': val['createAt'],
                'growth': val['growth'],
                'name': val['name'],
                'period': val['period'],
                'updatedAt': now,
                'userId': val['userId']}
        )
        id_obj = models.Software.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete sample information
# Find sample information by id
class DealSampleView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Sample.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.Sample.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')


## Image Meta Controller

# Find image metadata by userId
# Save image metadata
# Update image metadata
class ImageMetaView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print(val)
        # try:
        obj = models.ImageMeta.objects.create(
            createdAt=now,
            duration=val['duration'],
            format=val['format'],
            frameRate=val['frameRate'],
            name=val['name'],
            recordArea=val['recordArea'],
            recordPosition="val['recordPosition']",  # 改过，没有
            signalType=val['signalType'],
            startAt=val['startAt'],
            stimulateDetail=val['stimulateDetail'],
            stimulateMaterial=val['stimulateMaterial'],
            stimulateType=val['stimulateType'],
            updatedAt=now,
            userId=kwargs.get("userId"),
        )
        val['userId'] = kwargs.get("userId")
        val['id'] = obj.id
        return JsonResponse(val, status=200, reason='OK')
        # except:
        #     return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.ImageMeta.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()

        val = json.loads(request.body.decode('utf-8'))
        obj = models.ImageMeta.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                "createdAt": now,
                "duration": val['duration'],
                "format": val['format'],
                "frameRate": val['frameRate'],
                "name": val['name'],
                "recordArea": val['recordArea'],
                "recordPosition": val['recordPosition'],
                "signalType": val['signalType'],
                "startAt": val['startAt'],
                "stimulateDetail": val['stimulateDetail'],
                "stimulateMaterial": val['stimulateMaterial'],
                "stimulateType": val['stimulateType'],
                "updatedAt": now,
                "userId": val['userId']}
        )
        id_obj = models.ImageMeta.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete image metadata
# Find image metadata by id
class DealImageMetaView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.ImageMeta.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.ImageMeta.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')


## Iec Meta Controller

# Find Iec file metadata by userId
# Save Iec file metadata
# Update Iec file metadata
class IecMetaView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print(val)
        # try:
        obj = models.IecMeta.objects.create(
            channelNum=val['channelNum'],
            createdAt=now,
            duration=val['duration'],
            name=val['name'],
            rate=val['rate'],
            recordPosition=val['recordPositon'],  # 改过，少一个i
            samplingRate=val['samplingRate'],
            signalType=val['signalType'],
            startAt=val['startAt'],
            stimulateDetail=val['stimulateDetail'],
            stimulateMaterial=val['stimulateMaterial'],
            stimulateType=val['stimulateType'],
            updatedAt=now,
            userId=kwargs.get('userId'),
        )
        val['userId'] = kwargs.get("userId")
        val['id'] = obj.id
        return JsonResponse(val, status=200, reason='OK')
        # except:
        #     return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.IecMeta.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()

        val = json.loads(request.body.decode('utf-8'))
        obj = models.IecMeta.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                "channelNum": val['channelNum'],
                "createdAt": now,
                "duration": val['duration'],
                "name": val['name'],
                "rate": val['rate'],
                "recordPosition": val['recordPosition'],
                "samplingRate": val['samplingRate'],
                "signalType": val['signalType'],
                "startAt": val['startAt'],
                "stimulateDetail": val['stimulateDetail'],
                "stimulateMaterial": val['stimulateMaterial'],
                "stimulateType": val['stimulateType'],
                "updatedAt": now,
                "userId": val['userId'], }
        )
        id_obj = models.IecMeta.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete Iec file metadata
# Find Iec file metadata by id
class DealIecMetaView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.IecMeta.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.IecMeta.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')


## Equipment Controller

# Find Equipment information by userId
# Save Equipment information
# Update Equipment information
class EquipmentView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print(val)
        # try:
        obj = models.Equipment.objects.create(
            createdAt=now,
            name=val['name'],
            updatedAt=now,
            userId=int(kwargs.get("userId")),
            description=val['description'],
            provider=val['provider']
        )
        val['userId'] = int(kwargs.get("userId"))
        val['id'] = obj.id
        return JsonResponse(val, status=200, reason='OK')
        # except:
        #     return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Equipment.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        obj = models.Equipment.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                "createdAt": now,
                "name": val['name'],
                "updatedAt": now,
                "userId": val['userId'],
                "description": val['description'],
                "provider": val['provider']}
        )
        id_obj = models.Equipment.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete Equipment information
# Find Equipment information by id
class DealEquipmentView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Equipment.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.Equipment.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')


## Environment Controller

# Find Environment information by userId
# Save Environment information
# Update Environment information
class EnvironmentView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        try:
            obj = models.Environment.objects.create(
                createdAt=now,
                humidity=val['humidity'],
                light=val['light'],
                name=val['name'],
                pressure=val['pressure'],
                temperature=val['temperature'],
                updatedAt=now,
                userId=kwargs.get("userId")
            )
            val['userId'] = kwargs.get("userId")
            val['id'] = obj.id
            return JsonResponse(val, status=200, reason='OK')
        except:
            return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Environment.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        obj = models.Environment.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                "createdAt": now,
                "humidity": val['humidity'],
                "light": val['light'],
                "name": val['name'],
                "pressure": val['pressure'],
                "temperature": val['temperature'],
                "updatedAt": now,
                "userId": val['userId']}
        )
        id_obj = models.Environment.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete Equipment information
# Find Equipment information by id
class DealEnvironmentView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.Environment.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.Environment.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')


## Dataset Meta Controller

# Find Dataset Meta information by userId
# Save Dataset Meta information
# Update Dataset Meta information
class DatasetMetaView(View):
    def post(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        print("-----------------------------")
        qq = {'name': 'qwdqd', 'goal': 'qwdqw', 'operators': 'fqwf', 'sample': 'fwe', 'postion': '', 'stimulus': '',
              'signalType': 'vwdvd', 'detail': 'sfvdf', 'paper': 'fasf', 'position': 'wefwe'}
        print(val)
        # try:
        obj = models.DatasetMeta.objects.create(
            createdAt=now,
            detail=val['detail'],
            goal=val['goal'],
            name=val['name'],
            operators=val['operators'],
            paper=val['paper'],
            position=val['position'],  # 改过->position->postion
            sample=val['sample'],
            signalType=val['signalType'],
            stimulus=val['stimulus'],
            updatedAt=now,
            userId=kwargs.get("userId")
        )
        val['userId'] = kwargs.get("userId")
        val['id'] = obj.id
        return JsonResponse(val, status=200, reason='OK')
        # except:
        #     return JsonResponse({"error": "创建错误，已存在"}, status=401, reason='Unauthorized')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.DatasetMeta.objects.filter(userId=kwargs.get('userId')).values()
            data = list(obj)
            return JsonResponse(data, status=200, reason='OK', safe=False)
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')

    def put(self, request, *args, **kwargs):
        now = datetime.now()
        val = json.loads(request.body.decode('utf-8'))
        obj = models.DatasetMeta.objects.update_or_create(
            name=val['name'],
            userId=val['userId'],
            defaults={
                "createdAt": now,
                "detail": val['detail'],
                "goal": val['goal'],
                "name": val['name'],
                "operators": val['operators'],
                "paper": val['paper'],
                "position": val['position'],
                "sample": val['sample'],
                "signalType": val['signalType'],
                "stimulus": val['stimulus'],
                "updatedAt": now,
                "userId": val['userId']}
        )
        id_obj = models.DatasetMeta.objects.filter(name=val['name'], userId=val['userId']).first()
        val['id'] = id_obj.id
        return JsonResponse(val, status=200, reason='OK')


# Delete Dataset Meta information
# Find Dataset Meta information by id
class DealDatasetMetaView(View):
    def delete(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            obj = models.DatasetMeta.objects.filter(userId=kwargs.get('userId'), id=kwargs.get('id')).delete()
            return JsonResponse({}, status=200, reason='OK')
        except:
            return JsonResponse({"error": "不存在"}, status=204, reason='No Content')

    def get(self, request, *args, **kwargs):
        now = datetime.now()
        try:
            data = models.DatasetMeta.objects.filter(id=kwargs.get('id')).values()
            return JsonResponse(data[0], status=200, reason='OK')
        except:
            return JsonResponse({}, status=401, reason='Unauthorized')
