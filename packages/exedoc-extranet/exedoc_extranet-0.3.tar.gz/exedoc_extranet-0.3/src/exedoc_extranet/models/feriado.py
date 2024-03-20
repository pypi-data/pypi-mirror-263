from django.db import models
from django.db.models import Q

from models import Region, Comuna


class FeriadoAlcance(models.Model):
    nombre = models.CharField(max_length=20, null=False, blank=False)


class FeriadoTipo(models.Model):
    TIPO_CIVIL = 'CIVIL'
    TIPO_RELIGIOSO = 'RELIGIOSO'

    TIPOS_FERIADO = [
        (TIPO_CIVIL, 'CIVIL'),
        (TIPO_RELIGIOSO, 'RELIGIOSO')
    ]

    motivo = models.CharField(max_length=100, null=False, blank=False)
    irrenunciable = models.BooleanField(default=False)
    tipo = models.CharField(max_length=20,
                            choices=TIPOS_FERIADO,
                            default=TIPO_CIVIL
                            )
    alcance = models.ForeignKey(FeriadoAlcance, related_name="alcance_del_feriado", on_delete=models.DO_NOTHING)

    constraints = [
        models.UniqueConstraint(
            fields=['motivo'],
            name='motivo_de_feriado'
        )
    ]


class Feriado(models.Model):
    fecha = models.DateField(null=False, blank=False)
    tipo_feriado = models.ForeignKey(FeriadoTipo, null=False, blank=False, on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, null=True, blank=True, on_delete=models.DO_NOTHING)
    comuna = models.ForeignKey(Comuna, null=True, blank=True, on_delete=models.DO_NOTHING)
    nota = models.CharField(max_length=100, null=True, blank=True, default='')

    constraints = [
        models.CheckConstraint(
            name="Feriado_Comunal_Sin_Comuna_o_Con_region",
            check=(Q(tipo_feriado__feriado_alcance__alcance='Comunal',
                     region__isnull=False,
                     comuna__isnull=True)
                   | Q(tipo_feriado__feriado_alcance__alcance='Comunal',
                       region__isnull=False,
                       comuna__isnull=False))
        ),
        models.CheckConstraint(
            name="Feriado_Regional_Sin_Region_o_Con_Comuna",
            check=(Q(tipo_feriado__feriado_alcance__alcance='Regional',
                     region__isnull=True,
                     comuna__isnull=False)
                   | Q(tipo_feriado__feriado_alcance__alcance='Regional',
                       region__isnull=False,
                       comuna__isnull=False))
        ),
        models.UniqueConstraint(
            name='dia_feriado_nacional',
            fields=['fecha', 'tipo_feriado'],
            condition=Q(tipo_feriado__feriado_alcance__alcance='Nacional')
        ),
        models.UniqueConstraint(
            name='dia_feriado_regional',
            fields=['fecha', 'tipo_feriado', 'region'],
            condition=Q(tipo_feriado__feriado_alcance__alcance='Regional')
        ),
        models.UniqueConstraint(
            name='dia_feriado_comunal',
            fields=['fecha', 'tipo_feriado', 'comuna'],
            condition=Q(tipo_feriado__feriado_alcance__alcance='Comunal')
        )
    ]
