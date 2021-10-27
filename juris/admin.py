from django.contrib import admin
from django.contrib.auth.models import User
from .models import Expediente, PersonasIntervenientes, Actualizacion
# Register your models here.


# admin.site.register(Expediente)
# admin.site.register(PersonasIntervenientes)
# admin.site.register(Actualizacion)

class ActualizacionInline(admin.TabularInline):
    model = Actualizacion
    extra = 0

class PersonasIntervenientesInline(admin.TabularInline):
    model = PersonasIntervenientes
    extra = 0

@admin.register(Expediente)
class ExpedienteAdmin(admin.ModelAdmin):
    inlines = [ActualizacionInline, PersonasIntervenientesInline]

@admin.register(PersonasIntervenientes)
class PersonasIntervenientesAdmin(admin.ModelAdmin):
    pass

@admin.register(Actualizacion)
class ActualizacionAdmin(admin.ModelAdmin):
    pass