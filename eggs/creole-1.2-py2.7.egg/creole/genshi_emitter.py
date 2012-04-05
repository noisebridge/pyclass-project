#!/usr/bin/env python
# -*- coding: utf-8 -*-

ur"""
Test cases contributed by Jan Klopper (janklopper@underdark.nl),
modified by Radomir Dopieralski (MoinMoin:RadomirDopieralski).

>>> import lxml.html.usedoctest
>>> import creole
>>> def parse(text):
...     text = GenshiEmitter(creole.Parser(text).parse()).emit().render()
...     print unicode(text, 'utf-8')
>>> def wiki_parse(text):
...     rules = creole.Rules(wiki_words=True)
...     print GenshiEmitter(creole.Parser(text, rules).parse()).emit().render()

>>> parse(u'test')
<p>test</p>

>>> parse(u'test\ntest')
<p>test test</p>

>>> parse(u'test\n\ntest')
<p>test</p><p>test</p>

>>> parse(u'test\\\\test')
<p>test<br>test</p>

>>> parse(u'ÓÔÕÖØÙÚÛÜÝßàáâãäåæçèéêëìíîïñòóôõöøùúûüýÿŒœ%0A')
<p>ÓÔÕÖØÙÚÛÜÝßàáâãäåæçèéêëìíîïñòóôõöøùúûüýÿŒœ%0A</p>

>>> parse(u'----')
<hr>

>>> parse(u'==test==')
<h2>test</h2>

>>> parse(u'== test')
<h2>test</h2>

>>> parse(u'==test====')
<h2>test</h2>

>>> parse(u'=====test')
<h5>test</h5>

>>> parse(u'==test==\ntest\n===test===')
<h2>test</h2>
<p>test</p>
<h3>test</h3>

>>> parse(u'test\n* test line one\n * test line two\ntest\n\ntest')
<p>test</p>
<ul>
    <li>test line one</li>
    <li>test line two test</li>
</ul>
<p>test</p>

>>> parse(u'* test line one\n* test line two\n** Nested item')
<ul>
    <li>test line one</li>
    <li>test line two<ul>
        <li>Nested item</li>
    </ul></li>
</ul>

>>> parse(u'* test line one\n* test line two\n# Nested item')
<ul>
    <li>test line one</li>
    <li>test line two<ol>
        <li>Nested item</li>
    </ol></li>
</ul>

>>> parse(u'test //test test// test **test test** test')
<p>test <i>test test</i> test <b>test test</b> test</p>

>>> parse(u'test //test **test// test** test')
<p>test <i>test <b>test<i> test<b> test</b></i></b></i></p>

>>> parse(u'**test')
<p><b>test</b></p>

>>> parse(u'|x|y|z|\n|a|b|c|\n|d|e|f|\ntest')
<table>
    <tr><td>x</td><td>y</td><td>z</td></tr>
    <tr><td>a</td><td>b</td><td>c</td></tr>
    <tr><td>d</td><td>e</td><td>f</td></tr>
</table>
<p>test</p>

>>> parse(u'|=x|y|=z=|\n|a|b|c|\n|d|e|f|')
<table>
    <tr><th>x</th><td>y</td><th>z</th></tr>
    <tr><td>a</td><td>b</td><td>c</td></tr>
    <tr><td>d</td><td>e</td><td>f</td></tr>
</table>

>>> parse(u'test http://example.com/test test')
<p>test <a href="http://example.com/test" class="external">http://example.com/test</a> test</p>

>>> parse(u'http://example.com/,test, test')
<p><a href="http://example.com/,test" class="external">http://example.com/,test</a>, test</p>

>>> parse(u'(http://example.com/test)')
<p>(<a href="http://example.com/test" class="external">http://example.com/test</a>)</p>

XXX This might be considered a bug, but it's impossible to detect in general.
>>> parse(u'http://example.com/(test)')
<p><a href="http://example.com/(test" class="external">http://example.com/(test</a>)</p>

>>> parse(u'http://example.com/test?test&test=1')
<p><a href="http://example.com/test?test&amp;test=1" class="external">http://example.com/test?test&amp;test=1</a></p>

>>> parse(u'~http://example.com/test')
<p>http://example.com/test</p>

>>> parse(u'http://example.com/~test')
<p><a href="http://example.com/~test" class="external">http://example.com/~test</a></p>

>>> parse(u'[[test]] [[tset|test]]')
<p><a href="test" class="internal">test</a> <a href="tset" class="internal">test</a></p>

>>> parse(u'[[http://example.com|test]]')
<p><a href="http://example.com" class="external">test</a></p>

>>> wiki_parse(u'Lorem WikiWord iPsum sit ameT.')
<p>Lorem <a href="WikiWord" class="internal">WikiWord</a> iPsum sit ameT.</p>

"""


import re

from creole.parser import Parser
from creole.rules import LinkRules

from genshi import Stream, QName, Attrs

START, END, TEXT = Stream.START, Stream.END, Stream.TEXT

POS = (None, None, None)

class GenshiEmitter(object):
    """
    Generate Genshi stream output for the document
    tree consisting of DocNodes.
    """

    def __init__(self, root, link_rules=None):
        self.root = root
        self.link_rules = link_rules or LinkRules()

    def get_text(self, node):
        """Try to emit whatever text is in the node."""

        try:
            return node.children[0].content or ''
        except:
            return node.content or ''

    def wrap(self, tag, node):
        yield START, (QName(tag), Attrs()), POS
        for part in self.emit_children(node):
            yield part
        yield END, QName(tag), POS

    # *_emit methods for emitting nodes of the document:

    def document_emit(self, node):
        return self.emit_children(node)

    def text_emit(self, node):
        yield TEXT, node.content, POS

    def separator_emit(self, node):
        yield START, (QName('hr'), Attrs()), POS
        yield END, QName('hr'), POS

    def paragraph_emit(self, node):
        return self.wrap('p', node)

    def bullet_list_emit(self, node):
        return self.wrap('ul', node)

    def number_list_emit(self, node):
        return self.wrap('ol', node)

    def list_item_emit(self, node):
        return self.wrap('li', node)

    def table_emit(self, node):
        return self.wrap('table', node)

    def table_row_emit(self, node):
        return self.wrap('tr', node)

    def table_cell_emit(self, node):
        return self.wrap('td', node)

    def table_head_emit(self, node):
        return self.wrap('th', node)

    def emphasis_emit(self, node):
        return self.wrap('i', node)

    def strong_emit(self, node):
        return self.wrap('b', node)

    def header_emit(self, node):
        yield START, (QName('h%d' % node.level), Attrs()), POS
        yield TEXT, node.content, POS
        yield END, QName('h%d' % node.level), POS

    def code_emit(self, node):
        return self.wrap('tt', node)

    def link_emit(self, node):
        target = node.content
        class_ = "internal"
        m = self.link_rules.addr_re.match(target)
        if m:
            if m.group('extern_addr'):
                class_ = "external"
            elif m.group('inter_wiki'):
                raise NotImplementedError
        yield START, (QName('a'),
                      Attrs([
                            (QName('href'), target),
                            (QName('class'), class_),
                            ])), POS
        if node.children:
            for part in self.emit_children(node):
                yield part
        else:
            yield TEXT, target, POS
        yield END, QName('a'), POS

    def image_emit(self, node):
        target = node.content
        text = self.get_text(node)
        class_ = "internal"
        m = self.link_rules.addr_re.match(target)
        if m:
            if m.group('extern_addr'):
                class_ = "external"
            elif m.group('inter_wiki'):
                raise NotImplementedError
        yield START, (QName('img'),
                      Attrs([
                        (QName('src'), target),
                        (QName('alt'), text),
                        (QName('class'), class_),
                      ])), POS
        yield END, QName('img'), POS

    def macro_emit(self, node):
        raise NotImplementedError

    def break_emit(self, node):
        yield START, (QName('br'), Attrs()), POS
        yield END, QName('br'), POS

    def preformatted_emit(self, node):
        yield START, (QName('pre'), Attrs()), POS
        yield TEXT, node.content, POS
        yield END, QName('pre'), POS

    def default_emit(self, node):
        """Fallback function for emitting unknown nodes."""

        raise TypeError('Unknown node type')

    def emit_children(self, node):
        """Emit all the children of a node."""

        for child in node.children:
            for part in self.emit_node(child):
                yield part

    def emit_node(self, node):
        """Emit a single node."""

        emit = getattr(self, '%s_emit' % node.kind, self.default_emit)
        return emit(node)

    def emit(self):
        """Emit the document represented by self.root DOM tree."""

        return Stream(self.emit_node(self.root))


