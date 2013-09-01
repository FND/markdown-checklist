"""
Markdown Checklist

a [Python Markdown](http://pythonhosted.org/Markdown/) extension for lists of
tasks with checkboxes

inspired by
[GitHub task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments)
"""

import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


class ChecklistExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.preprocessors.add('checklist', ChecklistPreprocessor(md),
                '<reference')


class ChecklistPreprocessor(Preprocessor):

    pattern = re.compile(r'^([*-]) \[([ Xx])\]')

    def run(self, lines):
        return [self._transform_line(line) for line in lines]

    def _transform_line(self, line):
        return self.pattern.sub(self._replacer, line)

    def _replacer(self, match):
        list_prefix, state = match.groups()
        checked = ' checked' if state != ' ' else ''
        return '%s <input type="checkbox" disabled%s>' % (list_prefix, checked)
