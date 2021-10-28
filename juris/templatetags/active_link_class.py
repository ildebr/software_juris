from django.template import Library
from django.template.context import RequestContext, Context
from django.urls import reverse

register = Library()


@register.simple_tag(takes_context=True)
def active_link_class(context: Context,
                      *args,
                      active_class: str,
                      inactive_class: str = '',
                      **kwargs):
    path: str = context["request"].path
    if path.startswith(reverse(*args, **kwargs)):
        return active_class
    return inactive_class
