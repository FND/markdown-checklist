import os

from setuptools import setup, find_packages

from markdown_checklist import (__version__ as VERSION, __author__ as AUTHOR,
        __license__ as LICENSE, __doc__ as DESC)


META = {
    'name': 'markdown-checklist',
    'url': 'https://github.com/FND/markdown-checklist',
    'version': VERSION,
    'description': 'Python Markdown extension for task lists with checkboxes',
    'long_description': DESC.strip(),
    'license': LICENSE,
    'author': AUTHOR,
    'author_email': '',
    'maintainer': AUTHOR,
    'packages': find_packages(exclude=['test']),
    'platforms': 'Posix; MacOS X; Windows',
    'include_package_data': True,
    'zip_safe': False,
    'install_requires': ['markdown'],
    'extras_require': {
        'testing': ['pytest'],
        'coverage': ['figleaf', 'coverage']
    }
}


if __name__ == '__main__':
    setup(**META)
