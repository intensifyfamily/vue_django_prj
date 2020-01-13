"""PLANTS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from . import views
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('', views.UserInfoView.as_view(), name='用户信息'),
    path('/login', views.UserLoginView.as_view(), name='用户登录'),
    path('/<str:id>', views.FindUserView.as_view(), name='获取用户信息'),
    path('/<str:userId>/dataset', views.DataSetView.as_view(), name='获取用户dataset'),
    path('/<str:userId>/software', views.SoftwareView.as_view(), name='software操作'),
    path('/<str:userId>/software/<str:id>', views.DealSoftwareView.as_view(), name='用户信息'),
    path('/<str:userId>/sample', views.SampleView.as_view(), name='用户信息'),
    path('/<str:userId>/sample/<str:id>', views.DealSampleView.as_view(), name='用户信息'),
    path('/<str:userId>/imageMeta', views.ImageMetaView.as_view(), name='用户信息'),
    path('/<str:userId>/imageMeta/<str:id>', views.DealImageMetaView.as_view(), name='用户信息'),
    path('/<str:userId>/iecMeta', views.IecMetaView.as_view(), name='用户信息'),
    path('/<str:userId>/iecMeta/<str:id>', views.DealIecMetaView.as_view(), name='用户信息'),
    path('/<str:userId>/equipment', views.EquipmentView.as_view(), name='用户信息'),
    path('/<str:userId>/equipment/<str:id>', views.DealEquipmentView.as_view(), name='用户信息'),
    path('/<str:userId>/environment', views.EnvironmentView.as_view(), name='用户信息'),
    path('/<str:userId>/environment/<str:id>', views.DealEnvironmentView.as_view(), name='用户信息'),
    path('/<str:userId>/datasetMeta', views.DatasetMetaView.as_view(), name='用户信息'),
    path('/<str:userId>/datasetMeta/<str:id>', views.DealDatasetMetaView.as_view(), name='用户信息'),
]
