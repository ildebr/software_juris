from django.db.models import OuterRef, Subquery
from django.http.response import Http404
from django.views.generic import ListView, DetailView

from juris.models import LegalRecord, Part, legal_record
import re


class LegalRecordListView(ListView):
    model = LegalRecord
    template_name = "expediente/list.html"
    context_object_name = "expedientes"


class LegalRecordDetailView(DetailView):
    model = LegalRecord
    template_name = "expediente/detail.html"
    context_object_name = "expediente"

    def get_object(self):
        code = self.kwargs.get("code")
        try:
            return self.model.get_by_code(code)
        except LegalRecord.DoesNotExist:
            raise Http404(
                "No %(verbose_name)s found matching the query"
                % {"verbose_name": LegalRecord._meta.verbose_name}
            )

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        legal_record = context["expediente"]

        context["parts"] = map(
            lambda person: [
                person,
                person.part_set.get(legal_record=legal_record).get_type_display(),
            ],
            legal_record.parts.all(),
        )

        context["proceedings"] = legal_record.proceeding_set.all()

        return context
