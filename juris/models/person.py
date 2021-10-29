from django.db.models import CharField, EmailField, Model, TextChoices
from django.urls import reverse


class Person(Model):
    class Type(TextChoices):
        LEGAL = "LE", "Legal"
        NATURAL = "NA", "Natural"

    name = CharField("nombre", max_length=50)
    last_name = CharField("apellido", max_length=50)
    email = EmailField()
    identity_number = CharField("cédula de identidad", primary_key=True, max_length=15)
    type = CharField(
        "tipo de persona", max_length=2, choices=Type.choices, default=Type.NATURAL
    )

    def get_absolute_url(self):
        return reverse("person_detail", kwargs={"pk": self.pk})

    class Meta:
        verbose_name = "persona"
        verbose_name_plural = "personas"

    def get_full_name(self):
        return f"{self.name} {self.last_name}"
