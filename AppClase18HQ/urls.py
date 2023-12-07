"""
URL configuration for clase18 project.

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
from django.urls import path
from AppClase18HQ.views import crear_curso, show_html, crear_curso_form, busqueda_camada, CursoList, \
    CursoDetalle, CursoCreacion, CursoActualizacion, CursoEliminar


class CursDetalle:
    pass


urlpatterns = [
    path('agregar_curso/', crear_curso),
    path('show/', show_html),
    path('curso/', crear_curso_form),
    path('buscar/', busqueda_camada),
    path('cursos/listar', CursoList.as_view(), name="CursosList"),
    path('curso/<int:pk>', CursoDetalle.as_view(), name="CursosDetail"),
    path('crear', CursoCreacion.as_view(), name="CursosCreate"),
    path('editar/<int:pk>', CursoActualizacion.as_view(), name="CursosEditar"),
    path('eliminar/<int:pk>', CursoEliminar.as_view(), name="CursosEliminar")
]
