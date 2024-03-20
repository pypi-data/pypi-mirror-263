"""Tipos de IMIV en SEIM"""
from django.db import models


class TipoIMIV(models.Model):
    """Tipos de IMIV en SEIM"""

    TIPO_IMIV_NORMAL = 1
    TIPO_IMIV_COMPLEMENTARIO = 2
    TIPO_IMIV_INFORME_SUFICIENCIA = 3

    class Meta:
        verbose_name_plural = "Tipos de IMIV"
        verbose_name = "Tipo de IMIV"

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
