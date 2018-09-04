from django import template

register = template.Library()

@register.filter(is_safe=True)
def checkboxize(value):
    """Converts True/False into disabled checkbox html <input> elems"""
    if value == True:
        return 'TAK'
    else:
        return 'NIE'

@register.filter(is_safe=True)
def addclass(value, arg):
    return value.as_widget(attrs={'class': arg})