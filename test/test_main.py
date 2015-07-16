# -*- coding: utf-8 -*-
from markdown import markdown

from markdown_checklists.extension import ChecklistsExtension


def test_checklists():
    source = r"""
Hello World
===========

* [ ] foo
* [x] bar
* [ ] baz
* [ ]
* [x]
* [ ] Der Unit-Test `contextMenuReplacesText` wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?) Datei: `X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java`

lorem ipsum
    """.strip()

    print("\n")
    print(source)
    print("\n")

    print("\n")
    print(type(source))
    print(repr(source))
    print("\n")


    html = markdown(source)
    assert html == r"""
<h1>Hello World</h1>
<ul>
<li>[ ] foo</li>
<li>[x] bar</li>
<li>[ ] baz</li>
<li>[ ]</li>
<li>[x]</li>
<li>[ ] Der Unit-Test <code>contextMenuReplacesText</code> wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?) Datei: <code>X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java</code></li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    expected = r"""
<h1>Hello World</h1>
<ul class="checklist">
<li class="task-list-item"><input type="checkbox" id="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"><label for="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"> foo</label></li>
<li class="task-list-item"><input type="checkbox" id="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311" checked><label for="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"> bar</label></li>
<li class="task-list-item"><input type="checkbox" id="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"><label for="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"> baz</label></li>
<li class="task-list-item"><input type="checkbox"></li>
<li class="task-list-item"><input type="checkbox" checked></li>
<li class="task-list-item"><input type="checkbox" id="11d23cf018de6e2936e7f4376b246b436b3334aaa492d13f7aa6270216dee55e"><label for="11d23cf018de6e2936e7f4376b246b436b3334aaa492d13f7aa6270216dee55e"> Der Unit-Test <code>contextMenuReplacesText</code> wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?) Datei: <code>X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java</code></label></li>
</ul>
<p>lorem ipsum</p>
    """.strip()

    html = markdown(source, extensions=[ChecklistsExtension()])
    assert html == expected

    html = markdown(source, extensions=['markdown_checklists.extension'])
    assert html == expected


def test_syntax_variations():
    source = r"""
Hello World
===========

- [x] foo
- [ ] bar
- [X] baz

lorem ipsum
    """.strip()

    html = markdown(source, extensions=[ChecklistsExtension()])
    assert html == r"""
<h1>Hello World</h1>
<ul class="checklist">
<li class="task-list-item"><input type="checkbox" id="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c" checked><label for="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"> foo</label></li>
<li class="task-list-item"><input type="checkbox" id="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"><label for="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"> bar</label></li>
<li class="task-list-item"><input type="checkbox" id="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179" checked><label for="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"> baz</label></li>
</ul>
<p>lorem ipsum</p>
    """.strip()


def test_class():
    source = r"""
* [x] foo
* [ ] bar
* [X] baz

----

* [ ] lorem
* [x] ipsum
* [ ] ...
    """.strip()

    html = markdown(source, extensions=[ChecklistsExtension()])
    assert html == r"""
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


def test_realworld_example():
    source = r"""
**09.07.2015 - Getting Startet:**

 - [] Der Unit-Test `contextMenuReplacesText` wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?) Datei: `X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java`
 - [X] Parent Pom wird nicht gefunden beim starten der pdfsam-community variante. (`mvn exec:java`). Weiterer Schritt nötig um Parent Pom lokal zu installieren: `cd pdfsam-parent && mvn install`, bevor pdfsam-community gestartet werden kann.
 - [ ] Neuer vollständiger Befehl um das Projekt zu bauen, im lokalen maven repository zu installieren und pdf-sam community zu starten: `mvn clean install -Dmaven.test.skip=true && cd pdfsam-parent/ && mvn install && cd .. && cd pdfsam-community && mvn exec:java`

    """.strip()

    html = markdown(source)
    assert html == r"""
<p><strong>09.07.2015 - Getting Startet:</strong></p>
<ul>
<li>[] Der Unit-Test <code>contextMenuReplacesText</code> wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?) Datei: <code>X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java</code></li>
<li>[X] Parent Pom wird nicht gefunden beim starten der pdfsam-community variante. (<code>mvn exec:java</code>). Weiterer Schritt nötig um Parent Pom lokal zu installieren: <code>cd pdfsam-parent &amp;&amp; mvn install</code>, bevor pdfsam-community gestartet werden kann.</li>
<li>[ ] Neuer vollständiger Befehl um das Projekt zu bauen, im lokalen maven repository zu installieren und pdf-sam community zu starten: <code>mvn clean install -Dmaven.test.skip=true &amp;&amp; cd pdfsam-parent/ &amp;&amp; mvn install &amp;&amp; cd .. &amp;&amp; cd pdfsam-community &amp;&amp; mvn exec:java</code></li>
</ul>
    """.strip()


    html = markdown(source, extensions=[ChecklistsExtension()])
    assert html == r"""
<p><strong>09.07.2015 - Getting Startet:</strong></p>
<ul>
<li>[] Der Unit-Test <code>contextMenuReplacesText</code> wurde auskommentiert um die ausführung zu verhindern. Dieser Test funktioniert in meiner Umgebung nicht wie erwachtet. (Tastatur Layout?, Aktivierte Sprache des Betriebsystems?) Datei: <code>X:\pdfsam\pdfsam-fx\src\test\java\org\pdfsam\ui\prefix\PrefixFieldTest.java</code></li>
<li class="task-list-item"><input type="checkbox" id="26703b3e4519a2ab24f5e1436367e6ecdcff46964278f6456ec5530dda4ee772" checked><label for="26703b3e4519a2ab24f5e1436367e6ecdcff46964278f6456ec5530dda4ee772"> Parent Pom wird nicht gefunden beim starten der pdfsam-community variante. (<code>mvn exec:java</code>). Weiterer Schritt nötig um Parent Pom lokal zu installieren: <code>cd pdfsam-parent &amp;&amp; mvn install</code>, bevor pdfsam-community gestartet werden kann.</label></li>
<li class="task-list-item"><input type="checkbox" id="2e265eca17bd1470a09518ebe6fa9605a08101e1a90a44a13456fc7717bd49f1"><label for="2e265eca17bd1470a09518ebe6fa9605a08101e1a90a44a13456fc7717bd49f1"> Neuer vollständiger Befehl um das Projekt zu bauen, im lokalen maven repository zu installieren und pdf-sam community zu starten: <code>mvn clean install -Dmaven.test.skip=true &amp;&amp; cd pdfsam-parent/ &amp;&amp; mvn install &amp;&amp; cd .. &amp;&amp; cd pdfsam-community &amp;&amp; mvn exec:java</code></label></li>
</ul>
    """.strip()
