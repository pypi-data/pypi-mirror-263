from django.db import models
from . import Proyecto, Ficha, Documentos


class Proyecto_Ficha(models.Model):
    id = models.AutoField(primary_key=True)
    proyecto_id = models.ForeignKey(Proyecto, related_name='proyecto_ficha_proyecto', on_delete=models.DO_NOTHING)
    ficha_id = models.ForeignKey(Ficha, related_name='proyecto_ficha_ficha', on_delete=models.DO_NOTHING)
    declaracion_proy_conjunto_documentos = models.ForeignKey(Documentos, null=True, blank=True,
                                                             related_name='declaracion_proy_conjunto_documentos_id',
                                                             on_delete=models.DO_NOTHING)
    estado_declaracion = models.CharField(max_length=1, null=True, blank=True)
    proyecto_principal = models.BooleanField(default=False)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)
    #direccion = models.charfield(null=True, blank=True)
    @staticmethod
    def get_proyecto(ficha_id):
        return Proyecto_Ficha.objects.filter(ficha_id_id=ficha_id).first().proyecto_id

    @staticmethod
    def get_proyectos(ficha_id):
        return [pry.proyecto_id for pry in Proyecto_Ficha.objects.filter(ficha_id_id=ficha_id)]

    @staticmethod
    def get_proyecto_principal(ficha_id):
        """Devuelve el proyecto principal de una ficha"""
        return Proyecto_Ficha.objects.filter(ficha_id_id=ficha_id, proyecto_principal=True).first()



