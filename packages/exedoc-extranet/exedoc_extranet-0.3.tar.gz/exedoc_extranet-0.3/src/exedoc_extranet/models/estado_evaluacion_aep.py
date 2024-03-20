from django.db import models


class EstadoEvaluacionAEP(models.Model):
    """Estado por los que viaja la evaluación de una solicitud de aporte al espacio público"""
    INICIO_AEP = 1  # INICIO_AEP: el interesado ingresa la solicitud de aporte al espacio público
    EN_REVISION_AEP = 2  # EN_REVISION_AEP: el interesado sube los documentos y los envía; el revisor inicial revisa admisibilidad
    INFORMACION_INCOMPLETA_AEP = 3  # INFORMACION_INCOMPLETA_AEP: En la revisión inicial se rechaza el ingreso por información incompleta
    EN_TRAMITE_AEP = 4  # EN_TRAMITE_AEP: La solicitud es aceptada en admisibilidad; el AOE escoge los AOC a los que consultará
    OFICIO_CONSULTA_AEP = 5  # OFICIO_CONSULTA_AEP: El AOE debe redactar el oficio de consulta a los AOC
    EN_CONSULTA_AEP = 6  # EN_CONSULTA_AEP: El AOC debe emitir sus observaciones a la solicitud de aporte al espacio público
    EN_EVALUACION_AEP = 7  # EN_EVALUACION_AEP: El AOE debe emitir su evaluación de la solicitud de aporte al espacio público
    OBSERVADA_AEP = 8  # OBSERVADA_AEP: El firmante AOE ha firmado la resolución de observación generada por el analista
    EN_EVALUACION_CORREGIDA_AEP = 9  # EN_EVALUACION_CORREGIDA_AEP: El Interesado corrige la solicitud de aporte al espacio público
    APROBADA_AEP = 10  # APROBADA_AEP: El firmante AOE ha firmado la resolución de aprobación generada por el analista
    RECHAZADA_AEP = 11  # RECHAZADA_AEP: El firmante AOE ha firmado la resolución de rechazo generada por el analista
    DESISTIDA_AEP = 12  # DESISTIDA_AEP: El firmante AOE ha firmado la resolución de desistimiento generada por el analista
    NO_ADMISIBLE_AEP = 13  # NO_ADMISIBLE_AEP: La solicitud no es admisible
    RECHAZADA_NO_CORRECCION_AEP = 14  # RECHAZADA_NO_CORRECCION_AEP: : El firmante AOE ha firmado la resolución de rechazo generada por el analista
    SOLICITUD_DESISTIDA_AEP = 15  # SOLICITUD_DESISTIDA_AEP: El interesado desiste de la evaluación AEP
    RESOLUCION_APROBADA_AEP = 16  # RESOLUCION_APROBADA_AEP: El AOE generó la resolución de aprobación y la envió a firma
    RESOLUCION_RECHAZADA_AEP = 17  # RESOLUCION_RECHAZADA_AEP: El AOE generó la resolución de rechazo y la envió a firma
    RESOLUCION_OBSERVADA_AEP = 18  # RESOLUCION_OBSERVADA_AEP: El AOE generó la resolución de observación y la envió a firma
    RESOLUCION_DESISTIDA_AEP = 19  # RESOLUCION_DESISTIDA_AEP: El AOE generó la resolución de desistimiento y la envió a firma
    RESOLUCION_RECHAZO_NO_CORRECCION_AEP = 20  # RESOLUCION_RECHAZO_NO_CORRECCION_AEP: El AOE generó la resolución de rechazo y la envió a firma

    # Orden: INICIO_AEP, EN_REVISION_AEP, EN_TRAMITE_AEP, OFICIO_CONSULTA_AEP, EN_CONSULTA_AEP, EN_EVALUACION_AEP
    #      : RESOLUCION_APROBADA_AEP, APROBADA_AEP
    #      : RESOLUCION_RECHAZADA_AEP, RECHAZADA_AEP
    #      : RESOLUCION_OBSERVADA_AEP, OBSERVADA_AEP
    #      : SOLICITUD_DESISTIDA_AEP, RESOLUCION_DESISTIDA_AEP, DESISTIDA_AEP
    # si el usuario desiste, el analista debe hacer una resolución de desistimiento

    id = models.AutoField(primary_key=True)
    estado = models.CharField(max_length=50, null=False, blank=False)
    estado_interesado = models.CharField(max_length=50, null=True, blank=True, default=None)
    estado_terminal = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.estado}"

    def __repr__(self):
        return f"{self.id} - {self.estado}"

    @staticmethod
    def get_estado_interesado(estado_id):
        return EstadoEvaluacionAEP.objects.get(id=estado_id).estado_interesado

    @staticmethod
    def get_estado_by_id(estado_id):
        return EstadoEvaluacionAEP.objects.get(id=estado_id)
