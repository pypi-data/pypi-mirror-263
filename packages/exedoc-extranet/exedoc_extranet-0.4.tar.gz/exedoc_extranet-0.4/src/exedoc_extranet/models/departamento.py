"""
Departamentos de los organismos evaluadores o competentes del proyecto
"""
from django.db import models
from . import Organismo, Perfil


class Departamento(models.Model):
    """
    Departamentos de los organismos evaluadores o competentes del proyecto
    """
    REGIONAL = "REGIONAL"
    COMUNAL = "COMUNAL"
    ZONAL = "ZONAL"
    NACIONAL = "NACIONAL"

    COBERTURAS = [
        (REGIONAL, 'REGIONAL'),
        (COMUNAL, 'COMUNAL'),
        (ZONAL, 'ZONAL'),
        (NACIONAL, 'NACIONAL')
    ]

    DEPARTAMENTO_EVALUADOR_AEP = 31
    DEPARTAMENTO_EVALUADOR_SEREMI = 1
    DEPARTAMENTO_EVALUADOR_DTTP = 16

    nombre = models.CharField(max_length=200, null=True, blank=True)
    sigla = models.CharField(max_length=200, null=True, blank=True)
    estado = models.BooleanField(default=True)
    organismo = models.ForeignKey(Organismo,
                                  related_name='organismo',
                                  on_delete=models.DO_NOTHING)
    cobertura = models.CharField(max_length=10,
                                 choices=COBERTURAS,
                                 default=REGIONAL
                                 )
    acceso = models.ManyToManyField(
        Perfil,
        through='Acceso',
        through_fields=('departamento', 'perfil'),
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    @property
    def full_sigla(self):
        return f'{self.sigla}_{self.organismo.sigla}'.upper()
