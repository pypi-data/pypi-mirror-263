"""
Modelo contenedor de los datos utilizados en la categorización del proyecto
"""
from django.db import models

from . import Ficha, Departamento, Region, Comuna, Documentos, TipoIMIV, EstadoEvaluacion


class Imiv(models.Model):
    """
    Modelo contenedor de los datos utilizados en la categorización del proyecto
    """
    CATEGORIA_EXENTO = "EXENTO"
    CATEGORIA_BASICO = "BASICO"
    CATEGORIA_INTERMEDIO = "INTERMEDIO"
    CATEGORIA_MAYOR = "MAYOR"
    CATEGORIA_COMPLEMENTARIO = "COMPLEMENTARIO"

    OBSERVADO = 'OBSERVADO'
    RECHAZADO = 'RECHAZADO'
    APROBADO = 'APROBADO'
    RECHAZADO_NO_CORRECCION = 'RECHAZADONOCORRECCION'
    SILENCIO_POSITIVO = 'SILENCIOPOSITIVO'

    OPCION_RESOLUCION = [(APROBADO, 'APROBADO'), (RECHAZADO, 'RECHAZADO'), (OBSERVADO, 'OBSERVADO'), (RECHAZADO_NO_CORRECCION, 'RECHAZADO_NO_CORRECCION'),
                         (SILENCIO_POSITIVO, 'SILENCIOPOSITIVO')]

    ficha = models.OneToOneField(Ficha, on_delete=models.DO_NOTHING, primary_key=True, related_name='imiv_ficha')
    vigencia = models.DateTimeField(null=True)
    flujo_vehicular = models.IntegerField()
    unidad_flujo_vehicular = models.CharField(max_length=10, null=True)
    flujo_viajes = models.IntegerField()
    unidad_flujo_viajes = models.CharField(max_length=10, null=True)
    categoria_flujo_vehicular = models.CharField(max_length=20, null=True)
    categoria_flujo_viajes = models.CharField(max_length=20, null=True)
    intersecciones_vehicular = models.IntegerField()
    intersecciones_viajes = models.IntegerField()
    estado = models.CharField(max_length=30, null=True, blank=True, choices=OPCION_RESOLUCION)
    departamento_evaluador = models.ForeignKey(Departamento, null=True, blank=True, related_name='imiv_evaluador', on_delete=models.DO_NOTHING)
    region_evaluador = models.ForeignKey(Region, null=True, blank=True, related_name='imiv_region_evaluador', on_delete=models.DO_NOTHING)
    comuna_evaluador = models.ForeignKey(Comuna, null=True, blank=True, related_name='imiv_region_evaluador', on_delete=models.DO_NOTHING)

    aporte_espacio_publico = models.BooleanField(null=True, default=False)
    documento_declaracion_jurada = models.ForeignKey(Documentos, null=True, blank=True, related_name='documento_declaracion_jurada', on_delete=models.DO_NOTHING)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    tipo_imiv = models.ForeignKey(TipoIMIV, null=False, default=TipoIMIV.TIPO_IMIV_NORMAL, on_delete=models.DO_NOTHING)
    ultimo_estado_evaluacion = models.ForeignKey(EstadoEvaluacion, null=True, on_delete=models.SET_NULL)

    @property
    def categoria(self):
        """
        Propiedad calculada: retorna la categoría del proyecto
        """
        if self.categoria_flujo_vehicular == self.categoria_flujo_viajes:
            return self.categoria_flujo_vehicular
        elif self.categoria_flujo_vehicular == self.CATEGORIA_MAYOR or self.categoria_flujo_viajes == self.CATEGORIA_MAYOR:
            return self.CATEGORIA_MAYOR
        elif self.categoria_flujo_vehicular == self.CATEGORIA_INTERMEDIO or self.categoria_flujo_viajes == self.CATEGORIA_INTERMEDIO:
            return self.CATEGORIA_INTERMEDIO
        elif self.categoria_flujo_vehicular == self.CATEGORIA_BASICO or self.categoria_flujo_viajes == self.CATEGORIA_BASICO:
            return self.CATEGORIA_BASICO
        else:
            return self.CATEGORIA_EXENTO
