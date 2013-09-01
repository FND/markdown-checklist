import markdown

from markdown_checklist import ChecklistExtension


def test_checkbox():
    source = """
Hello World
===========

* [ ] foo
* [x] bar
* [ ] baz

lorem ipsum
    """.strip()

    html = markdown.markdown(source)
    assert html == """
<h1>Hello World</h1>
<ul>
<li>[ ] foo</li>
<li>[x] bar</li>
<li>[ ] baz</li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    html = markdown.markdown(source, extensions=[ChecklistExtension()])
    assert html == """
<h1>Hello World</h1>
<ul>
<li><input type="checkbox" disabled> foo</li>
<li><input type="checkbox" disabled checked> bar</li>
<li><input type="checkbox" disabled> baz</li>
</ul>
<p>lorem ipsum</p>
    """.strip()
