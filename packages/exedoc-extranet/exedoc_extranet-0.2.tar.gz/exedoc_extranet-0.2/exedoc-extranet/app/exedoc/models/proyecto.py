from django.db import models
from . import Tipo_Tramite, Comuna, Direccion_Rol, Usuario


class Proyecto(models.Model):
    id = models.AutoField(primary_key=True)
    identificador = models.CharField(max_length=12, null=True, blank=True)
    tipo_tramite = models.ForeignKey(Tipo_Tramite, related_name='proyecto_Tipo_Tramite', on_delete=models.DO_NOTHING)
    nombre = models.CharField(max_length=100, null=True, blank=True)
    comuna_cod_comuna = models.ForeignKey(Comuna, related_name='proyecto_Comuna', on_delete=models.DO_NOTHING)
    total_terreno = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    superficie_util = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    superficie_edificada = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    latitud = models.DecimalField(
        max_digits=10, decimal_places=7, null=True, blank=True)
    longitud = models.DecimalField(
        max_digits=10, decimal_places=7, null=True, blank=True)
    rol_fusion = models.CharField(max_length=1, null=True, blank=True)
    # proyecto_padre_id se apunta a si mismo opcional
    proyecto_padre_id = models.ForeignKey("self", null=True, blank=True, on_delete=models.SET_NULL)
    proposito = models.CharField(max_length=1, null=True, blank=True)
    tipo_crecimiento = models.CharField(max_length=20, null=True, blank=True)
    direccion_principal = models.ForeignKey(Direccion_Rol, null=True, blank=True, related_name='proyecto_direccion_rol',
                                            on_delete=models.SET_NULL)
    usuario_creador = models.ForeignKey(Usuario, null=True, blank=True, related_name='proyecto_usuario',
                                        on_delete=models.SET_NULL)
    rut_pertenece = models.CharField(max_length=45, null=True, blank=True)
    descripcion = models.CharField(max_length=800, null=True, blank=True)
    colinda_camino_publico = models.CharField(max_length=1, null=True, blank=True)
    colinda_red_vial_basica = models.CharField(max_length=1, null=True, blank=True)
    colinda_via_urbana = models.CharField(max_length=1, null=True, blank=True)
    estado = models.CharField(max_length=20, null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    superficie_util_edificada_subterranea = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    superficie_util_edificada_sobre_terreno = models.DecimalField(max_digits=13, decimal_places=3, null=True,
                                                                  blank=True)
    superficie_comun_edificada_subterranea = models.DecimalField(max_digits=13, decimal_places=3, null=True, blank=True)
    superficie_comun_edificada_sobre_terreno = models.DecimalField(max_digits=13, decimal_places=3, null=True,
                                                                   blank=True)
    tipo_creador = models.CharField(max_length=30, null=True, blank=True)  # PERSONA_NATURAL, PERSONA_JURIDICA
    aporte_espacio_publico = models.BooleanField(null=True, default=False)
    cup = models.CharField(max_length=100, null=True, blank=True)
    cup_valido = models.BooleanField(null=True)
    ms_entry_id = models.IntegerField(blank=True, null=True)
    ms_application_id = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.nombre
