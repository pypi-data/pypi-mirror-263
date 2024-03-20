from django.db import models

from . import Evaluacion_Imiv, Usuario


class Analista_Asignado(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='analista_asignado_usuario', )
    evaluacion_imiv = models.ForeignKey(Evaluacion_Imiv, related_name='analista_asignado_evaluacion_imiv', on_delete=models.DO_NOTHING, default=None)
    vigente = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (('usuario', 'evaluacion_imiv'),)
