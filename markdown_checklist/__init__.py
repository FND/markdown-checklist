"""
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


Usage
-----

    import markdown
    html = markdown.markdown(source, extensions=['markdown_checklist.extension'])

or

    import markdown
    from markdown_checklist.extension import ChecklistExtension
    html = markdown.markdown(source, extensions=[ChecklistExtension()])
"""

__version__ = '0.1.0'
__author__ = 'FND'
__license__ = 'MIT'
