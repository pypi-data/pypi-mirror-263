from django.db import models


class Tipo_Participacion(models.Model):
    """Tipos de participación"""
    class Meta:
        verbose_name_plural = "Tipos de participación"
        verbose_name = "Tipo de participación"

    TITULAR = 'TITULAR'
    REPRESENTANTE_LEGAL = 'REPRESENTANTE_LEGAL'
    PROYECTISTA = 'PROYECTISTA'
    CONSULTOR = 'CONSULTOR'
    ELABORACION_INFORME = 'ELABORACION_INFORME'

    TIPOS = [
        (TITULAR, 'TITULAR'),
        (REPRESENTANTE_LEGAL, 'REPRESENTANTE_LEGAL'),
        (PROYECTISTA, 'PROYECTISTA'),
        (CONSULTOR, 'CONSULTOR'),
        (ELABORACION_INFORME, 'ELABORACION_INFORME')
    ]
                                     
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=45,
                              choices=TIPOS,
                              default=TITULAR)

    def __str__(self):
        retorno = "{0} - {1}.".format(self.id, self.nombre)
        return retorno
