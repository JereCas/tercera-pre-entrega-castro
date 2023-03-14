"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from Entrega_tres.views import index, alumnos, profesores, cursos ,agregar_alumno, buscar_alumno, agregar_profesor, buscar_profesor, agregar_curso, buscar_curso 

urlpatterns = [
    path('', index, name="index"),
    path('admin/', admin.site.urls),
    path('alumnos/', alumnos, name="pag_alumnos"),
    path('profesores/', profesores, name="pag_profesores"),
    path('cursos/', cursos, name="pag_cursos"),
    path('alumnos/agregar', agregar_alumno, name="agregar-alumnos"),
    path('alumnos/buscar', buscar_alumno, name="buscar-alumno"),
    path('profesores/agregar', agregar_profesor, name="agregar-profesores"),
    path('profesores/buscar', buscar_profesor, name="buscar-profesor"),
    path('cursos/agregar', agregar_curso, name="agregar-cursos"),
    path('cursos/buscar', buscar_curso, name="buscar-curso"),
]
