from django.contrib import admin
from campeonato.models.carreras import Carrera


class CarreraAdmin(admin.ModelAdmin):
    model = Carrera
    list_display = (
        'nombre',
    )

