import re

from django.db.models import CharField, DateField, Manager, ManyToManyField, Model
from django.urls import reverse

from juris.models.person import Person

REGEX = re.compile(r"^([A-z0-9]{5})-([A-z0-9]{1})-(\d{4})-([A-z0-9]{2})-([A-z0-9]{6})$")


class LegalRecordManager(Manager):
    def get_by_code(self, code: str):

        match = REGEX.match(code)

        if match is None:
            raise self.model.DoesNotExist(
                "%s matching query does not exist." % self.model._meta.object_name
            )

        return self.get(
            prosecutor_number=match[1],
            letter=match[2],
            start_date__year=match[3],
            court_number=match[4],
            record_number=match[5],
        )


class LegalRecord(Model):
    objects = LegalRecordManager()

    start_date = DateField("fecha de inicio")
    end_date = DateField("fecha de conclusión", blank=True, null=True)
    prosecutor_number = CharField("número de fiscalía", max_length=5)
    court_number = CharField("número del tribunal", max_length=2)
    record_number = CharField("número de expediente", max_length=6)
    letter = CharField("competencia", max_length=1)
    termination_reason = CharField("motivo de conclusión", max_length=100, blank=True)
    summary = CharField("resumen del caso", max_length=100, blank=True)

    parts = ManyToManyField("Person", through="Part", related_name="legal_records")

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

    @classmethod
    def get_by_code(cls, code: str):
        return cls._default_manager.get_by_code(code)

    def get_code(self):
        return f"{self.prosecutor_number}-{self.letter}-{self.start_date.year}-{self.court_number}-{self.record_number}"

    def __str__(self):
        return self.get_code()

    def get_absolute_url(self):
        return reverse("legal_record_detail", kwargs={"code": self.get_code()})

    def get_person_part_type_display(self, person: "Person"):
        return person.part_set.get(legal_record=self).get_type_display()
