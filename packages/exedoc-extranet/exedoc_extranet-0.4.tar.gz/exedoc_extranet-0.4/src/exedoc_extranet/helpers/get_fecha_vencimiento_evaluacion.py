from . import set_business_due_date_from_date, get_business_due_date_from_today, date_to_str_local
from exedoc_extranet.models import EstadoEvaluacion, Categoria_Imiv, Evaluacion_Imiv


def get_fecha_vencimiento_evaluacion(evaluacion_imiv_id):
    """Obtiene las fechas asociadas a la evaluación de IMIV"""
    evaluacion_imiv = Evaluacion_Imiv.objects.get(id=evaluacion_imiv_id)
    # Si la evaluación es versión 2, está en estado INICIAL, obtenemos la última en estado Observado
    if evaluacion_imiv.version == 2 and evaluacion_imiv.estado_evaluacion_id == EstadoEvaluacion.OBSERVADO:
        obs_eval = Evaluacion_Imiv.objects.filter(
                imiv=evaluacion_imiv.imiv, vigente=False, estado_evaluacion_id=EstadoEvaluacion.OBSERVADO
        ).order_by(
                'fecha_creacion'
        ).last()
        evaluacion_imiv = Evaluacion_Imiv.objects.get(id=obs_eval.id)
    
    categoria_imiv = Categoria_Imiv.objects.get(nombre=evaluacion_imiv.imiv.categoria)
    tipo_imiv = evaluacion_imiv.imiv.tipo_imiv
    
    from exedoc_extranet.models import TiemposProyectoEstadoEvaluacion
    
    tiempos_proyecto_estado_evaluacion = TiemposProyectoEstadoEvaluacion.objects.get(
            estado_evaluacion_origen_id=evaluacion_imiv.estado_evaluacion_id
    )
    
    from exedoc_extranet.models import Prorroga
    prorrogable = False if Prorroga.objects.filter(
            evaluacion_imiv=evaluacion_imiv,
            estado_evaluacion_id=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id,
            interesado=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id == EstadoEvaluacion.OBSERVADO and
                       evaluacion_imiv.version == 1,
            estado__in=(Prorroga.APROBADA, Prorroga.RECHAZADA)
    ).exists() else None
    from exedoc_extranet.models import TiemposProyecto
    tiempo_a_calcular_prorrogable = TiemposProyecto.objects.filter(
            categoria_imiv=categoria_imiv,
            estado_evaluacion_id=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id,
            tipo_imiv=tipo_imiv,
            prorrogable=True,
            version_imiv=evaluacion_imiv.version
    ).exists()
    
    tiempo_a_calcular = None
    if TiemposProyecto.objects.filter(
            categoria_imiv=categoria_imiv,
            estado_evaluacion_id=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id,
            tipo_imiv=tipo_imiv,
            version_imiv=evaluacion_imiv.version
    ).exists():
        tiempo_a_calcular = TiemposProyecto.objects.filter(
                categoria_imiv=categoria_imiv,
                estado_evaluacion_id=tiempos_proyecto_estado_evaluacion.estado_evaluacion_destino_id,
                tipo_imiv=tipo_imiv,
                version_imiv=evaluacion_imiv.version
        ).first()
    #print(f"tiempo a calcular es {tiempo_a_calcular}") 
    #revisar aca el duplicar el tiempo#
    if tiempo_a_calcular is None:
        prorrogable = False
        tiempo_a_calcular_prorrogable = False
        tiempo_a_calcular = TiemposProyecto.objects.get(id=0)
    
    fecha_plazo_aoe = evaluacion_imiv.fecha_evaluacion_aoe
    dias_plazo_aoe = evaluacion_imiv.dias_evaluacion_aoe
    _fecha_plazo_aoe = set_business_due_date_from_date(
            evaluacion_imiv.fecha_ingreso,
            tiempo_a_calcular.plazo_AOE + evaluacion_imiv.prorroga_evaluacion_aoe,
            tiempo_a_calcular.tipo_plazo
    )
    if dias_plazo_aoe != tiempo_a_calcular.plazo_AOE or fecha_plazo_aoe != _fecha_plazo_aoe:
        fecha_plazo_aoe = _fecha_plazo_aoe
        dias_plazo_aoe = tiempo_a_calcular.plazo_AOE
    
    fecha_plazo_aoc = evaluacion_imiv.fecha_evaluacion_aoc
    old_fecha_plazo_aoc = evaluacion_imiv.fecha_evaluacion_aoc 
    dias_plazo_aoc = evaluacion_imiv.dias_evaluacion_aoc
    _fecha_plazo_aoc = set_business_due_date_from_date(
            evaluacion_imiv.fecha_ingreso,
            tiempo_a_calcular.plazo_AOC + evaluacion_imiv.prorroga_evaluacion_aoc,
            tiempo_a_calcular.tipo_plazo
    )
    if dias_plazo_aoc != tiempo_a_calcular.plazo_AOC or fecha_plazo_aoc != _fecha_plazo_aoc:
        fecha_plazo_aoc = _fecha_plazo_aoc
        dias_plazo_aoc = tiempo_a_calcular.plazo_AOC
    
    fecha_plazo_interesado = evaluacion_imiv.fecha_respuesta_interesado
    old_fecha_plazo_interesado = evaluacion_imiv.fecha_respuesta_interesado
    dias_plazo_interesado = evaluacion_imiv.dias_respuesta_interesado
    _fecha_plazo_interesado = None
    if evaluacion_imiv.fecha_respuesta is not None and tiempo_a_calcular.plazo_interesado > 0:
        _fecha_plazo_interesado = set_business_due_date_from_date(
                evaluacion_imiv.fecha_respuesta,
                tiempo_a_calcular.plazo_interesado + evaluacion_imiv.prorroga_respuesta_interesado,
                TiemposProyecto.DIAS_CORRIDOS
        )
        if dias_plazo_interesado != tiempo_a_calcular.plazo_interesado or fecha_plazo_interesado != \
                _fecha_plazo_interesado:
            fecha_plazo_interesado = _fecha_plazo_interesado
            dias_plazo_interesado = tiempo_a_calcular.plazo_interesado
    
    prorrogable_aoe = False
    prorrogable_aoc = False
    # Si el tiempo del estado de evaluación no es prorrogable se salta los cálculos
    if not tiempo_a_calcular_prorrogable:
        prorrogable = False
    
    if prorrogable is None and tiempo_a_calcular_prorrogable and evaluacion_imiv.estado_evaluacion.id in (
            EstadoEvaluacion.EN_TRAMITE, EstadoEvaluacion.EN_EVALUACION, EstadoEvaluacion.OBSERVADO) and (
            evaluacion_imiv.prorroga_evaluacion_aoe == 0 or evaluacion_imiv.prorroga_evaluacion_aoc == 0 or
            evaluacion_imiv.prorroga_respuesta_interesado == 0):
        
        # Calcula fecha de inicio y término de la ventana de prórroga
        # para el AOE
        fecha_prorroga_aoe_inicio = set_business_due_date_from_date(fecha_plazo_aoe, -12, TiemposProyecto.DIAS_HABILES)
        fecha_prorroga_aoe_fin = set_business_due_date_from_date(fecha_plazo_aoe, -3, TiemposProyecto.DIAS_HABILES)
        # para el AOC
        fecha_prorroga_aoc_inicio = set_business_due_date_from_date(fecha_plazo_aoc, -12, TiemposProyecto.DIAS_HABILES)
        fecha_prorroga_aoc_fin = set_business_due_date_from_date(fecha_plazo_aoc, -3, TiemposProyecto.DIAS_HABILES)
        # para el interesado
        fecha_prorroga_interesado_inicio = set_business_due_date_from_date(
                fecha_plazo_interesado, -12, TiemposProyecto.DIAS_HABILES
        )
        fecha_prorroga_interesado_fin = set_business_due_date_from_date(
                fecha_plazo_interesado, -3, TiemposProyecto.DIAS_HABILES
        )
        
        __business_due_date = get_business_due_date_from_today(0)
        
        # define si el proyecto es prorrogable
        # la ventana de solicitud de prórroga del AOE está abierta
        if fecha_prorroga_aoe_inicio is not None and fecha_prorroga_aoe_fin is not None:
            if fecha_prorroga_aoe_inicio <= __business_due_date <= fecha_prorroga_aoe_fin:
                prorrogable_aoe = True
        
        # la ventana de solicitud de prórroga del AOC está abierta
        if fecha_prorroga_aoc_inicio is not None and fecha_prorroga_aoc_fin is not None:
            if fecha_prorroga_aoc_inicio <= __business_due_date <= fecha_prorroga_aoc_fin:
                prorrogable_aoc = True
        
        # la ventana de solicitud de prórroga está abierta
        if fecha_prorroga_interesado_inicio is not None and fecha_prorroga_interesado_fin is not None:
            prorrogable = fecha_prorroga_interesado_inicio <= __business_due_date <= fecha_prorroga_interesado_fin
    
    return {
            "maximo_dias_prorroga_AOE": tiempo_a_calcular.plazo_AOE,
            "maximo_dias_prorroga_AOC": tiempo_a_calcular.plazo_AOC,
            "maximo_dias_prorroga_interesado": tiempo_a_calcular.plazo_interesado,
            "dias_de_plazo_AOE": dias_plazo_aoe + evaluacion_imiv.prorroga_evaluacion_aoe,
            "dias_de_plazo_AOC": dias_plazo_aoc + evaluacion_imiv.prorroga_evaluacion_aoc,
            "dias_de_plazo_interesado": dias_plazo_interesado + evaluacion_imiv.prorroga_respuesta_interesado,
            "fecha_plazo_AOE": fecha_plazo_aoe,
            "fecha_plazo_AOC": fecha_plazo_aoc,
            "old_fecha_plazo_AOC": old_fecha_plazo_aoc,
            "old_fecha_plazo_AOC_str": date_to_str_local(old_fecha_plazo_aoc, "%d/%m/%Y"),
            "fecha_plazo_interesado": fecha_plazo_interesado,
            "fecha_plazo_AOE_str": date_to_str_local(fecha_plazo_aoe, "%d/%m/%Y"),
            "fecha_plazo_AOC_str": date_to_str_local(fecha_plazo_aoc, "%d/%m/%Y"),
            "fecha_plazo_interesado_str": date_to_str_local(fecha_plazo_interesado, "%d/%m/%Y"),
            "prorrogable_aoe": prorrogable_aoe,
            "prorrogable_aoc": prorrogable_aoc,
            "prorrogable": prorrogable,
            "old_fecha_plazo_interesado": old_fecha_plazo_interesado,
            "old_fecha_plazo_interesado_str": date_to_str_local(old_fecha_plazo_interesado, "%d/%m/%Y")
    }
