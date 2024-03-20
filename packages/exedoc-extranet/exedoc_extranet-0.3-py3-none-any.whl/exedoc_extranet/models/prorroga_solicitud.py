"""Solicitudes de prorroga"""
from django.db import models

from . import Usuario, Prorroga, Acceso, Documentos, Permiso


class ProrrogaSolicitud(models.Model):
    """Solicitudes de prorroga"""
    AOC = 'AOC'
    AOE = 'AOE'
    INTERESADO = 'interesado'
    TIPOS_SOLICITANTE = (AOE, AOC, INTERESADO,)
    SOLICITANTES = [
        (AOC, 'AOC'),
        (AOE, 'AOE'),
        (INTERESADO, 'interesado')
    ]

    id = models.AutoField(primary_key=True)
    prorroga = models.ForeignKey(Prorroga, related_name='solicitudes', on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    acceso = models.ForeignKey(Acceso, on_delete=models.DO_NOTHING, default=None, null=True)
    permiso = models.ForeignKey(Permiso, on_delete=models.DO_NOTHING, default=None, null=True)
    dias = models.PositiveSmallIntegerField(default=1)
    motivo = models.CharField(max_length=800, null=False, blank=False)
    folio = models.CharField(max_length=50, null=True)
    solicitante = models.CharField(max_length=10, choices=SOLICITANTES, default=None)
    solicitud = models.ForeignKey(Documentos, null=True, blank=True,
                                  related_name='prorrogasolicitud_documento',
                                  on_delete=models.DO_NOTHING)
    oficio_generado = models.BooleanField(default=False)
    oficio_enviado = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
