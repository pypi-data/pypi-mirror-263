from django.db import models


# noinspection SpellCheckingInspection,GrazieInspection
class TipoDocumentoSeim(models.Model):
    """Tipos de docuemntos SEIM"""

    class Meta:
        verbose_name = "Tipo de documento SEIM"
        verbose_name_plural = "Tipos de documentos SEIM"

    DECLJUR = "DECLJUR"
    CERING = "CERING"
    CERINGCORR = "CERINGCORR"
    OFICONVU = "OFICONVU"
    SOLPRO = "SOLPRO"
    RESPRORE = "RESPRORE"
    OFIRESVU = "OFIRESVU"
    OFIRESVUAD = "OFIRESVUAD"
    RESMUNEVA = "RESMUNEVA"
    RESSEREVA = "RESSEREVA"
    RESNOCOS = "RESNOCOS"
    RESNOCOM = "RESNOCOM"
    RESEVAC = "RESEVAC"
    RESMEVAOBS = "RESMEVAOBS"
    RESEVAOBS = "RESEVAOBS"
    RESEVAOBC = "RESEVAOBC"
    RESMEVAOBC = "RESMEVAOBC"
    CERSILS = "CERSILS"
    CERSILC = "CERSILC"
    CERINGM = "CERINGM"
    RESEVASM = "RESEVASM"
    RESEVACM = "RESEVACM"
    RESEVAOBSM = "RESEVAOBSM"
    RESEVAOBCM = "RESEVAOBCM"
    CERSUF = "CERSUF"
    OFISOLPRO = "OFISOLPRO"
    OTROSAD = "OTROSAD"
    SOLDES = "SOLDES"
    RESDES = "RESDES"
    RESDESM = "RESDESM"
    SIMS = "SIMS"
    SIMC = "SIMC"
    OFICATS = "OFICATS"
    OFICATC = "OFICATC"
    CEREXE462B = "CEREXE462B"
    CEREXE463 = "CEREXE463"
    CERVERSEM = "CERVERSEM"
    RESEVAD = "RESEVAD"
    PENDIENTE = "PENDIENTE"

    RESEAEPAP = "RESEAEPAP"
    RESEAEPRE = "RESEAEPRE"
    RESEAEPOB = "RESEAEPOB"

    ACTEAEPMUNAP = "ACTEAEPMUNAP"
    ACTEAEPMUNRE = "ACTEAEPMUNRE"
    ACTEAEPMUNOB = "ACTEAEPMUNOB"

    CEREAEPMUNAP = "CEREAEPMUNAP"
    CEREAEPMUNRE = "CEREAEPMUNRE"
    CEREAEPMUNOB = "CEREAEPMUNOB"

    RESEAEPDESIS = "RESEAEPDESIS"

    # CERTIFICADO INGRESO APORTE ESPACIO PUBLICO
    CERINGAP = 'CERINGAP'

    # OFICIO CONSULTA EVALUACION APORTE ESPACIO PUBLICO
    OFICONEAEP = "OFICONEAEP"

    # OFICIO DE OBSERVACIONES EAEP VU APORTE ESPACIO PUBLICO
    OFIOBSEAEP = "OFIOBSEAEP"

    DECLJURTRAN = "DECLJURTRAN"

    # RESOLUCIONES DE EVALUACIÓN INFORME DE SUFICIENCIA: OBSERVA Y RECHAZA/APRUEBA
    RESUFOB = "RESUFOB"
    RESUFAR = "RESUFAR"

    TIPOS_DOCUMENTO_SEIM = [
        (DECLJUR, {
            "codigo": "DECLJUR",
            "nombre": "Declaración jurada de ingreso"
        }),
        (CERING, {
            "codigo": "CERING",
            "nombre": "Certificado de ingreso"
        }),
        (CERINGCORR, {
            "codigo": "CERINGCORR",
            "nombre": "Certificado de ingreso IMIV Corregido"
        }),
        (OFICONVU, {
            "codigo": "OFICONVU",
            "nombre": "Oficio de consulta VU"
        }),
        (SOLPRO, {
            "codigo": "SOLPRO",
            "nombre": "Oficio solicitud prórroga"
        }),
        (RESPRORE, {
            "codigo": "RESPRORE",
            "nombre": "Resolución prórroga rechaza"
        }),
        (OFIRESVU, {
            "codigo": "OFIRESVU",
            "nombre": "Oficio respuesta VU"
        }),
        (OFIRESVUAD, {
            "codigo": "OFIRESVUAD",
            "nombre": "Adjunto Oficio respuesta VU"
        }),
        (RESEVAD, {
            "codigo": "RESEVAD",
            "nombre": "Adjunto resolución"
        }),
        (RESMUNEVA, {
            "codigo": "RESMUNEVA",
            "nombre": "Resolución Municipal evaluacion IMIV - aprueba/rechaza Simple"
        }),
        (RESSEREVA, {
            "codigo": "RESSEREVA",
            "nombre": "Resolución Seremitt evaluacion IMIV - aprueba/rechaza Simple"
        }),
        (RESNOCOM, {
            "codigo": "RESNOCOM",
            "nombre": "Resolución Municipal Rechazo No Corrección"
        }),
        (RESNOCOS, {
            "codigo": "RESNOCOS",
            "nombre": "Resolución Seremitt Rechazo No Corrección"
        }),
        (RESEVAC, {
            "codigo": "RESEVAC",
            "nombre": "Resolución evaluacion IMIV - aprueba/rechaza Conjunto"
        }),
        (RESEVAOBC, {
            "codigo": "RESEVAOBC",
            "nombre": "Resolución evaluacion IMIV - observado Conjunto"
        }),
        (RESMEVAOBS, {
            "codigo": "RESMEVAOBS",
            "nombre": "Resolución evaluacion IMIV - observado Simple Municipal"
        }),
        (RESEVAOBS, {
            "codigo": "RESEVAOBS",
            "nombre": "Resolución evaluacion IMIV - observado Simple"
        }),
        (RESMEVAOBC, {
            "codigo": "RESMEVAOBC",
            "nombre": "Resolución evaluacion IMIV - observado Conjunto Municipal"
        }),
        (CERSILS, {
            "codigo": "CERSILS",
            "nombre": "Certificado silencio positivo Simple"
        }),
        (CERSILC, {
            "codigo": "CERSILC",
            "nombre": "Certificado silencio positivo Conjunto"
        }),
        (CERINGM, {
            "codigo": "CERINGM",
            "nombre": "Certificado ingreso modificado"
        }),
        (RESEVASM, {
            "codigo": "RESEVASM",
            "nombre": "Resolución evaluacion IMIV - aprueba/rechaza (modificado) Simple"
        }),
        (RESEVACM, {
            "codigo": "RESEVACM",
            "nombre": "Resolución evaluacion IMIV - aprueba/rechaza (modificado) Conjunto"
        }),
        (RESEVAOBSM, {
            "codigo": "RESEVAOBSM",
            "nombre": "Resolución evaluacion IMIV - observado (modificado) Simple"
        }),
        (RESEVAOBCM, {
            "codigo": "RESEVAOBCM",
            "nombre": "Resolución evaluacion IMIV - observado (modificado) Conjunto"
        }),
        (CERSUF, {
            "codigo": "CERSUF",
            "nombre": "Certificado de suficiencia"
        }),
        (OFISOLPRO, {
            "codigo": "OFISOLPRO",
            "nombre": "Oficio aprobación prórroga"
        }),
        (RESDES, {
            "codigo": "RESDES",
            "nombre": "Resolución de desistimiento"
        }),
        (RESDESM, {
            "codigo": "RESDESM",
            "nombre": "Resolución de desistimiento Municipal"
        }),
        (SIMS, {
            "codigo": "SIMS",
            "nombre": "Simulación simple"
        }),
        (SIMC, {
            "codigo": "SIMC",
            "nombre": "Simulación conjunto"
        }),
        (OFICATS, {
            "codigo": "OFICATS",
            "nombre": "Oficio categorización simple"
        }),
        (OFICATC, {
            "codigo": "OFICATC",
            "nombre": "Oficio categorización conjunto"
        }),
        (CEREXE462B, {
            "codigo": "CEREXE462B",
            "nombre": "Certificado de exención 462 b"
        }),
        (CEREXE463, {
            "codigo": "CEREXE462B",
            "nombre": "Certificado de exención 463"
        }),
        (CERVERSEM, {
            "codigo": "CERVERSEM",
            "nombre": "Certificado de verificación de semejanza"
        }),
        (OTROSAD, {
            "codigo": "OTROSAD",
            "nombre": "Otros Adjuntos"
        }),
        (PENDIENTE, {
            "codigo": "PENDIENTE",
            "nombre": "Documento repetido, pendiente de reutilizar"
        }),

        (RESEAEPAP, {
            "codigo": "RESEAEPAP",
            "nombre": "Documento Adjunto para resolución de Aprobación"
        }),
        (RESEAEPRE, {
            "codigo": "RESEAEPRE",
            "nombre": "Documento Adjunto para resolución de Rechazo"
        }),
        (RESEAEPOB, {
            "codigo": "RESEAEPOB",
            "nombre": "Documento Adjunto para resolución Observada"
        }),

        (ACTEAEPMUNAP, {
            "codigo": "ACTEAEPMUNAP",
            "nombre": "Acta Concejo Municipal para resolución de Aprobación"
        }),
        (ACTEAEPMUNRE, {
            "codigo": "ACTEAEPMUNRE",
            "nombre": "Acta Concejo Municipal para resolución de Rechazo"
        }),
        (ACTEAEPMUNOB, {
            "codigo": "ACTEAEPMUNOB",
            "nombre": "Acta Concejo Municipal para resolución Observada"
        }),

        (CEREAEPMUNAP, {
            "codigo": "CEREAEPMUNAP",
            "nombre": "Certificado de Aprobación"
        }),
        (CEREAEPMUNRE, {
            "codigo": "CEREAEPMUNRE",
            "nombre": "Certificado de Rechazo"
        }),
        (CEREAEPMUNOB, {
            "codigo": "CEREAEPMUNOB",
            "nombre": "Certificado de Observación"
        }),
        (DECLJURTRAN, {
            "codigo": "DECLJURTRAN",
            "nombre": "Declaración jurada de ingreso"
        }),

        (RESEAEPDESIS, {
            "codigo": "RESEAEPDESIS",
            "nombre": "Documento Adjunto para Resolución de Aprobación de Desistimiento"
        }),
        (CERINGAP, {
            "codigo": "CERINGAP",
            "nombre": "Certificado Ingreso Aporte"
        }),

        (OFICONEAEP, {
            "codigo": "OFICONEAEP",
            "nombre": "Oficio de consulta de Órganos Competentes"
        }),
        (OFIOBSEAEP, {
            "codigo": "OFIOBSEAEP",
            "nombre": "Oficio de observaciones de Órganos Competentes VU"
        }),
        (SOLDES, {
            "codigo": "SOLDES",
            "nombre": "Solicitud de desistimiento"
        }),

        (RESUFOB, {
            "codigo": "RESUFOB",
            "nombre": "Resolución de observación de informe de suficiencia"
        }),
        (RESUFAR, {
            "codigo": "RESUFAR",
            "nombre": "Resolución de aprobación/rechazo de informe de suficiencia"
        })
    ]

    # Emisores de los documentos de SEIM
    EMISOR_SEIM = 'SEIM'
    EMISOR_AOEM = 'AOEM'  # AOE Municipalidad
    EMISOR_AOE = 'AOE'  # AOE Seremitt
    EMISOR_AOC = 'AOC'
    EMISOR_INTERESADO = 'INTERESADO'
    EMISOR_FOC = 'FOC'
    EMISOR_FOE = 'FOE'
    EMISORES = [
        (EMISOR_SEIM, 'SEIM'),
        (EMISOR_AOEM, 'AOEM'),
        (EMISOR_AOE, 'AOE'),
        (EMISOR_AOC, 'AOC'),
        (EMISOR_INTERESADO, 'INTERESADO'),
        (EMISOR_FOC, 'FOC'),
        (EMISOR_FOE, 'FOE'),
    ]
    TIPO_DOCUMENTO__CERTIFICADO = 'Certificado'
    TIPO_DOCUMENTO__OFICIO = 'Oficio'
    TIPO_DOCUMENTO__RESOLUCION = 'Resolucion'
    TIPO_DOCUMENTO__DECLARACION_JURADA = 'Declaracion Jurada'
    TIPO_DOCUMENTO__DOCUMENTO_DIGITAL = 'Documento digital'
    TIPOS_DOCUMENTO = [
        (TIPO_DOCUMENTO__CERTIFICADO, 'Certificado'),
        (TIPO_DOCUMENTO__OFICIO, 'Oficio'),
        (TIPO_DOCUMENTO__RESOLUCION, 'Resolucion'),
        (TIPO_DOCUMENTO__DECLARACION_JURADA, 'Declaracion Jurada'),
        (TIPO_DOCUMENTO__DOCUMENTO_DIGITAL, 'Documento digital')
    ]

    codigo = models.CharField(max_length=20, null=True, blank=True, unique=True)
    nombre = models.CharField(max_length=200, null=True, blank=True)
    multiple = models.BooleanField(default=False)
    forzar_nombre = models.BooleanField(default=False)
    mostrar_interesado = models.BooleanField(default=False)
    tipo_documento = models.CharField(
        max_length=20,
        choices=TIPOS_DOCUMENTO,
        default=TIPO_DOCUMENTO__DOCUMENTO_DIGITAL
    )
    emisor_documento = models.CharField(
        max_length=10,
        choices=EMISORES,
        default=EMISOR_SEIM
    )
    plantilla = models.CharField(max_length=200, null=True)
    file_name = models.CharField(max_length=100, null=True)

    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    es_adjunto = models.BooleanField(default=False)

    # noinspection PyBroadException
    @staticmethod
    def _get(codigo: str or None):
        return TipoDocumentoSeim.objects.get(codigo=codigo)

    # noinspection PyBroadException
    @staticmethod
    def get_obj(codigo: str or None):
        """Obtiene el objeto tipo de documento seim con el código"""
        return TipoDocumentoSeim._get(codigo)

    # noinspection PyBroadException
    @staticmethod
    def get_name(codigo: str or None):
        """Obtiene el nombre del tipo de documento seim con el código"""
        nombre = codigo
        try:
            nombre = TipoDocumentoSeim._get(codigo=codigo).nombre
        except:
            pass
        return nombre

    # noinspection PyBroadException
    @staticmethod
    def get_id(codigo: str or None):
        """Obtiene el ID del tipo de documento seim con el código"""
        _id = None
        try:
            _id = TipoDocumentoSeim._get(codigo=codigo).id
        except:
            pass
        return _id

    # noinspection PyBroadException
    @staticmethod
    def get_file_name(codigo: str or None):
        """Obtiene el nombre del archivo del tipo de documento seim con el código"""
        file_name = codigo
        try:
            file_name = TipoDocumentoSeim._get(codigo=codigo).file_name
        except:
            pass
        return file_name
