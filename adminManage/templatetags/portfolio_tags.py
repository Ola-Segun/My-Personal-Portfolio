from django import template
from ..models import Adminmessage

register = template.Library()

@register.simple_tag
def new_message():
    return Adminmessage.objects.filter(is_read=False).count()