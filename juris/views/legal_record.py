from django.views.generic import ListView, DetailView

from juris.models import LegalRecord


class LegalRecordListView(ListView):
    model = LegalRecord
    template_name = "expediente/list.html"
    context_object_name = 'expedientes'


class LegalRecordDetailView(DetailView):
    model = LegalRecord
    template_name = "expediente/detail.html"
    context_object_name = 'expediente'
