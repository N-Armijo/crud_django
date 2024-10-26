from django.db import models

# Create your models here.
#Cada clase es una tabla
class Tarea(models.Model):
    titulo = models.CharField(max_length=100)
    descripcion = models.TextField()
    completado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True) #Se ingresa la fecha por defecto del registro
