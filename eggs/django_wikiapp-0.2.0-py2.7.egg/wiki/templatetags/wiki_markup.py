# -*- coding: utf-8 -*-
""" Provides util tags to work with markup and other wiki stuff.
"""
from django import template
from django.conf import settings

from template_utils.markup import formatter
# importing here so it is possible to use its filters
# when loading this module.
from template_utils.templatetags.generic_markup import *

try:
    from creole import Parser as CreoleParser
    from creole2html import HtmlEmitter
except ImportError:
    CreoleParser = None

def creole(text, **kw):
    """Returns the text rendered by the Creole markup.
    """
    if CreoleParser is None and settings.DEBUG:
        raise template.TemplateSyntaxError("Error in creole filter: "
            "The Creole library isn't installed, try easy_install creole.")
    parser = CreoleParser(text)
    emitter = HtmlEmitter(parser.parse())
    return emitter.emit()

if CreoleParser is not None:
    formatter.register('creole', creole)

register = template.Library()

@register.inclusion_tag('wiki/article_content.html')
def render_content(article, content_attr='content', markup_attr='markup'):
    """ Display an the body of an article, rendered with the right markup.

    - content_attr is the article attribute that will be rendered.
    - markup_attr is the article atribure with the markup that used
      on the article.

    Use examples on templates:

        {# article have a content and markup attributes #}
        {% render_content article %}

        {# article have a body and markup atributes #}
        {% render_content article 'body' %}

        {# we want to display the  summary instead #}
        {% render_content article 'summary' %}

        {# post have a tease and a markup_style attributes #}
        {% render_content post 'tease' 'markup_style' %}

        {# essay have a content and markup_lang attributes #}
        {% render_content essay 'content' 'markup_lang' %}

    """
    return {
        'content': getattr(article, content_attr),
        'markup': getattr(article, markup_attr)
    }
