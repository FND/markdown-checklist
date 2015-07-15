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
* Class Attribute for `<ul>`-Tag for Checklists.
* Class Attribute for `<li>`-Tag of Checklists.

## Installation

    $ pip install markdown-checklist

### Markdown-Renderer Extension for OmniMarkupPreviewer

*installs the extension to the current user.*

    $ make OmniMarkupPreviewerInstall

## Usage

    import markdown
    html = markdown.markdown(source, extensions=['markdown_checklists.extension'])

or

    import markdown
    from markdown_checklists.extension import ChecklistExtension
    html = markdown.markdown(source, extensions=[ChecklistExtension()])

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

__version__ = '0.5.2'
__author__ = 'Tobias Hochguertel, FND'
__license__ = 'MIT'
