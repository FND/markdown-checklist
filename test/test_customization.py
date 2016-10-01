from markdown import markdown

from markdown_checklist.extension import ChecklistExtension


def render_item(checked):
    checked = ' xecked' if checked else ''
    return '<li><input type="checkbox" disabled%s>' % checked


def test_checklists():
    source = """
* [ ] foo
* [x] bar
* [ ] baz
    """.strip()

    expected = """
<ul class="checklist">
<li><input type="checkbox" disabled> foo</li>
<li><input type="checkbox" disabled xecked> bar</li>
<li><input type="checkbox" disabled> baz</li>
</ul>
    """.strip()

    html = markdown(source,
            extensions=[ChecklistExtension(render_item=render_item)])
    assert html == expected
