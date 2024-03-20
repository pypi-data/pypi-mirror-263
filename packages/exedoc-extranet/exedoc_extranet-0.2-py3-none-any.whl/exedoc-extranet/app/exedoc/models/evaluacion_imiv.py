""" Modelo contenedor de los datos de la evaluación del IMIV ingresados por el interesado """

from django.db import models

from . import Imiv, Documentos, EstadoEvaluacion, Usuario, Region, Comuna


class Evaluacion_Imiv(models.Model):
    """ Modelo contenedor de los datos de la evaluación del IMIV ingresados por el interesado """
    
    class Meta:
        verbose_name_plural = "Evaluaciones Imiv"
        verbose_name = "Evaluaciones Imiv"
    
    imiv = models.ForeignKey(Imiv, related_name='evaluacion_imiv_imiv', on_delete=models.DO_NOTHING)
    version = models.PositiveSmallIntegerField(default=1)
    vigente = models.BooleanField(default=True)
    comentarios = models.CharField(max_length=800, null=True, blank=True)
    accesos_vehiculares = models.CharField(max_length=800, null=True, blank=True)
    accesos_vehiculares_documento = models.ForeignKey(
            Documentos,
            related_name='Evaluacion_Imiv_Accesos_Vehiculares',
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True
    )
    accesos_peatonales = models.CharField(max_length=800, null=True, blank=True)
    accesos_peatonales_documento = models.ForeignKey(
            Documentos,
            related_name='Evaluacion_Imiv_Accesos_Peatonales',
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True
    )
    accesos_cargas = models.CharField(max_length=800, null=True, blank=True)
    accesos_cargas_documento = models.ForeignKey(
            Documentos, related_name='Evaluacion_Imiv_Accesos_Cargas', on_delete=models.DO_NOTHING, null=True,
            blank=True
    )
    vias_externas_colindantes = models.ForeignKey(
            Documentos,
            related_name='Evaluacion_Imiv_Vias_Externas_Colindantes',
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True
    )
    vias_internas_colindantes = models.ForeignKey(
            Documentos,
            related_name='Evaluacion_Imiv_Vias_Internas_Colindantes',
            on_delete=models.DO_NOTHING,
            null=True,
            blank=True
    )
    otras_consideraciones = models.CharField(max_length=800, null=True, blank=True)
    observaciones = models.CharField(max_length=800, null=True, blank=True)
    estado_evaluacion = models.ForeignKey(
            EstadoEvaluacion,
            null=True,
            blank=True,
            related_name='evaluacion_imiv_estado_evaluacion',
            on_delete=models.DO_NOTHING,
            default=EstadoEvaluacion.EN_REVISION
    )
    fecha_ingreso = models.DateTimeField(null=True, blank=True)
    fecha_respuesta = models.DateTimeField(null=True, blank=True)
    
    fecha_evaluacion_aoc = models.DateTimeField(null=True, blank=True)
    dias_evaluacion_aoc = models.IntegerField(default=0)
    prorroga_evaluacion_aoc = models.IntegerField(default=0)
    
    fecha_evaluacion_aoe = models.DateTimeField(null=True, blank=True)
    dias_evaluacion_aoe = models.IntegerField(default=0)
    prorroga_evaluacion_aoe = models.IntegerField(default=0)
    
    fecha_respuesta_interesado = models.DateTimeField(null=True, blank=True)
    dias_respuesta_interesado = models.IntegerField(default=0)
    prorroga_respuesta_interesado = models.IntegerField(default=0)
    
    usuario_ingreso = models.ForeignKey(
            Usuario, null=True, blank=True, related_name='evaluacion_imiv_usuario_ingreso', on_delete=models.SET_NULL
    )
    norma_utilizada = models.CharField(max_length=800, null=True, blank=True)
    cantidad_predios = models.IntegerField(null=True, default=0)
    
    cup = models.CharField(max_length=50, null=True, blank=True)
    
    usuario_elaboracion_informe = models.ForeignKey(
            Usuario,
            null=True,
            blank=True,
            related_name='evaluacion_imiv_usuario_elaboracion_informe',
            on_delete=models.SET_NULL
    )
    nro_acto_administrativo = models.CharField(max_length=50, null=True, blank=True)
    fecha_acto_administrativo = models.DateTimeField(null=True)
    region_aprueba_informe = models.ForeignKey(
            Region, null=True, blank=True, related_name='evaluacion_imiv_region_aprueba', on_delete=models.DO_NOTHING
    )
    nro_permiso_edificacion = models.CharField(max_length=50, null=True, blank=True)
    nro_expediente_exedoc = models.CharField(max_length=50, null=True, blank=True)
    comuna_otorga_permiso = models.ForeignKey(
            Comuna, null=True, blank=True, related_name='evaluacion_imiv_comuna_otorga', on_delete=models.DO_NOTHING
    )
    
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    motivo_desistimiento = models.CharField(max_length=800, null=True)
    
    @staticmethod
    def vigente_exists(ficha_id: int or None) -> bool:
        if ficha_id is None:
            return False
        return Evaluacion_Imiv.objects.filter(imiv__ficha_id=ficha_id, vigente=True).exists()
    
    @staticmethod
    def exists(ficha_id: int or None) -> bool:
        if ficha_id is None:
            return False
        return Evaluacion_Imiv.objects.filter(imiv__ficha_id=ficha_id).exists()
    
    def update_fecha_vencimiento_evaluacion(self, prorroga):
        
        if prorroga.fecha_evaluacion_aoe is not None:
            self.prorroga_evaluacion_aoe = prorroga.dias
            self.fecha_evaluacion_aoe = prorroga.fecha_evaluacion_aoe
        
        if prorroga.fecha_evaluacion_aoc is not None:
            self.prorroga_evaluacion_aoc = prorroga.dias
            self.fecha_evaluacion_aoc = prorroga.fecha_evaluacion_aoc
        
        if prorroga.fecha_respuesta_interesado is not None:
            self.prorroga_respuesta_interesado = prorroga.dias
            self.fecha_respuesta_interesado = prorroga.fecha_respuesta_interesado
        
        self.save()

    def set_fecha_evaluacion_aoe(self):
        from . import TiemposProyecto
        from app.exedoc.helpers import set_business_due_date_from_date
        self.fecha_evaluacion_aoe = set_business_due_date_from_date(
                initial_date=self.fecha_ingreso,
                offset=self.dias_evaluacion_aoe + self.prorroga_evaluacion_aoe,
                type_offset=TiemposProyecto.DIAS_CORRIDOS
        )
        self.save()

    def set_fecha_evaluacion_aoc(self):
        from . import TiemposProyecto
        from app.exedoc.helpers import set_business_due_date_from_date
        self.fecha_evaluacion_aoc = set_business_due_date_from_date(
                initial_date=self.fecha_ingreso,
                offset=self.dias_evaluacion_aoc + self.prorroga_evaluacion_aoc,
                type_offset=TiemposProyecto.DIAS_CORRIDOS
        )
        self.save()

    def set_fecha_evaluacion_interesado(self):
        from app.exedoc.models import TiemposProyecto
        from app.exedoc.helpers import set_business_due_date_from_date
        self.fecha_respuesta_interesado = set_business_due_date_from_date(
                initial_date=self.fecha_respuesta,
                offset=self.dias_respuesta_interesado + self.prorroga_respuesta_interesado,
                type_offset=TiemposProyecto.DIAS_CORRIDOS
        )
        self.save()

