from django.db import models
from . import Usuario


class Email_Usuario(models.Model):
    email = models.CharField(max_length=250)
    usuario = models.ForeignKey(Usuario, related_name='usuario', on_delete=models.DO_NOTHING)
    estado = models.BooleanField(default=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True, null=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, null=True)

    constraints = [
        models.UniqueConstraint(
            fields=['usuario', 'email'],
            name='unique email de usuario'
        )
    ]

    class Meta:
        unique_together = (("usuario", "email"),)

