from django.template import Library
from django.template.defaultfilters import stringfilter

register = Library()

@register.filter
@stringfilter
def split(string, sep):
    """Return the string split by sep.

    Example usage: {{ value|split:"/" }}
    """
    return string.split(sep)
