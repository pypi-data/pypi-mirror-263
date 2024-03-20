from django.db import models


class EstadoEvaluacion(models.Model):
    """Estado por los que viaja una evaluación"""
    INICIO = 1
    EN_REVISION = 2
    EN_TRAMITE = 3
    APROBADO = 4
    RECHAZADO = 5
    DEVUELTO = 6
    OBSERVADO = 7
    APROBADO_SILENCIO_POSITIVO = 8
    NO_ASIGNADO = 9
    EN_CONSULTA = 10
    EN_EVALUACION = 11
    EN_EVALUACION_CORREGIDO = 12
    RECHAZADO_NO_CORRECCION = 13
    NO_ASIGNADO_AOC = 14
    DESISTIDO = 15
    RESOLUCION_NO_CORRECCION = 16
    RESOLUCION_EN_FIRMA = 17
    RESOLUCION_DESISTIDO = 18
    RESOLUCION_APROBADO = 19
    RESOLUCION_RECHAZADO = 20
    RESOLUCION_OBSERVADO = 21
    SOLICITUD_DESISTIMIENTO = 22
    RESOLUCION_APROBADO_SILENCIO_POSITIVO = 23
    CREAR_RESOLUCION_NO_CORRECCION = 24
    # ORDEN ESTADOS: INICIO, EN_REVISION, NO_ASIGNADO, NO_ASIGNADO_AOC, EN_CONSULTA, EN_TRAMITE, EN_EVALUACION
    # INICIO: el interesado ingresa el imiv
    # EN_REVISION: el interesado sube los documentos y los envía
    # NO_ASIGNADO: el coordinador asigna un AOE
    # NO_ASIGANDO_AOC: el aoe selecciona los competentes <<==
    # EN_CONSULTA: el aoe envia el oficio consulta
    # EN_TRAMITE: el aoe espera la respuesta de los aoc
    # EN_EVALUACION: el aoe debe responder

    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, null=False, blank=False)
    estado_interesado = models.CharField(max_length=50, null=True, blank=True, default=None)
    estado_terminal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.estado}"

    def __repr__(self):
        return f"{self.id} - {self.estado}"

    @staticmethod
    def get_estado_interesado(estado):
        return EstadoEvaluacion.objects.get(id=estado).estado_interesado
