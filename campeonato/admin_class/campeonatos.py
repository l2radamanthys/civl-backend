from django.contrib import admin
from campeonato.models.campeonatos import Campeonato


class CampeonatoAdmin(admin.ModelAdmin):
    model = Campeonato
    list_display = (
        'nombre',
    )

