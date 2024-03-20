from app.exedoc.utils import Rut
from app.exedoc.models import Persona_Juridica, Persona_Juridica_Usuario, Usuario
from config import constants


def obtiene_titular_representante_proyecto(rut_pertenece):
    """Obtiene Titular y representante del proyecto"""
    personas = {
        "responsable": None,
        "titular": None
    }
    persona_juridica = Persona_Juridica.objects \
        .filter(rut=rut_pertenece) \
        .first()
    if persona_juridica:
        persona_juridica_usuario = Persona_Juridica_Usuario.objects \
            .filter(persona_juridica_rut=persona_juridica,
                    tipo_participacion_id=2,
                    estado=Persona_Juridica_Usuario.VIGENTE) \
            .first()
        if persona_juridica_usuario:
            personas['responsable'] = {
                'rut_sin_formato': f'{persona_juridica_usuario.usuario_rut.rut}',
                'rut': f'{Rut(persona_juridica_usuario.usuario_rut.rut).__repr__()}',
                'nombre_completo': '{0} {1} {2}'.format(persona_juridica_usuario.usuario_rut.nombres,
                                                        persona_juridica_usuario.usuario_rut.ap_paterno,
                                                        persona_juridica_usuario.usuario_rut.ap_materno),
                'nombres': persona_juridica_usuario.usuario_rut.nombres,
                'paterno': persona_juridica_usuario.usuario_rut.ap_paterno,
                'materno': persona_juridica_usuario.usuario_rut.ap_materno,
                'email': persona_juridica_usuario.email.email,
                'tipo': constants.PERSONA_NATURAL
            }
        personas["titular"] = {
            'rut_sin_formato': f'{persona_juridica.rut}',
            'rut': f'{Rut(persona_juridica.rut)}',
            'nombre_completo': persona_juridica.razon_social,
            'nombres': persona_juridica.razon_social,
            'paterno': '-',
            'materno': '-',
            'email': persona_juridica.email,
            'tipo': constants.PERSONA_JURIDICA

        }

    else:
        persona = Usuario.objects \
            .filter(rut=rut_pertenece) \
            .first()
        personas['titular'] = {
            'rut_sin_formato': f'{persona.rut}',
            'rut': f'{Rut(persona.rut)}',
            'nombre_completo': '{0} {1} {2}'.format(persona.nombres,
                                                    persona.ap_paterno,
                                                    persona.ap_materno),
            'nombres': persona.nombres,
            'paterno': persona.ap_paterno,
            'materno': persona.ap_materno,
            'email': persona.email,
            'tipo': constants.PERSONA_NATURAL
        }
    return personas
