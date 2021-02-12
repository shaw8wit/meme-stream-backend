from django import template
from django.templatetags.static import (
    do_static as _do_static, static as _static,)

register = template.Library()


def static(path):
    return _static(path)


# template tag for staticfiles tag to static tag converter
# to make swagger compatible with current django version

@register.tag('static')
def do_static(parser, token):
    return _do_static(parser, token)
