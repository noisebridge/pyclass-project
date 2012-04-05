import re

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.html import conditional_escape
from django.utils.safestring import mark_safe

from wiki.forms import WIKI_WORD_RE


register = template.Library()

url_re = r'https?://\w+(\.\w+)*(/)?'

wikiword_link = re.compile(r'(?<!!)\b(%s)\b' % WIKI_WORD_RE)
url_pattern = re.compile(r'(?<!!)(%s)' % url_re)

#((is_relative, pattern), ...)
link_patterns = (
    (True, wikiword_link),
    (False, url_pattern),
)


@register.filter
@stringfilter
def wiki_links(text, autoescape=None):
    if autoescape:
        text = conditional_escape(text)
    for is_relative, pattern in link_patterns:
        tag = r'<a href="%s">\1</a>' 
        if is_relative:
            tag = tag % r'../\1/'
        else:
            tag = tag % r'\1'
        text = pattern.sub(tag, text)
    return mark_safe(text)


@register.inclusion_tag('wiki/article_teaser.html')
def show_teaser(article):
    """ Show a teaser box for the summary of the article.
    """
    return {'article': article}


@register.inclusion_tag('wiki/wiki_title.html')
def wiki_title(group):
    """ Display a <h1> title for the wiki, with a link to the group main page.
    """
    if group:
        return {'group': group,
                'group_name': group.name,
                'group_type': group._meta.verbose_name.title(),
                'group_url': group.get_absolute_url()}
    else:
        # no need to put group in context since it is None
        return {}
