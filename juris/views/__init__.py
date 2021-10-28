from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views import generic

from juris.models import Actualizacion


#Todas las vistas requieren que haya un usado loggeado
def index(request):
    return render(request, 'index.html')


class ActualizacionDetailView(LoginRequiredMixin, generic.ListView):
    model = Actualizacion
    context_object_name = ''
