from django.db import models


class Organismo(models.Model):
    ORGANISMO_EVALUADOR_SEREMI = 1
    ORGANISMO_EVALUADOR_DTTP = 4

    nombre = models.CharField(max_length=200, null=True, blank=True)
    sigla = models.CharField(max_length=50, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    usuario_modificacion = models.IntegerField(null=True)
