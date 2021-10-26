from django.contrib import admin
from django.contrib.auth.models import User
from .models import Profile, Expediente, PersonasIntervenientes, Actualizacion
# Register your models here.

admin.site.register(Profile)
admin.site.register(Expediente)
admin.site.register(PersonasIntervenientes)
admin.site.register(Actualizacion)
