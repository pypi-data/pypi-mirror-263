from django.db import models
from . import Evaluacion_Imiv, TipoDocumentoSeim, EvaluacionAEP, Archivo, Permiso, Departamento, EstadoEvaluacion, EstadoEvaluacionAEP

class BorradorDocumentoEvaluacion(models.Model):
    NUEVO = 1
    EN_FIRMA = 2
    FIRMADO = 3
    OBSERVADO = 4
    ESTADOS = [(NUEVO, 1), (EN_FIRMA, 2), (FIRMADO, 3), (OBSERVADO, 4)]

    estado_borrador = models.IntegerField(choices=ESTADOS, default=NUEVO)
    folio = models.CharField(max_length=50, null=True)
    autofolio = models.BooleanField(default=False)

    evaluacion_imiv = models.ForeignKey(Evaluacion_Imiv, related_name='borrador_documento_evaluacion_evaluacion_imiv', on_delete=models.DO_NOTHING, null=True)
    evaluacion_aep = models.ForeignKey(EvaluacionAEP, related_name='borrador_documento_evaluacion_evaluacion_aep', on_delete=models.DO_NOTHING, null=True)
    departamento = models.ForeignKey(Departamento, null=True, on_delete=models.DO_NOTHING, related_name='borrador_departamento_evaluador')
    contenido_documento_seim = models.CharField(max_length=800, null=False, blank=False)
    observacion_documento_seim = models.CharField(max_length=800, null=False, blank=False)
    tipo_documento_seim = models.ForeignKey(
        TipoDocumentoSeim,
        null=True,
        blank=True,
        related_name='borrador_documento_evaluacion_tipo_documento_seim',
        on_delete=models.DO_NOTHING
    )
    adjunto = models.ForeignKey(Archivo, related_name='borrador_documento_evaluacion_archivo_adjunto', on_delete=models.DO_NOTHING, null=True)
    archivo = models.ForeignKey(Archivo, related_name='borrador_documento_evaluacion_archivo_principal', on_delete=models.DO_NOTHING, null=True)
    tipo_adjunto_seim = models.ForeignKey(
        TipoDocumentoSeim,
        null=True,
        blank=True,
        related_name='borrador_documento_evaluacion_tipo_adjunto_seim',
        on_delete=models.DO_NOTHING
    )

    analista = models.ForeignKey(Permiso, on_delete=models.DO_NOTHING, related_name='borrador_documento_evaluacion_permiso_analista', )
    firmante = models.ForeignKey(Permiso, on_delete=models.DO_NOTHING, related_name='borrador_documento_evaluacion_permiso_firmante', )

    estado_origen_evaluacion_imiv = models.ForeignKey(EstadoEvaluacion, null=True, related_name='borrador_estado_evaluacion_imiv', on_delete=models.DO_NOTHING)
    estado_origen_evaluacion_aep = models.ForeignKey(EstadoEvaluacionAEP, null=True, related_name='borrador_estado_evaluacion_aep', on_delete=models.DO_NOTHING)

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
