from django.db import models
from . import Provincia


class Comuna(models.Model):
    provincia = models.ForeignKey(Provincia, related_name='comunas_provincia', on_delete=models.DO_NOTHING)
    codigo_comuna = models.CharField(max_length=10)
    nombre = models.CharField(max_length=200)
    nombre_formal = models.CharField(max_length=500, null=True)
    cant_habitantes = models.IntegerField(default=1)
    es_capital_regional = models.BooleanField(default=False)
    entity = models.CharField(max_length=400, null=True)

    def __str__(self):
        return self.nombre if self.nombre_formal is None else self.nombre_formal
