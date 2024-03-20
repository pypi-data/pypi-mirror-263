from django.db import models
from . import Evaluacion_Imiv, Usuario, TipoDocumentoSeim, Documentos, EvaluacionAEP


class DocumentoEvaluacionImiv(models.Model):
    evaluacion_imiv = models.ForeignKey(Evaluacion_Imiv,
                                        related_name='DocumentoEvaluacionImiv_Evaluacion_Imiv',
                                        null=True,
                                        on_delete=models.DO_NOTHING)
    evaluacion_aep = models.ForeignKey(EvaluacionAEP,
                                       related_name='DocumentoEvaluacionImiv_EvaluacionAEP',
                                       null=True,
                                       on_delete=models.DO_NOTHING)
    documento = models.ForeignKey(Documentos, null=True, blank=True,
                                  related_name='DocumentoEvaluacionImiv_Documentos',
                                  on_delete=models.DO_NOTHING)
    tipo_documento_seim = models.ForeignKey(TipoDocumentoSeim, null=True, blank=True,
                                            related_name='DocumentoEvaluacionImiv_Tipo_documento_seim',
                                            on_delete=models.DO_NOTHING)
    usuario = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING, related_name='DocumentoEvaluacionImiv_usuario', )
    vigente = models.BooleanField(default=True)
    activo = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    esPlano = models.BooleanField(null=True, default=False, editable=True)
    estaTimbrado = models.BooleanField(null=True, default=False, editable=True)
