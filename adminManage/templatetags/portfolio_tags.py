from django import template
from ..models import message

register = template.Library()

@register.simple_tag
def new_message():
    return message.objects.filter(is_read=False).count()