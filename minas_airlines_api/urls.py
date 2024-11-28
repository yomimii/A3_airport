"""
URL configuration for minas_airlines_api project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from rest_framework import routers
from minasAirlines.views import AeronaveViewSet, HangarViewSet, ListaAeronavesHangar

# Criar o router para os ViewSets
router = routers.DefaultRouter()
router.register('airplanes', AeronaveViewSet, basename='Airplanes')
router.register('hangars', HangarViewSet, basename='Hangars')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),  # Inclui as rotas do router
    path('hangars/<int:pk>/airplanes/', ListaAeronavesHangar.as_view(), name='airplanes-by-hangar'),  # Rota para listar aeronaves por hangar
]
