from markdown import markdown

from markdown_checklist.extension import ChecklistExtension


def render_item(caption, checked):
    checked = ' checked' if checked else ''
    template = '<li><label><input type="checkbox" disabled%s>%s</label></li>'
    return template % (checked, caption)


def test_checklists():
    source = """
* [ ] foo
* [x] bar
* [ ] baz
    """.strip()

    expected = """
<ul class="checklist">
<li><label><input type="checkbox" disabled> foo</label></li>
<li><label><input type="checkbox" disabled checked> bar</label></li>
<li><label><input type="checkbox" disabled> baz</label></li>
</ul>
    """.strip()

    html = markdown(source,
            extensions=[ChecklistExtension(render_item=render_item)])
    assert html == expected
