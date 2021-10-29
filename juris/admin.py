from django.contrib.admin import ModelAdmin, TabularInline, register

from juris.models import LegalRecord, Part, Person, Proceeding


class ProceedingInline(TabularInline):
    model = Proceeding


class PartInline(TabularInline):
    model = Part


class PersonInline(TabularInline):
    model = Person


@register(LegalRecord)
class LegalRecordAdmin(ModelAdmin):
    inlines = (ProceedingInline, PartInline)


@register(Part)
class PartAdmin(ModelAdmin):
    pass

@register(Proceeding)
class ProceedingAdmin(ModelAdmin):
    pass


@register(Person)
class PersonAdmin(ModelAdmin):
    inlines = (PartInline,)
    pass
