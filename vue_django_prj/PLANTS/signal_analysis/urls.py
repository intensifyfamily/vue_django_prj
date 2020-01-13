from django.urls import path,include
from . import views
app_name = 'users'

urlpatterns = [
    path('analysis/ap/extraction/<str:rate>/', views.ForExtractionView.as_view(), name=''),
    path('analysis/ap/judgement/<str:rate>/', views.FindJudgementView.as_view(), name=''),
    path('analysis/image/multiple/<str:datasetId>/', views.ForMultipleView.as_view(), name=''),
    path('analysis/image/single/<str:datasetId>/', views.ForSingleView.as_view(), name=''),
    path('analysis/smooth/<str:windowWidth>/', views.ForSmoothView.as_view(), name=''),
    path('analysis/sort/<str:datasetId>/', views.ForSortView.as_view(), name=''),

]
