from django.db import models

from . import Zona


class Region(models.Model):
    codigo_region = models.CharField(max_length=200)
    region_ordinal = models.CharField(max_length=200, null=True)
    nombre = models.CharField(max_length=200)
    nombre_formal = models.CharField(max_length=500, null=True)
    orden = models.IntegerField(null=True, blank=True)
    zona = models.ForeignKey(Zona, on_delete=models.DO_NOTHING, related_name='zona_region', null=True, blank=True)
    sigla_seim = models.CharField(max_length=30, null=True)
    constraints = [
        models.UniqueConstraint(
            fields=['codigo_region'],
            name='unique código de región'
        ),
        models.UniqueConstraint(
            fields=['region_ordinal'],
            name='unique región ordinal de región'
        ),
        models.UniqueConstraint(
            fields=['orden'],
            name='unique orden de región'
        ),
        models.UniqueConstraint(
            fields=['sigla_seim'],
            name='unique sigla seim de región'
        ),
        models.UniqueConstraint(
            fields=['nombre'],
            name='unique nombre de región'
        ),
        models.UniqueConstraint(
            fields=['nombre_formal'],
            name='unique nombre_formal de región'
        )
    ]

    def __str__(self):
        return self.nombre or 'S/I' if self.nombre_formal is None else self.nombre_formal
