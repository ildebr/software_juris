from django.views.generic import ListView, DetailView
from django.urls import path

from juris.models import Expediente


class ExpedienteListView(ListView):
    model = Expediente
    template_name = "expediente/list.html"
    context_object_name = 'expedientes'


class ExpedienteDetailView(DetailView):
    model = Expediente
    template_name = "expediente/detail.html"
