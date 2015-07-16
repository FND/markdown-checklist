from markdown import markdown

from markdown_checklists.extension import ChecklistsExtension


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
<li class="task-list-item"><input type="checkbox" id="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"><label for="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"> foo</label></li>
<li class="task-list-item"><input type="checkbox" id="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311" checked><label for="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"> bar</label></li>
<li class="task-list-item"><input type="checkbox" id="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"><label for="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"> baz</label></li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    html = markdown(source, extensions=[ChecklistsExtension()])
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

    html = markdown(source, extensions=[ChecklistsExtension()])
    assert html == """
<h1>Hello World</h1>
<ul class="checklist">
<li class="task-list-item"><input type="checkbox" id="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c" checked><label for="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"> foo</label></li>
<li class="task-list-item"><input type="checkbox" id="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"><label for="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"> bar</label></li>
<li class="task-list-item"><input type="checkbox" id="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179" checked><label for="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"> baz</label></li>
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

    html = markdown(source, extensions=[ChecklistsExtension()])
    assert html == """
<ul class="checklist">
<li class="task-list-item"><input type="checkbox" id="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c" checked><label for="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"> foo</label></li>
<li class="task-list-item"><input type="checkbox" id="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"><label for="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"> bar</label></li>
<li class="task-list-item"><input type="checkbox" id="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179" checked><label for="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"> baz</label></li>
</ul>
<hr />
<ul class="checklist">
<li class="task-list-item"><input type="checkbox" id="d99f0729bf97ea577a31c7405e3cdd06cd348d2cc5abd49468dd491d5ff80c7c"><label for="d99f0729bf97ea577a31c7405e3cdd06cd348d2cc5abd49468dd491d5ff80c7c"> lorem</label></li>
<li class="task-list-item"><input type="checkbox" id="c1faa4ff4d958383a5f295634f03a5f1d1dadda2f133b1116c1faf6c4b6c555a" checked><label for="c1faa4ff4d958383a5f295634f03a5f1d1dadda2f133b1116c1faf6c4b6c555a"> ipsum</label></li>
<li class="task-list-item"><input type="checkbox" id="4501c820f066129ae4d33ca959607e85c8b9aeb7de7e329197c9e307ef05a023"><label for="4501c820f066129ae4d33ca959607e85c8b9aeb7de7e329197c9e307ef05a023"> ...</label></li>
</ul>
    """.strip()
