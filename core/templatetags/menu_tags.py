from django import template
from django.template.loader import render_to_string

from core.models import Menu

register = template.Library()

@register.simple_tag
def draw_menu(type):
    template = '{template_name}.html'.format(template_name=type)
    menu_items = Menu.objects.filter(parent=None).prefetch_related('children')
    context = {'menu_items': menu_items, }
    return render_to_string(template, context)


