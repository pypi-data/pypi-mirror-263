from django.db import models

from models import Categoria_Imiv, EstadoEvaluacion, TipoIMIV


class TiemposProyecto(models.Model):
    """Define los tiempos de evaluación de SEIM"""

    class Meta:
        verbose_name = "Tiempo de proyecto"
        verbose_name_plural = "Tiempos de proyecto"

    MINUTOS = 'MINUTOS'
    HORAS_CORRIDAS = 'HORAS_CORRIDAS'
    HORAS_HABILES = 'HORAS_HABILES'
    DIAS_CORRIDOS = 'DIAS_CORRIDOS'
    DIAS_HABILES = 'DIAS_HABILES'
    TIPOS = [
        (HORAS_CORRIDAS, 'HORAS_CORRIDAS'),
        (HORAS_HABILES, 'HORAS_HABILES'),
        (DIAS_CORRIDOS, 'DIAS_CORRIDOS'),
        (DIAS_HABILES, 'DIAS_HABILES')
    ]

    estado_evaluacion = models.ForeignKey(EstadoEvaluacion, on_delete=models.DO_NOTHING, related_name='tiempos_proyecto_estado_evaluacion')
    categoria_imiv = models.ForeignKey(Categoria_Imiv, on_delete=models.DO_NOTHING, related_name='tiempos_proyecto_categoria_imiv')
    tipo_imiv = models.ForeignKey(TipoIMIV, null=False, default=TipoIMIV.TIPO_IMIV_NORMAL, on_delete=models.DO_NOTHING)
    plazo_AOE = models.IntegerField(default=0)
    plazo_AOC = models.IntegerField(default=0)
    plazo_interesado = models.IntegerField(default=0)
    tipo_plazo = models.CharField(max_length=20, choices=TIPOS, default=DIAS_HABILES)
    version_imiv = models.IntegerField(default=1)
    prorrogable = models.BooleanField(default=False)

    @staticmethod
    def get_tiempos_proyecto(estado_evaluacion_id, categoria_imiv_id, tipo_imiv_id, version_imiv):
        """Obtiene los tiempos de evaluación de acuerdo al estado de evaluación"""
        from apps.extranet.models.tiempos_proyecto_estado_evaluacion import TiemposProyectoEstadoEvaluacion
        if not TiemposProyectoEstadoEvaluacion.objects.filter(estado_evaluacion_origen_id=estado_evaluacion_id).exists():
            return TiemposProyecto.objects.get(id=0)

        tiempos_proyecto_estado_evaluacion = TiemposProyectoEstadoEvaluacion.objects.get(estado_evaluacion_origen_id=estado_evaluacion_id)
        if not TiemposProyecto.objects.filter(
                estado_evaluacion_id=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id,
                categoria_imiv_id=categoria_imiv_id,
                tipo_imiv_id=tipo_imiv_id,
                version_imiv=version_imiv
        ).exists():
            return TiemposProyecto.objects.get(id=0)

        return TiemposProyecto.objects.get(
            estado_evaluacion_id=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id,
            categoria_imiv_id=categoria_imiv_id,
            tipo_imiv_id=tipo_imiv_id,
            version_imiv=version_imiv
        )
