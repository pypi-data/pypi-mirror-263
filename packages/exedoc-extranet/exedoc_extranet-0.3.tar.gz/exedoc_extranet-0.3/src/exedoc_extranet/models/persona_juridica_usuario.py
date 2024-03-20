from django.db import models

from . import Usuario, Persona_Juridica, Tipo_Participacion, Documentos, Email_Usuario


class Persona_Juridica_Usuario(models.Model):

    APROBAR = 'APROBAR'
    RECHAZADO = 'RECHAZADO'
    PENDIENTE = 'PENDIENTE'
    VIGENTE = 'VIGENTE'
    NO_VIGENTE = 'NO_VIGENTE'

    ESTADO = [
        (APROBAR, 'APROBAR'),
        (RECHAZADO, 'RECHAZADO'),
        (PENDIENTE, 'PENDIENTE'),
        (VIGENTE, 'VIGENTE'),
        (NO_VIGENTE, 'NO_VIGENTE')
    ]

    usuario_rut = models.ForeignKey(Usuario, related_name='usuario_track', on_delete=models.DO_NOTHING)
    persona_juridica_rut = models.ForeignKey(Persona_Juridica, related_name='persona_juridic_track',
                                             on_delete=models.DO_NOTHING)
    tipo_participacion = models.ForeignKey(Tipo_Participacion,
                                           related_name='tipo_participacion_secondary',
                                           on_delete=models.DO_NOTHING,
                                           default=1)
    email = models.ForeignKey(Email_Usuario,
                              related_name='Persona_Juridica_Usuario_Email',
                              on_delete=models.DO_NOTHING,
                              null=True,
                              blank=True,
                              default=None)
    estado = models.CharField(max_length=10,
                              choices=ESTADO,
                              default=APROBAR)
    documento_legal_documentos = models.ForeignKey(
        Documentos,
        related_name='persona_juridica_usuario_documentos',
        on_delete=models.DO_NOTHING, blank=True, null=True)

    usuario_ingreso = models.ForeignKey(Usuario,
                                        related_name='persona_juridica_usuario_usuario_ingreso',
                                        on_delete=models.DO_NOTHING, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        unique_together = (("usuario_rut", "persona_juridica_rut", "tipo_participacion"),)

    def __str__(self):
        retorno = "{0}.".format(self.persona_juridica_rut)
        return retorno
