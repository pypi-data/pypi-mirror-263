from django.db import models
from . import AporteEspacioPublico, EstadoEvaluacionAEP, Documentos
from datetime import datetime
import pytz


class EvaluacionAEP(models.Model):

    def save(self, *args, **kwargs):
        """On save, update timestamps"""
        if not self.id:
            self.fecha_creacion = datetime.now().astimezone(pytz.utc)
        self.fecha_modificacion = datetime.now().astimezone(pytz.utc)
        return super(EvaluacionAEP, self).save(*args, **kwargs)

    aporte_espacio_publico = models.ForeignKey(AporteEspacioPublico,
                                               related_name='evaluacion_aep_aporte_espacio_publico',
                                               on_delete=models.DO_NOTHING)
    estado_evaluacion_aep = models.ForeignKey(EstadoEvaluacionAEP,
                                              related_name='estado_evaluacion_aep_evaluacion_aep',
                                              on_delete=models.DO_NOTHING,
                                              null=True)
    version = models.PositiveSmallIntegerField(default=1)
    vigente = models.BooleanField(default=True)
    incluido_piimep = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(editable=False, null=True)
    fecha_modificacion = models.DateTimeField(null=True)
    estado_seleccion_aoe = models.CharField(max_length=10, null=True, blank=True)
    observaciones_rechazo = models.CharField(max_length=800, null=True, blank=True)
    observaciones_devuelto = models.CharField(max_length=800, null=True, blank=True)
    observaciones_desistimiento = models.CharField(max_length=800, null=True, blank=True)

    # ToDo: debo sacar esto de aqui ya no va
    # esto se debe eliminar
    resolucion = models.ForeignKey(Documentos, related_name='Evaluacion_AEP_Resolucion', on_delete=models.DO_NOTHING, null=True, blank=True)
    certificado = models.ForeignKey(Documentos, related_name='Evaluacion_AEP_Certificado', on_delete=models.DO_NOTHING, null=True, blank=True)
    acta = models.ForeignKey(Documentos, related_name='Evaluacion_AEP_Acta', on_delete=models.DO_NOTHING, null=True, blank=True)
    folio_resolucion = models.CharField(max_length=50, null=True, blank=True)
    # hasta aqui

    fecha_sesion_municipal = models.DateTimeField(null=True)
