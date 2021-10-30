from django.conf import settings
from django.forms import BoundField, Form, IntegerField
from django.http import HttpRequest
from django.shortcuts import redirect, render
from django.urls import reverse
from django.contrib import messages

from juris.models import LegalRecord


class CustomBoundField(BoundField):
    def label_tag(self, contents=None, attrs=None):
        attrs = {**(attrs or {}), "class": "form-label"}
        return super().label_tag(contents, attrs)


class SearchForm(Form):
    prosecutor_number = LegalRecord.prosecutor_number.field.formfield()
    letter = LegalRecord.letter.field.formfield()
    start_date__year = IntegerField(label="Año", min_value=1)
    court_number = LegalRecord.court_number.field.formfield()
    record_number = LegalRecord.record_number.field.formfield()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field in self.fields.values():
            field.widget.attrs.update({"class": "form-control"})

    def __getitem__(self, name):
        "Returns a BoundField with the given name."
        try:
            field = self.fields[name]
        except KeyError:
            raise KeyError("Key %r not found in Form" % name)
        return CustomBoundField(self, field, name)

    def find_legal_record(self):
        return LegalRecord.objects.get(
            start_date__year=self.cleaned_data["start_date__year"],
            prosecutor_number=self.cleaned_data["prosecutor_number"],
            court_number=self.cleaned_data["court_number"],
            letter=self.cleaned_data["letter"],
            record_number=self.cleaned_data["record_number"],
        )


def index(request: HttpRequest):
    if request.method == "POST":
        form = SearchForm(request.POST)
        re_captcha_token = request.POST.get("g-recaptcha-response", None)

        if form.is_valid():
            try:
                resultado = form.find_legal_record()
                return redirect(resultado.get_absolute_url())
            except LegalRecord.DoesNotExist:
                messages.add_message(
                    request,
                    messages.ERROR,
                    "No se encontro el expediente que busca.",
                )
    else:
        form = SearchForm()

    return render(
        request,
        "index.html",
        {"form": form, "RECAPTCHA_SITE_KEY": settings.RECAPTCHA_SITE_KEY},
    )
