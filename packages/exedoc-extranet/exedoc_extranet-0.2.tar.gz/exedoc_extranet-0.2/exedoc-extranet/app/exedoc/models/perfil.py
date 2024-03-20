from django.db import models


class Perfil(models.Model):
    """ Lista de perfiles """
    REVISOR_INICIAL = 1
    COORDINADOR = 2
    ANALISTA = 3
    ANALISTA_SECTRA = 4
    DIRECTOR_TRANSITO = 5
    SEREMI = 6
    ADMINISTRADOR = 7
    FIRMANTE_OC = 8
    ADMINISTRADOR_TI = 9
    FIRMANTE_OE = 10

    nombre = models.CharField(max_length=200, null=True, blank=True)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
