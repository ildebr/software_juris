from django.db.models import CharField, DateField, Model, ForeignKey
from django.db.models.deletion import PROTECT


class Proceeding(Model):
    summary = CharField("resumen", max_length=100)
    date = DateField("fecha de ingreso")
    type = CharField("tipo", max_length=100)
    legal_record = ForeignKey("LegalRecord", on_delete=PROTECT)

    class Meta:
        verbose_name = "actuación judicial"
        verbose_name_plural = "actuaciones judiciales"
