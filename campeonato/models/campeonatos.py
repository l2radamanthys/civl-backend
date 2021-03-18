from django.db import models


class Campeonato(models.Model):
    nombre = models.CharField(max_length=200, default=None, blank=True, null=True)

    class Meta:
        db_table = 'campeonatos'
        verbose_name = "Campeonato"
        verbose_name_plural = "campeonatos"

    def __str__(self):
        return self.nombre
