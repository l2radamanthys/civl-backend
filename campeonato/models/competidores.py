from django.db import models


class Competidor(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    apellido = models.CharField(max_length=200, default=None, blank=True, null=True)
    dni = models.CharField(max_length=20, default=None, blank=True, null=True)
    telefono = models.CharField(max_length=20, default=None, blank=True, null=True)
    email = models.CharField(max_length=100, default=None, blank=True, null=True)

    class Meta:
        db_table = 'competidores'
        verbose_name = "Competidor"
        verbose_name_plural = "competidores"

    def __str__(self):
        return self.nombre
