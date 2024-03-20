from django.db import models
from . import Documentos, EstadoEvaluacion


class Ficha(models.Model):
    id = models.AutoField(primary_key=True)
    estado_ficha = models.CharField(max_length=20, null=True)
    tipo_ficha = models.CharField(max_length=20, null=True, blank=True)
    documento_certificado = models.ForeignKey(
        Documentos, 
        null=True, 
        blank=True, 
        related_name='documento_certificado',
        on_delete=models.DO_NOTHING
    )
    documento_oficio = models.ForeignKey(
        Documentos, 
        null=True, 
        blank=True, 
        related_name='documento_oficio',
        on_delete=models.DO_NOTHING
    )
    identificador = models.CharField(max_length=12, null=True, blank=True)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    expediente = models.CharField(max_length=100, null=True, blank=True)
    descripcion = models.CharField(max_length=800, null=True, blank=True)
    estado_tramite = models.ForeignKey(
        EstadoEvaluacion, 
        null=True, 
        blank=True,
        related_name='estado_evaluacion',
        on_delete=models.DO_NOTHING
    )
    comentario_motivo_desistir = models.CharField(max_length=800, null=True, blank=True, default=" ")
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    requiere_imiv_complementario = models.BooleanField(default=False)
