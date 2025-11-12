from django.urls import path
from . import views

urlpatterns = [
    # Mapea /api/data-quality-analysis/ a la vista
    path('data-quality-analysis/', views.data_analysis_api, name='data_analysis_api'),
]