"""Modelo de zonas"""
from django.db import models


class Zona(models.Model):
    """Modelo de zonas"""
    class Meta:
        verbose_name_plural = "Zonas"
        verbose_name = "Zona"

    nombre = models.CharField(max_length=100)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=False)
    fecha_moficacion = models.DateTimeField(auto_now=True, null=True)
