from django.shortcuts import render
from django.urls import path
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.contrib.auth.models import User
from .models import Expediente, PersonasIntervenientes, Actualizacion
# Create your views here.


#Todas las vistas requieren que haya un usado loggeado
def index(request):
    return render(request, 'index.html' )

#vista detalle de expediente
class ExpedienteListView(LoginRequiredMixin, generic.ListView):
    model = PersonasIntervenientes
    #queryset = PersonasIntervenientes.objects.filter(persona__user__username=request.user)
    template_name = "expediente_list.html"
    context_object_name = 'personas'

    #filtro para recibir los expedientes en los que participa el usuario
    def get_queryset(self):
        return PersonasIntervenientes.objects.filter(user__username=self.request.user)

class ExpedienteDetailView(LoginRequiredMixin, generic.ListView):
    model = Actualizacion
    context_object_name= 'expediente'
    template_name = "expediente_detail.html"

    #filtro para recibir los detalles del expediente y actualizaciones

    def get_queryset(self):
        return Actualizacion.objects.filter(expediente=self.kwargs['expediente'])

class ActualizacionDetailView(LoginRequiredMixin, generic.ListView):
    model = Actualizacion
    context_object_name=''