from django import forms

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
    # id = forms.IntegerField(required=True, label='id')
    number = forms.IntegerField(required=True, label='number')
    size = forms.IntegerField(required=True, label='size')

class QueryDataSetForm(forms.Form):
    keyWord = forms.CharField(label='keyWord')
    number = forms.IntegerField(required=True, label='number')
    size = forms.IntegerField(required=True, label='size')

