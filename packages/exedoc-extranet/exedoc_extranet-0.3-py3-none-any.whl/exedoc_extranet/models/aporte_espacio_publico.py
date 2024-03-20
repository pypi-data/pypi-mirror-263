"""Modelo para soportar el ingreso y evaluación de las solicitudes de aporte al espacio público"""
from django.db import models
from . import Proyecto, Documentos, EstadoEvaluacionAEP


class AporteEspacioPublico(models.Model):
    """Modelo para soportar el ingreso y evaluación de las solicitudes de aporte al espacio público"""

    class Meta:
        verbose_name = "Aporte al Espacio Público"
        verbose_name_plural = "Aportes al Espacio Público"

    proyecto = models.ForeignKey(Proyecto, related_name="aporte_espacio_publico_imiv", on_delete=models.DO_NOTHING)
    vigente = models.BooleanField(default=True)
    aporte_permiso_edificacion = models.DecimalField(max_digits=13, decimal_places=3, null=False)
    permiso_edificacion = models.ForeignKey(Documentos, related_name="aporte_espacio_publico_permiso_edificacion", null=True, on_delete=models.DO_NOTHING)
    presupuesto_detallado = models.ForeignKey(Documentos, related_name="aporte_espacio_publico_presupuesto", on_delete=models.DO_NOTHING)
    informe_favorable_minvu = models.ForeignKey(Documentos, related_name="aporte_espacio_publico_informe_minvu", null=True, on_delete=models.DO_NOTHING)
    informe_favorable_mtt = models.ForeignKey(Documentos, related_name="aporte_espacio_publico_informe_mtt", null=True, on_delete=models.DO_NOTHING)
    justificacion = models.CharField(max_length=800, null=False, blank=False)

    estado_evaluacion_aep = models.ForeignKey(EstadoEvaluacionAEP, null=True, on_delete=models.DO_NOTHING)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    ultimo_estado_evaluacion_aep = models.ForeignKey(EstadoEvaluacionAEP, null=True, on_delete=models.SET_NULL,
                                                     related_name='extranet_AporteEspacioPublico_ultimo_estado_evaluacion_aep')
