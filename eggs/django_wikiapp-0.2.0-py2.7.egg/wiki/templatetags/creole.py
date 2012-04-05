# -*- coding: utf-8 -*-
""" Provides the `creole` template filter, to render
texts using the markup used by the MoinMoin wiki.
"""

from django import template
from django.conf import settings

try:
    from creole import Parser as CreoleParser
    from creole2html import HtmlEmitter
except ImportError:
    CreoleParser = None


register = template.Library()


@register.filter
def creole(text, **kw):
    """Returns the text rendered by the Creole markup.
    """
    if CreoleParser is None and settings.DEBUG:
        raise template.TemplateSyntaxError("Error in creole filter: "
            "The Creole library isn't installed, try easy_install creole.")
    parser = CreoleParser(text)
    emitter = HtmlEmitter(parser.parse())
    return emitter.emit()

class CreoleTextNode(template.Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return creole(self.nodelist.render(context))

@register.tag("creole")
def crl_tag(parser, token):
    """
    Render the Creole into html. Will pre-render template code first.
    """
    nodelist = parser.parse(('endcreole',))
    parser.delete_first_token()
    return CreoleTextNode(nodelist)

