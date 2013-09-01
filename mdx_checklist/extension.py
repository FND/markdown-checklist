import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor


def makeExtension(configs=None):
    return ChecklistExtension(configs=configs)


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
