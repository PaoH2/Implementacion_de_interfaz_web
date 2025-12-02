from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard_view, name='dashboard_web'),
    path('data-quality-analysis/', views.data_analysis_api, name='data_analysis_api'),
]