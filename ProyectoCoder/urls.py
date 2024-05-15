"""
URL configuration for ProyectoCoder project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path
from AppCoder import views


urlpatterns = [
    #path('', views.inicio,name="Inicio"),
    path('', views.buscarCentral,name="BusquedaCentral"),
    path('AppCoder/contratoFormulario/',views.contratoFormulario,name="ContratoFormulario"),
    path('AppCoder/admin/', admin.site.urls),
    path('AppCoder/cliente/', views.cliente,name="Cliente"),
    path('AppCoder/central/', views.central,name="Central"),
    #path('AppCoder/buscarCentral/', views.buscarCentral,name="BusquedaCentral"),
    path('AppCoder/buscar/', views.buscar),
]
