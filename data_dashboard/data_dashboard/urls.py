"""
URL configuration for data_dashboard project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.views.generic.base import RedirectView # Importar RedirectView

urlpatterns = [
    # Redirige la raíz (/) directamente a la URL de la API
    path('', RedirectView.as_view(url='/api/data-quality-analysis/', permanent=False), name='api-root-redirect'), 
    path('admin/', admin.site.urls),
    # Incluye las URLs de la aplicación data_analysis
    path('api/', include('data_analysis.urls')), 
]