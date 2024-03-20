from django.db import models
from . import Region


class Provincia(models.Model):
    region = models.ForeignKey(Region, related_name='provincias_region', on_delete=models.DO_NOTHING)
    codigo_provincia = models.CharField(max_length=200)
    nombre = models.CharField(max_length=200)
    nombre_formal = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.nombre if self.nombre_formal is None else self.nombre_formal
