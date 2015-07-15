from markdown import markdown

from markdown_checklists.extension import ChecklistExtension


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
<li class="task-list-item"><input type="checkbox"><label> foo</label></li>
<li class="task-list-item"><input type="checkbox" checked><label> bar</label></li>
<li class="task-list-item"><input type="checkbox"><label> baz</label></li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    html = markdown(source, extensions=[ChecklistExtension()])
    assert html == expected

    html = markdown(source, extensions=['markdown_checklists.extension'])
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
<li class="task-list-item"><input type="checkbox" checked><label> foo</label></li>
<li class="task-list-item"><input type="checkbox"><label> bar</label></li>
<li class="task-list-item"><input type="checkbox" checked><label> baz</label></li>
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
<li class="task-list-item"><input type="checkbox" checked><label> foo</label></li>
<li class="task-list-item"><input type="checkbox"><label> bar</label></li>
<li class="task-list-item"><input type="checkbox" checked><label> baz</label></li>
</ul>
<hr />
<ul class="checklist">
<li class="task-list-item"><input type="checkbox"><label> lorem</label></li>
<li class="task-list-item"><input type="checkbox" checked><label> ipsum</label></li>
<li class="task-list-item"><input type="checkbox"><label> ...</label></li>
</ul>
    """.strip()
