from django.db import models

from models import EstadoEvaluacion


class TiemposProyectoEstadoEvaluacion(models.Model):
    estado_evaluacion_origen = models.ForeignKey(EstadoEvaluacion,
                                                 null=False,
                                                 on_delete=models.DO_NOTHING,
                                                 related_name='tiempos_proyecto_estado_evaluacion_origen')
    estado_evaluacion_destino = models.ForeignKey(EstadoEvaluacion,
                                                  null=True,
                                                  on_delete=models.DO_NOTHING,
                                                  related_name='tiempos_proyecto_estado_evaluacion_destino')
