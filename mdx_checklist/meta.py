DESC = """
[Markdown Checklist](https://github.com/FND/markdown-checklist)

a [Python Markdown](http://pythonhosted.org/Markdown/) extension for lists of
tasks with checkboxes

inspired by
[GitHub task lists](https://github.com/blog/1375-task-lists-in-gfm-issues-pulls-comments):

    * [ ] foo
    * [x] bar
    * [ ] baz

becomes

    <ul>
    <li><input type="checkbox" disabled> foo</li>
    <li><input type="checkbox" disabled checked> bar</li>
    <li><input type="checkbox" disabled> baz</li>
    </ul>

* a dash can be used instead of an asterisk for list items
* both upper- and lowercase "x" are accepted to activate checkboxes


Installation
------------

    $ pip install markdown-checklist


Usage
-----

    import markdown
    html = markdown.markdown(source, extensions=['checklist'])

or

    import markdown
    from mdx_checklist.extension import ChecklistExtension
    html = markdown.markdown(source, extensions=[ChecklistExtension()])
"""

VERSION = '0.1.0'
AUTHOR = 'FND'
LICENSE = 'MIT'
