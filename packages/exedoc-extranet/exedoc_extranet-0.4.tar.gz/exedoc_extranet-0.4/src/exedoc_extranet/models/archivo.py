import uuid
from exedoc_extranet.config import settings
from django.db import models


class Archivo(models.Model):
    """Modelo para manejar archivos físicos"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    content_type = models.CharField(max_length=100)
    data = models.FileField()
    data_base64 = models.TextField(null=True, blank=True)
    firmado = models.BooleanField(null=False, default=False)
    fecha_firmado = models.DateTimeField(null=True)
    folio = models.CharField(max_length=50, null=True)
    url_gdmtt = models.CharField(max_length=800, null=True)
    id_documento_gdmtt = models.CharField(max_length=30, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    token_firma = models.TextField(null=True)
    request_firma = models.TextField(null=True)
    def __str__(self):
        return f"{self.name}"

    def get_url(self):
        url = self.url_gdmtt if self.url_gdmtt is not None else f"{settings.URL_FILE_DOWNLOAD}{self.id}"
        # noinspection HttpUrlsUsage
        if 'http://' not in url and 'https://' not in url:
            # noinspection HttpUrlsUsage
            url = f'http://{url}'
        return url

    def set_file_name(self, tipo_documento_seim, identificador_proyecto):
        _nombre_archivo = self.name
        if tipo_documento_seim.forzar_nombre:
            _nombre_archivo = f'{tipo_documento_seim.file_name}_{identificador_proyecto}.pdf'
            self.name = _nombre_archivo
            self.save()
        return _nombre_archivo
