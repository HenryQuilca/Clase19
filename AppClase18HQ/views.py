from django.http import HttpResponse
from django.shortcuts import render, redirect
from AppClase18HQ.models import Curso


# Create your views here.
def mostrar_cursos(request):
    cursos = Curso.objects.all()
    contexto = {
        "cursos": cursos,
        "nombre": "Henry"
    }
    return render(request, 'AppCoder/cursos.html', contexto)


def crear_curso(request):
    curso = Curso(nombre="Python", camada=47789)
    curso.save()

    return redirect("/app/cursos/")


def show_html(request):
    curso = Curso.objects.first()
    contexto = {"curso": curso, "nombre": "Henry"}
    return render(request, 'index.html', contexto)
