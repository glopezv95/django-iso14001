from django import template

register = template.Library()

@register.simple_tag()
def verbose(instance, field):
    return instance._meta.get_field(str(field)).verbose_name