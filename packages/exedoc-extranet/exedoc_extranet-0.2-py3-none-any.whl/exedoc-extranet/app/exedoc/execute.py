import requests
import json
import traceback
from rest_framework import status
from app.exedoc.models import ( Archivo, SeimLogSistema, BorradorDocumentoEvaluacion, LogSistema, Ficha, Evaluacion_Imiv, TipoDocumentoSeim,
    EstadoEvaluacion, TipoIMIV, DocumentoEvaluacionImiv, Proyecto_Ficha, Analista_Competente_Ficha, Analista_Asignado, Permiso, Comuna,
    
)
from config.constants import (
    TIPO_FICHA_SIMPLE, ACCESO_SEREMITT_SEREMI, DOCTO_SEIM_RESOLUCION_SUFICIENCIA_OBSERVA,
    DOCTO_SEIM_RESOLUCION_SUFICIENCIA_APRUEBA_RECHAZA
)
from app.exedoc.helpers import (obtiene_titular_representante_proyecto, get_fecha_vencimiento_evaluacion, date_to_str_local)
from app.exedoc.services import responsable_departamento_exedoc
from config import settings
from config.settings import EMISOR_DOCUMENTO_EXEDOC

def firma_electronica_avanzada(
    ficha_id, 
    estado_evaluacion=None, 
    prorroga=False, 
    borrador: BorradorDocumentoEvaluacion = None
):
    print("Estoy en firma electronica avanzada")
    """Firma Electrónica Avanzada"""
    log_sistema = SeimLogSistema(__file__, LogSistema.NONE, 'firma_electronica_avanzada')
    log_sistema \
        .add_params('ficha_id', ficha_id) \
        .add_params('estado_evaluacion', estado_evaluacion) \
        .info('Inicia función de firma electrónica avanzada')
    if not Ficha.objects.filter(id=ficha_id).exists():
        print("Ficha no existe")
        log_sistema.error("La ficha no existe")
        raise Ficha.DoesNotExist

    o_ficha = Ficha.objects.get(id=ficha_id)
    log_sistema.add_params("o_ficha", o_ficha)

    if not Evaluacion_Imiv.objects.filter(imiv_id=o_ficha.id, vigente=True).exists():
        print("La evaluacion no existe")
        log_sistema.error("La evaluacion no existe")
        raise Evaluacion_Imiv.DoesNotExist

    #print("Sali de los if de firma electrónica avanzada")
    o_evaluacion = Evaluacion_Imiv.objects.get(imiv_id=o_ficha.id, vigente=True)
    print(f'o_evaluacion es {o_evaluacion}')
    log_sistema.info("firma_electronica_avanzada: se encontró la evaluacion")

    if prorroga:
        #print("Estoy en el if de prórroga")
        tipo_documento_seim = TipoDocumentoSeim.RESPRORE
        log_sistema \
            .add_params("es_prorroga", True)

    elif not EstadoEvaluacion.objects.filter(id=estado_evaluacion).exists():
        print("El estado de evaluacion no existe")
        log_sistema.error("El estado de evaluacion no existe")
        raise EstadoEvaluacion.DoesNotExist

    else:
        #print("Estoy en el if de estado evaluacion")
        if estado_evaluacion == EstadoEvaluacion.RESOLUCION_OBSERVADO:
            log_sistema.add_params("es_observado", True)
            if o_evaluacion.imiv.tipo_imiv_id == TipoIMIV.TIPO_IMIV_INFORME_SUFICIENCIA:
                tipo_documento_seim = DOCTO_SEIM_RESOLUCION_SUFICIENCIA_OBSERVA
            else:
                tipo_documento_seim = TipoDocumentoSeim.RESEVAOBS if o_ficha.tipo_ficha == TIPO_FICHA_SIMPLE else \
                    TipoDocumentoSeim.RESEVAOBC
        elif estado_evaluacion in [EstadoEvaluacion.RESOLUCION_APROBADO, EstadoEvaluacion.RESOLUCION_RECHAZADO]:
            if o_evaluacion.imiv.tipo_imiv_id == TipoIMIV.TIPO_IMIV_INFORME_SUFICIENCIA:
                tipo_documento_seim = DOCTO_SEIM_RESOLUCION_SUFICIENCIA_APRUEBA_RECHAZA
            else:
                tipo_documento_seim = TipoDocumentoSeim.RESSEREVA if o_ficha.tipo_ficha == TIPO_FICHA_SIMPLE else \
                    TipoDocumentoSeim.RESEVAC
        elif estado_evaluacion == EstadoEvaluacion.RESOLUCION_DESISTIDO:
            tipo_documento_seim = TipoDocumentoSeim.RESDES
        elif estado_evaluacion == EstadoEvaluacion.RECHAZADO_NO_CORRECCION:
            tipo_documento_seim = TipoDocumentoSeim.RESNOCOS
        else:
            log_sistema.error("Estado de evaluación no implementado para firma electrónica avanzada")
            raise TipoDocumentoSeim.DoesNotExist
    print(f"tipo documento seim es {tipo_documento_seim}")
    log_sistema.add_params('tipo_documento_seim', tipo_documento_seim).info(f'FEA: el documento es {tipo_documento_seim}')

    if DocumentoEvaluacionImiv.objects.filter(
            evaluacion_imiv=o_evaluacion,
            tipo_documento_seim=TipoDocumentoSeim.get_id(tipo_documento_seim),
            vigente=True
    ).exists():
        print("El documento evaluacion imiv existe")
        log_sistema.info('El documento evaluacion imiv existe')
        o_documento_evaluacion_imiv = DocumentoEvaluacionImiv.objects.get(
            evaluacion_imiv=o_evaluacion,
            tipo_documento_seim=TipoDocumentoSeim.get_id(tipo_documento_seim),
            vigente=True
        )
        o_archivo = o_documento_evaluacion_imiv.documento.file

    elif borrador is not None:
        log_sistema.add_params("es_borrador", True)
        o_archivo = borrador.archivo

    else:
        print("No existe documento para enviar a firmar")
        log_sistema.error("No existe documento para enviar a firmar")
        raise DocumentoEvaluacionImiv.DoesNotExist
    
    print("firma_electronica_avanzada: se encontró el documento")
    log_sistema.add_params("o_archivo", o_archivo).info('firma_electronica_avanzada: se encontró el documento')
    # Distribución externa
    l_distribucion_externa = set([])

    # Interesado
    if o_ficha.tipo_ficha == TIPO_FICHA_SIMPLE:
        o_proyecto_ficha = Proyecto_Ficha.objects.filter(ficha_id=o_ficha).first()
        print('firma_electronica_avanzada: es proyecto simple')
        log_sistema.info('firma_electronica_avanzada: es proyecto simple')

    else:
        print('firma_electronica_avanzada: es proyecto conjunto')
        o_proyecto_ficha = Proyecto_Ficha.objects.filter(ficha_id=o_ficha, proyecto_principal=True).first()
        log_sistema.info('firma_electronica_avanzada: es proyecto conjunto')

    personas = obtiene_titular_representante_proyecto(o_proyecto_ficha.proyecto_id.rut_pertenece)
    if personas['titular'] is not None:
        print('firma_electronica_avanzada: El titular no es None')
        l_distribucion_externa.add(personas['titular']['nombre_completo'])

    if personas['responsable'] is not None:
        print('firma_electronica_avanzada: El responsable no es None')
        l_distribucion_externa.add(personas['responsable']['nombre_completo'])

    # AOC
    for aoc in Analista_Competente_Ficha.objects.filter(evaluacion_imiv=o_evaluacion).exclude(usuario_respuesta=None):
        print(f'firma_electronica_avanzada: Se añade el AOC {aoc} a la lista de distribución')
        l_distribucion_externa.add(aoc.usuario_respuesta.nombre_completo)

    # AOE
    o_analista_asignado = Analista_Asignado.objects.filter(evaluacion_imiv=o_evaluacion, vigente=True).first()
    print(f'firma_electronica_avanzada: Se añade el AOE {o_analista_asignado} a la lista de distribución y la cadena de confianza')
    l_distribucion_externa.add(o_analista_asignado.usuario.nombre_completo)
    l_cadena_confianza_seim = o_analista_asignado.usuario.cadena_de_confianza

    # revisor
    # Solo seremi
    revisor = Permiso.objects.filter(
        acceso_id=ACCESO_SEREMITT_SEREMI,
        region_asignada=o_evaluacion.imiv.region_evaluador,
        usuario__estado=True,
        estado=True
    ).first()
    if Comuna.objects.filter(provincia__region=o_evaluacion.imiv.region_evaluador, es_capital_regional=True).exists():
        l_ciudad = Comuna.objects.filter(
            provincia__region=o_evaluacion.imiv.region_evaluador, es_capital_regional=True
        ).first().nombre
    else:
        l_ciudad = ""

    l_organizacion_seim = revisor.region_asignada.nombre_formal.upper()
    l_tipo_materia = 107

    l_distribucion_externa.add(revisor.usuario.nombre_completo)

    l_distribucion_externa.add("Biblioteca")
    l_distribucion_externa.add("Gobierno Transparente")
    l_distribucion_externa_str = ' \n'.join(str(e) for e in l_distribucion_externa)

    l_emisor = EMISOR_DOCUMENTO_EXEDOC

    l_materia = TipoDocumentoSeim.get_name(tipo_documento_seim)
    l_id = TipoDocumentoSeim.get_id(tipo_documento_seim)
    fechas_plazo = get_fecha_vencimiento_evaluacion(o_evaluacion.id)
    l_plazo_firma = date_to_str_local(fechas_plazo["fecha_plazo_AOE"], "%Y-%m-%d %H:%M:%S")

    l_url_callback = f"{settings.URL_CALLBACK_EXEDOC}{l_id}/{o_archivo.id}/"
    log_sistema.add_params('l_url_callback', l_url_callback).info(f'FEA: el callback es {l_url_callback}')
    l_nombre_archivo = o_archivo.name

    l_numero_expediente = o_evaluacion.imiv.ficha.expediente
    log_sistema.add_params('l_numero_expediente', l_numero_expediente).info(f'FEA: el nro de expediente es {l_numero_expediente}')

    l_version_doc = 1
    # TODO  Versión de documento, en un inicio es 1

    responsable = responsable_departamento_exedoc(o_evaluacion.imiv)
    l_firmante = responsable["email"].split("@")[0]
    

    l_firma_acotada = True if tipo_documento_seim not in [TipoDocumentoSeim.RESDES, TipoDocumentoSeim.RESNOCOM, TipoDocumentoSeim.RESNOCOS] else False

    request_json = {
        "emisor": "seim",
        "documento": {
            "autor": "seim",
            "tipoDocumento": 104,
            "tipoMateria": l_tipo_materia,
            "reservado": False,
            "actosEfectosTerceros": False,
            "antecedentes": "Sin antecedentes",
            "materia": l_materia,
            "emisor": l_emisor,
            "ciudad": l_ciudad,
            "versionDoc": l_version_doc,
            "plazoFirma": l_plazo_firma,
            "firmaAcotada": l_firma_acotada,
            "fechaTope": l_plazo_firma,
            "urlCallbackSeim": l_url_callback,
            "destinatario": ["Expediente IMIV"],
            "dataArchivo": o_archivo.get_url(),
            "nombreArchivo": l_nombre_archivo,
            "contentType": "application/pdf",
            "visadores": [],
            "firmantes": [{
                "usuario": l_firmante,
                "esGrupo": False,
                "orden": "1"
            }],
            "distribucion": [],
            "organizacionSeim": l_organizacion_seim,
            "cadenaConfianzaSeim": l_cadena_confianza_seim,
            "distribucionExterna": l_distribucion_externa_str
        },
        "destinatario": [{
            "usuario": l_firmante,
            "copia": False
        }],
        "observacion": [{
            "texto": "Sin observaciones",
            "adjuntadoPor": "seim"
        }]
    }
    if l_numero_expediente:
        request_json["documento"].update(
            {
                "numeroExpediente": l_numero_expediente
            }
        )
    print('firma_electronica_avanzada: request enviado', request_json)
    log_sistema.add_params('request_json', request_json).info('FEA: Los parametros de la firma avanzada')

    o_archivo.request_firma = request_json
    o_archivo.save()

    print(f'firma_electronica_avanzada: call inyectar_doc_exedoc({ficha_id}, {o_archivo}, {log_sistema.to_dict()})')
    return inyectar_doc_exedoc(ficha_id, o_archivo, log_sistema)


def inyectar_doc_exedoc(
    ficha_id: str, 
    o_archivo: Archivo, 
    log_params: SeimLogSistema
):
    """Realiza la llamada d GDMTT/EXEDOC"""
    log_params \
        .add_params("ficha_id", ficha_id) \
        .add_params("request_firma", o_archivo.request_firma) \
        .info("Se inicia la llamada a EXEDOC, en inyectar_doc_exedoc()")
    try:
        print("-----------")
        print("Entre al try de firma electronica avanzada")
        response_firma = requests.post(settings.URL_FIRMA_EXEDOC, json=o_archivo.request_firma)
        print(f"El url que se esta usando es {settings.URL_FIRMA_EXEDOC}")
        print("---------")
        log_params \
            .add_params('url', settings.URL_FIRMA_EXEDOC) \
            .info("Vuelve de EXEDOC, en inyectar_doc_exedoc()")
        print("Arme los params de log de firma electrónica avanzada y escribi un log")
        if response_firma.status_code == 200:
            #print("Estoy en el if de resultado = 200")
            response_request = json.loads(response_firma.text)
            log_params \
                .add_params("response_request", response_request) \
                .add_params("data", response_request) \
                .add_params("status", response_firma.status_code) \
                .add_params("URL_GDMTT", settings.URL_FIRMA_EXEDOC)
            log_params.info("Se guarda el archivo recibido y retornan respuesta")
            return {
                "data": response_request,
                "status": response_firma.status_code,
                "URL_GDMTT": settings.URL_FIRMA_EXEDOC
            }
        else:
            print("Ocurrió un envío con error a exedoc")
            log_params \
                .add_params("response_firma", response_firma) \
                .add_params("response_firma.status_code", response_firma.status_code) \
                .warning('Envío con error a EXEDOC')

            if response_firma.status_code == 404:
                print("Estpy en error 404")
                mensaje = "No pudo firmar"
                log_params.info(f"{mensaje}, error {status.HTTP_404_NOT_FOUND}")
                return {
                    "data": mensaje,
                    "status": status.HTTP_404_NOT_FOUND
                }
            elif response_firma.status_code == 500:
                print("Estoy en error 500")
                mensaje = "Falló la firma"
                log_params.info(f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}")
                return {
                    "data": mensaje,
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
            elif response_firma.status_code > 400:
                mensaje = "Falló la firma"
                log_params.info(f"{mensaje}, error {status.HTTP_500_INTERNAL_SERVER_ERROR}")
                return {
                    "data": mensaje,
                    "status": status.HTTP_500_INTERNAL_SERVER_ERROR
                }
    except Exception as exception:
        log = f'Se produjo intentar firmar documento de ficha: {ficha_id}'
        log_params \
            .add_params('exception', exception.__str__()) \
            .add_params('mensaje', log) \
            .set_traceback('\n '.join(traceback.format_exc().splitlines()), ''.join(traceback.format_stack())) \
            .error(f'Fallo no controlado en la llamada de exedoc, se devuelve un error {status.HTTP_400_BAD_REQUEST}')
        return {
            "status": status.HTTP_400_BAD_REQUEST,
            "data": log,
        }
