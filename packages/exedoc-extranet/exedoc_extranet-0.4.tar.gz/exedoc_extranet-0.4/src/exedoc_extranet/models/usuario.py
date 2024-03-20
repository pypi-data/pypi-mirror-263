"""Modelo para usuarios"""
from django.db import models

from . import Comuna, Acceso


class Usuario(models.Model):
    """Modelo para usuarios"""
    UsuarioTokenClaveUnica = None
    UsuarioTypeClaveUnica = None

    rut = models.IntegerField(primary_key=True)
    rut_dv = models.CharField(max_length=1, null=True, blank=True)
    nombres = models.CharField(max_length=100, null=True, blank=True)
    ap_paterno = models.CharField(max_length=100, null=True, blank=True)
    ap_materno = models.CharField(max_length=100, null=True, blank=True)
    # No existe en la maqueta
    direccion = models.CharField(max_length=200, null=True, blank=True)
    numero = models.CharField(max_length=30, null=True, blank=True)
    direccion_otro = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=50, null=True, blank=True)
    telefono = models.CharField(max_length=50, null=True, blank=True)
    # No existe en la maqueta
    cod_comuna = models.ForeignKey(Comuna, null=True, blank=True, related_name='usuario_comuna', on_delete=models.DO_NOTHING)
    nuevo = models.BooleanField(default=True)
    estado = models.BooleanField(default=True)
    permiso = models.ManyToManyField(
        Acceso,
        through='Permiso',
        through_fields=('usuario', 'acceso'),
        related_name="permisos"
    )
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    ultimo_acceso = models.DateTimeField(null=True)
    tipo_acceso = models.CharField(max_length=15, null=True, blank=True)

    class Meta:
        ordering = ['rut']

    def __str__(self):
        retorno = "{0}-{1}.".format(self.rut, self.rut_dv)
        return retorno

    @property
    def nombre_completo(self):
        """Devueve el nombre completo del usuario"""
        __names = self.nombres or ''
        __paterno = self.ap_paterno or ''
        __materno = self.ap_materno or ''
        __complete = "{0} {1} {2}".format(__names.strip() or 'Sin nombre', __paterno.strip(), __materno.strip())
        return __complete.strip()

    @property
    def cadena_de_confianza(self):
        """Devuelve una sigla formada por las primeras letras del nombre y los apellidos"""
        __names = self.nombres[0] if self.nombres.strip().__len__() > 0 else ''
        __paterno = self.ap_paterno[0] if self.ap_paterno.strip().__len__() > 0 else ''
        __materno = self.ap_materno[0] if self.ap_materno.strip().__len__() > 0 else ''
        return f"{__names.strip()}{__paterno.strip()}{__materno.strip()}"

    def __repr__(self):
        return "nombre: %s, email:%s" % (self.nombres, self.email)
