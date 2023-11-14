from django.db import models


# Create your models here.
class Curso(models.Model):  # Ponemos la herencia models.Model
    nombre = models.CharField(max_length=40)  # Tendrá como máximo 40 caracteres (tipo str).
    camada = models.IntegerField()  # De tipo int.


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    corro = models.EmailField()
