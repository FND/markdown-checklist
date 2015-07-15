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
<li class="task-list-item"><input type="checkbox"> foo</li>
<li class="task-list-item"><input type="checkbox" checked> bar</li>
<li class="task-list-item"><input type="checkbox"> baz</li>
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
<li class="task-list-item"><input type="checkbox" checked> foo</li>
<li class="task-list-item"><input type="checkbox"> bar</li>
<li class="task-list-item"><input type="checkbox" checked> baz</li>
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
<li class="task-list-item"><input type="checkbox" checked> foo</li>
<li class="task-list-item"><input type="checkbox"> bar</li>
<li class="task-list-item"><input type="checkbox" checked> baz</li>
</ul>
<hr />
<ul class="checklist">
<li class="task-list-item"><input type="checkbox"> lorem</li>
<li class="task-list-item"><input type="checkbox" checked> ipsum</li>
<li class="task-list-item"><input type="checkbox"> ...</li>
</ul>
    """.strip()
