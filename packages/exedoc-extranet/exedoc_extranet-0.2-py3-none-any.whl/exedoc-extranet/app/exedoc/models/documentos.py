from django.db import models

from . import Archivo, LogSistema
from app.exedoc.services.set_log_sistema import set_log_sistema


class Documentos(models.Model):
    """Modelo para el manejo de documentos lógicos dentro del sistema"""
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    referencia_documento = models.CharField(max_length=800, null=True)
    fecha_ingreso = models.DateTimeField(null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    file = models.ForeignKey(Archivo, on_delete=models.DO_NOTHING, null=True, blank=True)
    folio = models.CharField(max_length=50, null=True)
    esPlano = models.BooleanField(null=True, default=False, editable=True)
    estaTimbrado = models.BooleanField(null=True, default=False, editable=True)


    def __str__(self):
        retorno = "{0}".format(self.nombre)
        return retorno

    @staticmethod
    def delete_document(file_id):
        """Borra un archivo subido al sistema"""
        log = 'ok'
        try:
            Documentos.objects.filter(file_id=file_id).delete()
            Archivo.objects.filter(id=file_id).delete()
        except Documentos.DoesNotExist:
            log = f'El documento con file_id {file_id} no existe'
        except Archivo.DoesNotExist:
            log = f'El archivo con file_id {file_id} no existe'
        if log != 'ok':
            set_log_sistema(__file__, LogSistema.NONE, 'delete_document', log)
        return log == 'ok'
