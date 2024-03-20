from django.db import models
from . import Departamento, Perfil


class Acceso(models.Model):
    """Modelo de los accesos al sistema"""
    perfil = models.ForeignKey(Perfil, on_delete=models.DO_NOTHING, related_name='acceso_perfil',)
    departamento = models.ForeignKey(Departamento, on_delete=models.DO_NOTHING, related_name='acceso_departamento',)
    estado = models.BooleanField(default=True)
