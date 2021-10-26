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
        return PersonasIntervenientes.objects.filter(persona__user__username=self.request.user)

#vista detalle de expediente
class ExpedienteDetailView(LoginRequiredMixin, generic.DetailView):
    model = Actualizacion

    context_object_name="object"
    template_name="actualizacion_detail.html"

    # def get_queryset(self):
        # pp = Actualizacion.objects.filter(expediente=self.kwargs['pk'])

        # return Actualizacion.objects.filter(expediente=pp.expediente)
    def get_queryset(self):
        return Actualizacion.objects.filter(expediente__numero_de_fiscalia='FP12')
    

class ActualizacionListView(LoginRequiredMixin, generic.ListView):
    model = Actualizacion

    def get_queryset(self):
        return Actualizacion.objects.filter(expediente=1)