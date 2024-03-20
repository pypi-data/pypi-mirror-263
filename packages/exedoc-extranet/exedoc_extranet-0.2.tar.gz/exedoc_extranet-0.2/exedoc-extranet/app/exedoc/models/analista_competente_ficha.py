from django.db import models
from . import Evaluacion_Imiv, Departamento, Comuna, Region, Usuario, Zona


class Analista_Competente_Ficha(models.Model):
    """Analistas competentes asignados a la ficha"""
    evaluacion_imiv = models.ForeignKey(Evaluacion_Imiv, related_name='analista_competente_ficha_evaluacion_imiv',
                                        on_delete=models.DO_NOTHING, default=None)
    departamento = models.ForeignKey(Departamento, null=True, blank=True,
                                     related_name='analista_competente_ficha_departamento',
                                     on_delete=models.DO_NOTHING)
    region = models.ForeignKey(Region, null=True, blank=True, related_name='analista_competente_ficha_region',
                               on_delete=models.DO_NOTHING)
    comuna = models.ForeignKey(Comuna, null=True, blank=True, related_name='analista_competente_ficha_comuna',
                               on_delete=models.DO_NOTHING)
    zona = models.ForeignKey(Zona, null=True, blank=True, related_name='analista_competente_ficha_zona',
                             on_delete=models.DO_NOTHING)
    regional = models.BooleanField(default=False)
    comunal = models.BooleanField(default=False)
    nacional = models.BooleanField(default=False)
    zonal = models.BooleanField(default=False)
    tomado_por = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True,
                                   related_name='analista_competente_ficha_usuario', )
    estado_respuesta = models.BooleanField(default=False)
    fuera_plazo = models.BooleanField(default=False)
    instance_id = models.CharField(max_length=100, null=True)
    fecha_plazo = models.DateTimeField(null=True)
    fecha_respuesta = models.DateTimeField(null=True)
    usuario_respuesta = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, null=True, blank=True,
                                          related_name='analista_competente_usuario_respuesta')
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    # Campos para controlar el envío de oficio consulta
    oficio_enviado = models.BooleanField(default=False)
    oficio_enviado_fecha = models.DateTimeField(null=True)
    # Campos para controlar la firma del documento de respuesta
    usuario_folio = models.CharField(max_length=50, null=True)
    estado_firma = models.BooleanField(default=False)
    usuario_firma = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    usuario_firma_fecha = models.DateTimeField(null=True)
