"""Log de errores del sistema"""
from django.db import models


class LogSistema(models.Model):
    """Log de errores del sistema"""

    class Meta:
        verbose_name_plural = "Logs sistema"

    GET = 'GET'
    POST = 'POST'
    PUT = 'PUT'
    PATCH = 'PATCH'
    DELETE = 'DELETE'
    NONE = 'NONE'

    METHODS = [
        (GET, 'GET'),
        (POST, 'POST'),
        (PUT, 'PUT'),
        (PATCH, 'PATCH'),
        (DELETE, 'DELETE'),
        (NONE, 'NONE'),
    ]

    ERROR = 'ERROR'
    WARNING = 'WARNING'
    DEBUG = 'DEBUG'
    LOG = 'LOG'
    INFO = 'INFO'

    TIPOS = [
        (ERROR, 'ERROR'),
        (WARNING, 'WARNING'),
        (LOG, 'LOG'),
        (INFO, 'INFO'),
        (DEBUG, 'DEBUG'),
    ]

    UsuarioLogin = None
    UsuarioToken = None

    view = models.CharField(max_length=512)
    method = models.CharField(max_length=10, choices=METHODS, default=POST)
    function = models.CharField(max_length=512)
    log = models.TextField()
    trace = models.TextField(null=True)
    stack = models.TextField(null=True)
    params = models.JSONField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    usuario_ingreso_id = models.IntegerField(null=True, blank=True)
    usuario_ingreso_token = models.TextField(null=True)
    tipo_registro = models.CharField(max_length=10, choices=TIPOS, default=ERROR)
