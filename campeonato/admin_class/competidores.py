from django.contrib import admin
from campeonato.models.competidores import Competidor


class CompetidorAdmin(admin.ModelAdmin):
    model = Competidor
    list_display = (
        'nombre',
    )

