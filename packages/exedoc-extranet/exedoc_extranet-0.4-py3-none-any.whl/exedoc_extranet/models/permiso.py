from django.db import models
from django.utils import timezone
from . import Usuario, Acceso, Region, Comuna, Zona


class Permiso(models.Model):
    """Modelo para administrar los permisos de los usuarios"""
    usuario = models.ForeignKey(Usuario, null=False, blank=False, related_name='permiso_usuario',
                                on_delete=models.DO_NOTHING)
    acceso = models.ForeignKey(Acceso, null=False, blank=False, related_name='permiso_acceso',
                               on_delete=models.DO_NOTHING)
    region_asignada = models.ForeignKey(Region, null=True, blank=True, related_name='permiso_region_asignada',
                                        on_delete=models.DO_NOTHING)
    comuna_asignada = models.ForeignKey(Comuna, null=True, blank=True, related_name='permiso_comuna_asignada',
                                        on_delete=models.DO_NOTHING)
    zona_asignada = models.ForeignKey(Zona, null=True, blank=True, related_name='permiso_zona_asignada',
                                      on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default=True)
    subrogante = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(null=False, default=timezone.now)

    @staticmethod
    def get_permiso_user(permiso_id, rut):
        permiso = None
        if Permiso.exists(permiso_id=permiso_id, usuario_id=rut):
            permiso = Permiso.objects.get(id=permiso_id, usuario_id=rut, estado=True)
        return permiso

    @staticmethod
    def exists(permiso_id: int or None, usuario_id: int or None) -> bool:
        if permiso_id is None or usuario_id is None:
            return False
        return Permiso.objects.filter(id=permiso_id, usuario_id=usuario_id, estado=True).exists()
