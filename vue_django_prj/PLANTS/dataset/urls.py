from django.urls import path,include
from . import views
app_name = 'dataset'

urlpatterns = [
    path('', views.DatasetView.as_view(), name='dataset'),
    path('/query', views.QueryView.as_view(), name='query'),
    path('/<str:id>', views.DealDatasetView.as_view(), name='delete'),
    path('/<str:id>/file', views.DatasetFileView.as_view(), name='file'),
    path('/<str:id>/zip', views.DatasetZipView.as_view(), name='zip'),
]
