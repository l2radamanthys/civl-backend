from django.db import models


class Carrera(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)
    fecha = models.DateField(default=None, null=True, blank=True)

    class Meta:
        db_table = 'carreras'
        verbose_name = "Carrera"
        verbose_name_plural = "Carreras"

    def __str__(self):
        return self.nombre
