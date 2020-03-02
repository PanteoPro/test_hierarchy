from django import template
from ..models import Theme

register = template.Library()


@register.filter(name="lowe")
def lowe(value): # Only one argument.
    """Converts a string into all lowercase"""
    return f'{value.lower()} PIDRrrr'


@register.inclusion_tag('myapp1/promo.html')
def themes():
	return {
		'themeses': Theme.objects.all()
	}

