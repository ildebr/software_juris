from django.db.models.query import QuerySet
from django.http.response import Http404
from django.views.generic import ListView, DetailView

from juris.models import LegalRecord
import re


class LegalRecordListView(ListView):
    model = LegalRecord
    template_name = "expediente/list.html"
    context_object_name = "expedientes"


REGEX = re.compile(r"^([A-z0-9]{5})-([A-z0-9]{1})-(\d{4})-([A-z0-9]{2})-([A-z0-9]{6})$")


class LegalRecordDetailView(DetailView):
    model = LegalRecord
    template_name = "expediente/detail.html"
    context_object_name = "expediente"

    def get_object(self):
        queryset = self.get_queryset()

        code = self.kwargs.get("code")

        match = REGEX.match(code)

        if match is None:
            raise Http404(
                "La ruta no coincide con un codigo de %(verbose_name)s"
                % {"verbose_name": queryset.model._meta.verbose_name}
            )

        try:

            obj = queryset.filter(
                prosecutor_number=match[1],
                letter=match[2],
                start_date__year=match[3],
                court_number=match[4],
                record_number=match[5],
            ).get()
        except queryset.model.DoesNotExist:
            raise Http404(
                "No %(verbose_name)s found matching the query"
                % {"verbose_name": queryset.model._meta.verbose_name}
            )
            
        return obj
