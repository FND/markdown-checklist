import re

from markdown.extensions import Extension
from markdown.preprocessors import Preprocessor
from markdown.postprocessors import Postprocessor


def makeExtension(configs=None):
    if configs is None:
        return ChecklistExtension()
    else:
        return ChecklistExtension(configs=configs)


class ChecklistExtension(Extension):

    def extendMarkdown(self, md, md_globals):
        md.postprocessors.add('checklist', ChecklistPostprocessor(md),
                '>raw_html')


class ChecklistPostprocessor(Postprocessor):
    """
    adds checklist class to list element
    """

    pattern = re.compile(r'<li>\[([ Xx])\]')
    item_pattern = re.compile(r'(<li.*<input type="checkbox"[ ]?[c]?[h]?[e]?[c]?[k]?[e]?[d]?>)(.*|.*\n*.*)(</li>)')

    def run(self, html):
        html = re.sub(self.pattern, self._convert_checkbox, html)
        before = '<ul>\n<li class="task-list-item"><input type="checkbox"'
        after = before.replace('<ul>', '<ul class="checklist">')
        checked_html = html.replace(before, after)
        checked_labeld_html = re.sub(self.item_pattern, self._convert_label, checked_html)
        return checked_labeld_html

    def _convert_checkbox(self, match):
        state = match.group(1)
        activeState = ''
        checked = ' checked' if state != ' ' else ''
        activeAttr = ' disabled' if activeState != ' ' else ''
        return '<li class="task-list-item"><input type="checkbox"%s>' % checked

    def _convert_label(self, match):
        before_item = match.group(1)
        item = match.group(2)
        after_item = match.group(3)
        return '%s<label>%s</label>%s' % (before_item, item, after_item)

