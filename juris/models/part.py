from django.db.models import CASCADE, CharField, ForeignKey, Model, TextChoices


class Part(Model):
    class Type(TextChoices):
        DEFENDANT = "DEF", "Acusado"
        PLAINTIFF = "PLA", "Demandante"

    legal_record = ForeignKey("LegalRecord", on_delete=CASCADE)
    person = ForeignKey("Person", on_delete=CASCADE)
    type = CharField("Tipo", max_length=3, choices=Type.choices)

    class Meta:
        unique_together = ("person", "type", "legal_record")
        verbose_name = "Parte"
        verbose_name_plural = "Partes"
