#!/usr/bin/python
# -*- coding: utf-8 -*-

import creole

class HtmlEmitter(creole.HtmlEmitter):
    """
    This class changes how we actually emit the HTML for some
    of the nodes. You should also override the link generation
    and macro support code here.
    """

    def header_emit(self, node):
        """Instead of using node.content, we emit the children."""

        return u'<h%d>%s</h%d>\n' % (node.level, self.emit_children(node),
                                     node.level)


class Rules(creole.Rules):
    """
    This class would be used to add or change any regular expressions.
    We don't need it in this particular case though, so we just leave
    it like the original class.
    """

class Parser(creole.Parser):
    r"""
    This class is for overriding the behavior of our parser. We change the
    rule that handles headings, so that instead of just putting the text
    inside the heading, it parses it, looking for any markup.

    Here are some simple tests:

    >>> import lxml.html.usedoctest
    >>> def parse(text):
    ...     print HtmlEmitter(Parser(text).parse()).emit()

    >>> parse(u'====test====')
    <h4>test</h4>

    >>> parse(u'===[[test]]===')
    <h3><a href="test">test</a></h3>

    >>> parse(u'==test //italic// **bold** test==')
    <h2>test <i>italic</i> <b>bold</b> test</h2>

    >>> parse(u'==test==\ntest')
    <h2>test</h2>
    <p>test</p>
    """

    def _head_repl(self, groups):
        # Note: this code can be shorter, I wrote it like this
        # so that I can comment on every step.
        #
        # The shorter version would look like this:
        #
        # self.cur = creole.DocNode('header', self.cur)
        # self.cur.level = len(groups.get('head_head', ' '))
        # self.parse_inline(groups.get('head_text', '').strip())
        # self.cur = self._upto(self.cur, ('document', 'section', 'blockquote'))
        # self.text = None

        # Make sure we are not inside a paragraph, list, other heading, etc.
        self.cur = self._upto(self.cur, ('document', 'section', 'blockquote'))
        # Remember where we are.
        parent = self.cur
        # Create the heading node.
        node = creole.DocNode('header', self.cur)
        # Set its level.
        node.level = len(groups.get('head_head', ' '))
        # Make it the curret node.
        self.cur = node
        # Parse the text inside the heading.
        text = groups.get('head_text', '').strip()
        self.parse_inline(text)
        # Go back to where we started.
        self.cur = parent
        self.text = None

if __name__=="__main__":
#    import sys
#    raw = unicode(sys.stdin.read(), 'utf-8', 'ignore')
#    rules = Rules()
#    document = Parser(raw, rules).parse()
#    html = HtmlEmitter(document).emit()
#    sys.stdout.write(html.encode('utf-8', 'ignore'))

# Instead of the above code to convert text from command line, we run tests:

    import doctest
    doctest.testmod()

