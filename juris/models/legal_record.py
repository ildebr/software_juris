from django.db.models import CASCADE, CharField, DateField, ForeignKey, Model
from django.db.models.fields.related import ManyToManyField
from django.urls import reverse
from juris.models.part import Part

from juris.models.person import Person
from juris.models.proceeding import Proceeding


class LegalRecord(Model):
    start_date = DateField("fecha de inicio")
    end_date = DateField("fecha de conclusión", blank=True, null=True)
    prosecutor_number = CharField("número de fiscalía", max_length=5)
    court_number = CharField("número del tribunal", max_length=2)
    record_number = CharField("número de expediente", max_length=6)
    letter = CharField("letra", max_length=1)
    termination_reason = CharField("motivo de conclusión", max_length=100, blank=True)
    summary = CharField("resumen del caso", max_length=100, blank=True)

    parts = ManyToManyField(Person, through=Part, related_name="legal_records")

    class Meta:
        verbose_name = "expediente"
        verbose_name_plural = "expedientes"

        # Los campos especificados en unique_together son para
        # que no hayan dos expedientes iguales
        unique_together = (
            "prosecutor_number",
            "court_number",
            "record_number",
            "letter",
        )

    @property
    def code(self):
        return self.get_code()

    def get_code(self):
        return f"{self.prosecutor_number}-{self.letter}-{self.start_date.year}-{self.court_number}-{self.record_number}"

    def __str__(self):
        return self.get_code()

    def get_absolute_url(self):
        return reverse("legal_record_detail", kwargs={"code": self.get_code()})
