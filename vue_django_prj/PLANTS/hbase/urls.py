from django.urls import path,include
from . import views
app_name = 'hbase'

urlpatterns = [
    path('', views.ForDeleteView.as_view(), name=''),
    path('/png/<str:rowKey>', views.FindPictureView.as_view(), name=''),
    path('/<str:rowKey>', views.ForFileView.as_view(), name=''),
]
