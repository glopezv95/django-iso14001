from django import template

register = template.Library()

@register.filter
def cssize(value):
    return value.lower().replace(" ", "-")