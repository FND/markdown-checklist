"""
[Markdown Checklists](https://github.com/tobiashochguertel/markdown-checklists)

a [Python Markdown](http://pythonhosted.org/Markdown/) extension for lists of
tasks with checkboxes inspured by [GitHub task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments).

Markdown-Checklists is forked from [Markdown Checklist](https://github.com/FND/markdown-checklist) and extended with addtional features.

## Features

* a dash can be used instead of an asterisk for list items
* both upper- and lowercase "x" are accepted to activate checkboxes

## Additional Features

* MakeFile provides task to create for Sublime-Text 3 Plugin [OmniMarkupPreviewer](https://github.com/timonwong/OmniMarkupPreviewer) an Markdown-Renderer extension with additonal template files.
* `class` attribute for `<ul>`-Tag for Checklists.
* `class` attribute for `<li>`-Tag of Checklists.
* Genearting key (hash) for each checkpoint text, using hash to make checklist check"ed" able.
* `id` attribute for `<input>`-Tag of Checklists.
* `for` attribute for `<label>`-Tag of Checklists.

## Example HTML Output

```
h1>Hello World</h1>
<ul class="checklist">
<li class="task-list-item"><input type="checkbox" id="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"><label for="ca052d1d7e0a2f787f4ef9937840dcf91e647b08b208df4bbce2e78d527a4f8c"> foo</label></li>
<li class="task-list-item"><input type="checkbox" id="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311" checked><label for="375719a43941c6a5e7f957c74b6f1d7e20cfefd0040181aaf6d3074c8eaac311"> bar</label></li>
<li class="task-list-item"><input type="checkbox" id="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"><label for="7d80d75283fdbf2a3d8a0e2eed45e9d844d1a7482372cd8bc59581725373c179"> baz</label></li>
<li class="task-list-item"><input type="checkbox"></li>
<li class="task-list-item"><input type="checkbox" checked></li>
</ul>
<p>lorem ipsum</p>
```

## Installation

    $ pip install markdown-checklists

### Markdown-Renderer Extension for OmniMarkupPreviewer

*installs the extension to the current user.*

    $ make OmniMarkupPreviewerInstall

## Usage

    import markdown
    html = markdown.markdown(source, extensions=['markdown_checklists.extension'])

or

    import markdown
    from markdown_checklists.extension import ChecklistsExtension
    html = markdown.markdown(source, extensions=[ChecklistsExtension()])

There is also a small JavaScript/jQuery library to make checkboxes interactive:

    new Checklists("article", function(checkbox, callback) {
        var uri = checkbox.closest("article").find("h1 a").attr("href");
        jQuery.get(uri, callback);
    }, function(markdown, checkbox, callback) {
        var uri = checkbox.closest("article").find("h1 a").attr("href");
        jQuery.ajax({
            type: "put",
            uri: uri,
            data: markdown,
            success: callback
        });
    });

See included `checklists.js` for details.
"""

__version__ = '0.6.3'
__author__ = 'Tobias Hochguertel, FND'
__license__ = 'MIT'
