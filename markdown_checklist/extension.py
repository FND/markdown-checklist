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

    def __init__(self, **kwargs):
        self.config = {
            "render_item": [render_item, "custom function to render items"]
        }
        super(ChecklistExtension, self).__init__(**kwargs)

    def extendMarkdown(self, md, md_globals):
        postprocessor = ChecklistPostprocessor(self.getConfig("render_item"), md)
        md.postprocessors.add('checklist', postprocessor, '>raw_html')


class ChecklistPostprocessor(Postprocessor):
    """
    adds checklist class to list element
    """

    pattern = re.compile(r'<li>\[([ Xx])\]')

    def __init__(self, render_item, *args, **kwargs):
        self.render_item = render_item
        super(ChecklistPostprocessor, self).__init__(*args, **kwargs)

    def run(self, html):
        html = re.sub(self.pattern, self._convert_checkbox, html)
        before = '<ul>\n<li><input type="checkbox"'
        after = before.replace('<ul>', '<ul class="checklist">')
        return html.replace(before, after)

    def _convert_checkbox(self, match):
        state = match.group(1)
        return self.render_item(state != ' ')


def render_item(checked):
    checked = ' checked' if checked else ''
    return '<li><input type="checkbox" disabled%s>' % checked
