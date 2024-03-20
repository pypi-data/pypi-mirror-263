from django.db import models
from django.db.models import Q, Max, Min, Avg

from . import Usuario, EstadoEvaluacion, Evaluacion_Imiv, EvaluacionAEP, EstadoEvaluacionAEP, Documentos
from exedoc_extranet.helpers.set_business_due_date_from_date import set_business_due_date_from_date


class Prorroga(models.Model):
    """Prórrogas de una evaluación"""
    INGRESADA = 'INGRESADA'
    ENFIRMA = 'ENFIRMA'
    ENGDMTT = 'ENGDMTT'
    APROBADA = 'APROBADA'
    RECHAZADA = 'RECHAZADA'
    OBSERVADA = 'OBSERVADA'

    ESTADOS_PRORROGA = [(INGRESADA, 'INGRESADA'), (APROBADA, 'APROBADA'), (RECHAZADA, 'RECHAZADA'),
                        (ENFIRMA, 'ENFIRMA'), (ENGDMTT, 'ENGDMTT'), (OBSERVADA, 'OBSERVADA')]

    id = models.AutoField(primary_key=True)
    evaluacion_imiv = models.ForeignKey(
        Evaluacion_Imiv, related_name='prorroga_evaluacion_imiv', on_delete=models.DO_NOTHING, null=True
    )
    evaluacion_eaep = models.ForeignKey(
        EvaluacionAEP, on_delete=models.DO_NOTHING, null=True, blank=True, related_name='prorroga_evaluacion_eaep'
    )

    estado = models.CharField(max_length=10, choices=ESTADOS_PRORROGA, default=None)
    dias = models.PositiveSmallIntegerField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    folio_resolucion = models.CharField(max_length=50, null=True)
    fecha_resolucion = models.DateTimeField(null=True)
    fecha_envio_resolucion = models.DateTimeField(null=True)
    evaluador = models.ForeignKey(
        Usuario, related_name='prorroga_usuario', on_delete=models.DO_NOTHING, null=True, blank=True
    )
    # Estado de evaluación en la que se está solicitando la prórroga
    # Es necesario verificar que el estado de evaluación permita que sus tiempos sean prorrogados
    estado_evaluacion = models.ForeignKey(
        EstadoEvaluacion, null=True, blank=True, related_name='prorroga_estado_evaluacion',
        on_delete=models.DO_NOTHING
    )

    estado_evaluacion_aep = models.ForeignKey(
        EstadoEvaluacionAEP,
        null=True,
        blank=True,
        related_name='prorroga_estado_evaluacion_eaep',
        on_delete=models.DO_NOTHING
    )

    interesado = models.BooleanField(default=False)
    aprobada = models.BooleanField(null=True)
    respuesta = models.ForeignKey(
        Documentos, null=True, blank=True, related_name='prorroga_documento', on_delete=models.DO_NOTHING
    )

    fecha_evaluacion_aoc = models.DateTimeField(null=True, default=None)
    fecha_evaluacion_aoe = models.DateTimeField(null=True, default=None)
    fecha_respuesta_interesado = models.DateTimeField(null=True, default=None)

    # Una evaluación solo puede tener una prórroga del interesado y una de los AOC/AOE por estado de evaluación
    # prorrogable
    constraints = [models.UniqueConstraint(
        fields=['evaluacion_imiv', 'estado_evaluacion_aep', 'interesado', 'estado_evaluacion'],
        name='unique prorroga'
    )]

    def set_fechas_prorrogadas(self):
        if self.dias is None:
            return False

        if not self.aprobada:
            return False

        if not self.interesado and self.evaluacion_imiv.fecha_ingreso is None:
            return False

        from exedoc_extranet.models import ProrrogaSolicitud
        prorroga_solo_aoe = self.solicitudes.filter(solicitante=ProrrogaSolicitud.AOE).exists() and \
                            self.solicitudes.count() == 1

        self.fecha_respuesta_interesado = None
        self.fecha_evaluacion_aoc = None
        self.fecha_evaluacion_aoe = None

        if not self.interesado:
            self.evaluacion_imiv.prorroga_evaluacion_aoc = self.dias
            self.evaluacion_imiv.prorroga_evaluacion_aoe = self.dias

            self.set_fecha_evaluacion_aoe()
            if not prorroga_solo_aoe:
                self.set_fecha_evaluacion_aoc()

        if self.interesado:
            __fecha_respuesta = self.evaluacion_imiv.fecha_respuesta
            __dias_respuesta_interesado = self.evaluacion_imiv.dias_respuesta_interesado

            if self.evaluacion_imiv.version == 1:
                self.evaluacion_imiv.prorroga_respuesta_interesado = self.dias

            if self.evaluacion_imiv.version == 2:
                __filtro = Q(
                    imiv_id=self.evaluacion_imiv.imiv_id,
                    vigente=False,
                    fecha_respuesta__isnull=False,
                    dias_respuesta_interesado__gt=0,
                    version=1
                )
                if Evaluacion_Imiv.objects.filter(__filtro).exists():
                    __evaluacion = Evaluacion_Imiv.objects.filter(__filtro).aggregate(Max('id'))
                    __evaluacion_anterior = Evaluacion_Imiv.objects.get(__evaluacion.id__max)
                    __fecha_respuesta = __evaluacion_anterior.fecha_respuesta
                    __dias_respuesta_interesado = __evaluacion_anterior.dias_respuesta_interesado
                    __evaluacion_anterior.prorroga_respuesta_interesado = self.dias
                    __evaluacion_anterior.save()

            self.set_fecha_evaluacion_interesado(__fecha_respuesta, __dias_respuesta_interesado + self.dias)
        self.save()

        return True

    def set_fecha_evaluacion_aoe(self):
        from . import TiemposProyecto
        self.fecha_evaluacion_aoe = set_business_due_date_from_date(
            initial_date=self.evaluacion_imiv.fecha_ingreso,
            offset=self.evaluacion_imiv.dias_evaluacion_aoe + self.dias,
            type_offset=TiemposProyecto.DIAS_CORRIDOS
        )
        self.save()

    def set_fecha_evaluacion_aoc(self):
        from . import TiemposProyecto
        self.fecha_evaluacion_aoc = set_business_due_date_from_date(
            initial_date=self.evaluacion_imiv.fecha_ingreso,
            offset=self.evaluacion_imiv.dias_evaluacion_aoc + self.dias,
            type_offset=TiemposProyecto.DIAS_CORRIDOS
        )
        self.save()

    def set_fecha_evaluacion_interesado(self, initial_date, offset):
        from . import TiemposProyecto
        self.fecha_respuesta_interesado = set_business_due_date_from_date(
            initial_date=initial_date,
            offset=offset,
            type_offset=TiemposProyecto.DIAS_CORRIDOS
        )
        self.save()

    def get_max_dias_solicitados(self):
        return self.solicitudes.aggregate(Max('dias'))['dias__max']

    def get_min_dias_solicitados(self):
        return self.solicitudes.aggregate(Min('dias'))['dias__min']

    def get_promedio_dias_solicitados(self):
        return self.solicitudes.aggregate(Avg('dias'))['dias__avg']
