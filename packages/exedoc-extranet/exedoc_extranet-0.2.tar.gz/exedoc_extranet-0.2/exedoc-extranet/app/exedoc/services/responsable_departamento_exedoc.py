from app.exedoc.utils import Rut
from app.exedoc.models import Permiso, Perfil
from app.exedoc.models.imiv import Imiv


def responsable_departamento_exedoc(imiv: Imiv):
    
    _filtro = {
        'estado': True,
        'region_asignada': imiv.region_evaluador,
        'comuna_asignada': imiv.comuna_evaluador,
        'acceso__perfil__id': Perfil.SEREMI if imiv.departamento_evaluador.cobertura == 'REGIONAL' else Perfil.DIRECTOR_TRANSITO,
        'subrogante': False,
        'usuario__estado': True
    }
    _filtro.pop('comuna_asignada' if imiv.departamento_evaluador.cobertura == 'REGIONAL' else 'region_asignada')
    
    o_encargado_departamento = Permiso.objects.filter(**_filtro).first()
    
    return {
        "rut": Rut(o_encargado_departamento.usuario.rut).__repr__(),
        "nombre_completo": o_encargado_departamento.usuario.nombre_completo,
        "email": o_encargado_departamento.usuario.email
    }
