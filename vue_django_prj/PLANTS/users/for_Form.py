from django import forms
## User Controller

# Save user information
class UserInfoForm(forms.Form):
    address = forms.CharField(required=True, label='地址')
    createdAt = forms.DateTimeField(required=True, label='注册时间', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    email = forms.CharField(required=True, label='邮箱')
    id = forms.IntegerField(required=True, label='id')
    password = forms.CharField(required=True, label='密码')
    sex = forms.CharField(required=True, label='性别')
    updatedAt = forms.DateTimeField(required=True, label='更新时间', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    username = forms.CharField(required=True, label='用户名')




# User Login in
class UserLoginForm(forms.Form):
    password = forms.CharField(required=True, label='密码')
    username = forms.CharField(required=True, label='用户名')

# Get dataset of the userId
# Create a dataset belong to the userId
class CreateDataSetForm(forms.Form):
    author = forms.CharField(label='author')
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    datasetMetaId = forms.IntegerField(label='datasetMetaId')
    description = forms.CharField(label='description')
    equipmentId = forms.IntegerField(label='equipmentId')
    name = forms.CharField(label='name')
    state = forms.CharField(label='state')
    type = forms.CharField(label='type')
    updatedAt = forms.DateTimeField(label='updateAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(label='userId')
    id = forms.IntegerField(label='id')

class GetDataSetForm(forms.Form):
    id = forms.IntegerField(required=True, label='id')
    number = forms.IntegerField(required=True, label='number')
    size = forms.IntegerField(required=True, label='size')

## Software Controller

# Find software information by userId
# Save software information
# Update software information
class PutSoftwareForm(forms.Form):
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    id = forms.IntegerField(required=True, label='id')
    name = forms.CharField(label='name')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(label='userId')
    version = forms.CharField(label='version')


## Sample Controller

# Find sample information by userId
# Save sample information
# Update sample information
class SampleForm(forms.Form):
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    growth = forms.CharField(label='growth')
    id = forms.IntegerField(required=True, label='id')
    name = forms.CharField(label='name')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(label='userId')
    period = forms.CharField(label='period')


## Image Meta Controller

# Find image metadata by userId
# Save image metadata
# Update image metadata
class ImageMetaForm(forms.Form):
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    duration = forms.IntegerField(required=True, label='duration')
    format = forms.CharField(label='format')
    frameRate = forms.IntegerField(required=True, label='frameRate')
    id = forms.IntegerField(required=True, label='id')
    name = forms.CharField(label='name')
    recordArea = forms.CharField(label='recordArea')
    recordPosition = forms.CharField(label='recordPosition')
    signalType = forms.CharField(label='signalType')
    startAt = forms.DateTimeField(label='startAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    stimulateDetail = forms.CharField(label='stimulateDetail')
    stimulateMaterial = forms.CharField(label='stimulateMaterial')
    stimulateType = forms.CharField(label='stimulateType')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(required=True, label='userId')

## Iec Meta Controller

# Find Iec file metadata by userId
# Save Iec file metadata
# Update Iec file metadata
class IecMetaForm(forms.Form):
    channelNum = forms.IntegerField(required=True, label='channelNum')
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    duration = forms.IntegerField(required=True, label='duration')
    id = forms.IntegerField(required=True, label='id')
    name = forms.CharField(label='name')
    rate = forms.IntegerField(required=True, label='rate')
    recordPosition = forms.CharField(label='recordPosition')
    samplingRate = forms.IntegerField(required=True, label='samplingRate')
    signalType = forms.CharField(label='signalType')
    startAt = forms.DateTimeField(label='startAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    stimulateDetail = forms.CharField(label='stimulateDetail')
    stimulateMaterial = forms.CharField(label='stimulateMaterial')
    stimulateType = forms.CharField(label='stimulateType')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(required=True, label='userId')

## Equipment Controller

# Find Equipment information by userId
# Save Equipment information
# Update Equipment information
class EquipmentForm(forms.Form):
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    id = forms.IntegerField(required=True, label='id')
    name = forms.CharField(label='name')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(label='userId')
    description = forms.CharField(label='description')
    provider = forms.CharField(label='provider')

## Environment Controller

# Find Environment information by userId
# Save Environment information
# Update Environment information
class EnvironmentForm(forms.Form):
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    humidity = forms.IntegerField(label='humidity')
    id = forms.IntegerField(label='id')
    light = forms.IntegerField(label='light')
    name = forms.CharField(label='name')
    pressure = forms.IntegerField(label='pressure')
    temperature = forms.IntegerField(label='temperature')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(label='userId')

## Dataset Meta Controller

# Find Dataset Meta information by userId
# Save Dataset Meta information
# Update Dataset Meta information
class DatasetMetaForm(forms.Form):
    createdAt = forms.DateTimeField(label='createdAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    detail = forms.CharField(label='detail')
    goal = forms.CharField(label='goal')
    id = forms.IntegerField(label='id')
    name = forms.CharField(label='name')
    operators = forms.CharField(label='operators')
    paper = forms.CharField(label='paper')
    position = forms.CharField(label='position')
    sample = forms.CharField(label='sample')
    signalType = forms.CharField(label='signalType')
    stimulus = forms.CharField(label='stimulus')
    updatedAt = forms.DateTimeField(label='updatedAt', input_formats=['%Y-%m-%dT%H:%M:%S.%fZ'])
    userId = forms.IntegerField(label='userId')

