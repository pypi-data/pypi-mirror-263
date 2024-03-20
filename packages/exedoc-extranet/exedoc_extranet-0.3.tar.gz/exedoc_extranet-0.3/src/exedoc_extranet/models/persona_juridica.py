from django.db import models
from . import Comuna, Documentos, Usuario


class Persona_Juridica(models.Model):
    APROBAR = 'APROBAR'
    APROBADO = 'APROBADO'
    RECHAZADO = 'RECHAZADO'
    MODIFICADO = 'MODIFICADO'

    ESTADO = [
        (APROBAR, 'APROBAR'),
        (APROBADO, 'APROBADO'),
        (MODIFICADO, 'MODIFICADO'),
        (RECHAZADO, 'RECHAZADO')
    ]

    rut = models.IntegerField(primary_key=True, null=False, blank=False)
    dv = models.CharField(max_length=1, null=True, blank=True)
    razon_social = models.CharField(max_length=200, null=True, blank=True)
    direccion = models.CharField(max_length=200, null=True, blank=True)
    direccion_numero = models.CharField(max_length=50, null=True, blank=True)
    direccion_depto = models.CharField(max_length=50, null=True, blank=True)
    comuna_cod_comuna = models.ForeignKey(Comuna,
                                          related_name='persona_juridica_comuna',
                                          on_delete=models.DO_NOTHING)
    acto_constitutivo_documentos = models.ForeignKey(Documentos, related_name='persona_juridica_documentos',
                                                     on_delete=models.DO_NOTHING)
    email = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    estado = models.CharField(max_length=10,
                              choices=ESTADO,
                              default=APROBAR)
    usuario_ingreso = models.ForeignKey(Usuario,
                                        related_name='persona_juridica_usuario_ingreso',
                                        on_delete=models.DO_NOTHING, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        retorno = "{0} - {1}.".format(self.rut, self.razon_social)
        return retorno
