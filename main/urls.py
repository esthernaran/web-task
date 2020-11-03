"""hola URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
import datetime
import os

from django.contrib import admin
from django.urls import path, re_path

import todo.views

urlpatterns = [
    path('', todo.views.homepage, name="homepage"),
    path('tareas/', todo.views.tareas),
    path(
        'tareas/<int:id_tarea>', 
        todo.views.detalle_tarea,
        name='detail_task',
    ),
    path('proyectos/', todo.views.proyectos),
    path('hola/', todo.views.hola),
    path('files/', todo.views.files),
    path('hola/<int:num>', todo.views.numero),
    path('admin/', admin.site.urls),
]
