from django.db import models


class Categoria_Imiv(models.Model):
    EXENTO = "EXENTO"
    BASICO = "BASICO"
    INTERMEDIO = "INTERMEDIO"
    MAYOR = "MAYOR"
    COMPLEMENTARIO = "COMPLEMENTARIO"

    CATEGORIAS = [
        (EXENTO, 'EXENTO'),
        (BASICO, 'BASICO'),
        (INTERMEDIO, 'INTERMEDIO'),
        (COMPLEMENTARIO, 'COMPLEMENTARIO'),
        (MAYOR, 'MAYOR')
    ]
    nombre = models.CharField(max_length=30,
                              choices=CATEGORIAS,
                              default=EXENTO)
    descripcion = models.CharField(max_length=100, null=True, blank=True, default=None)
    constraints = [
        models.UniqueConstraint(
            fields=['nombre'],
            name='unique nombre de categorizacion'
        )
    ]

    def __str__(self):
        return f"{self.nombre}"

    def __repr__(self):
        return f"{self.descripcion}"

    @staticmethod
    def get_descripcion(nombre: str = "EXENTO"):
        """Obtiene la descripción de una categoría IMIV"""
        return Categoria_Imiv.objects.get(nombre=nombre).__repr__()

    @staticmethod
    def get_id(nombre: str = "EXENTO"):
        """Obtiene el ID de una categoría IMIV"""
        return Categoria_Imiv.objects.get(nombre=nombre).id

    @staticmethod
    def get_by_description(description: str = "Básico"):
        """Obtiene el id de una categoría IMIV"""
        return Categoria_Imiv.objects.filter(descripcion__icontains=description).first()
