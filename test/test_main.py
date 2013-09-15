from markdown import markdown

from markdown_checklist.extension import ChecklistExtension


def test_checklists():
    source = """
Hello World
===========

* [ ] foo
* [x] bar
* [ ] baz

lorem ipsum
    """.strip()

    html = markdown(source)
    assert html == """
<h1>Hello World</h1>
<ul>
<li>[ ] foo</li>
<li>[x] bar</li>
<li>[ ] baz</li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    expected = """
<h1>Hello World</h1>
<ul class="checklist">
<li><input type="checkbox" disabled> foo</li>
<li><input type="checkbox" disabled checked> bar</li>
<li><input type="checkbox" disabled> baz</li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == expected

    html = markdown(source, extensions=['markdown_checklist.extension'])
    assert html == expected


def test_syntax_variations():
    source = """
Hello World
===========

- [x] foo
- [ ] bar
- [X] baz

lorem ipsum
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == """
<h1>Hello World</h1>
<ul class="checklist">
<li><input type="checkbox" disabled checked> foo</li>
<li><input type="checkbox" disabled> bar</li>
<li><input type="checkbox" disabled checked> baz</li>
</ul>
<p>lorem ipsum</p>
    """.strip()


def test_class():
    source = """
* [x] foo
* [ ] bar
* [X] baz

----

* [ ] lorem
* [x] ipsum
* [ ] ...
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == """
<ul class="checklist">
<li><input type="checkbox" disabled checked> foo</li>
<li><input type="checkbox" disabled> bar</li>
<li><input type="checkbox" disabled checked> baz</li>
</ul>
<hr />
<ul class="checklist">
<li><input type="checkbox" disabled> lorem</li>
<li><input type="checkbox" disabled checked> ipsum</li>
<li><input type="checkbox" disabled> ...</li>
</ul>
    """.strip()
