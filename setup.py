import os

from setuptools import setup, find_packages
import sys
_PY3 = sys.version_info[0] > 2

def getmetainfo(filepath):
    """
    Get metadata from a file, but without importing it. This
    trick needed because importing can set off ImportError,
    in that setup.py runs by definition before the modules it
    sets up (or their dependencies) are available.
    """
    if _PY3:
        exec(open(filepath).read())
        return vars()
    else:
        execfile(filepath)
        return locals()

metainfo = getmetainfo('./mdx_checklist/meta.py')

META = {
    'name': 'mdx_checklist',
    'url': 'https://github.com/FND/markdown-checklist',
    'version': metainfo['VERSION'],
    'description': 'Python Markdown extension for task lists with checkboxes',
    'long_description': metainfo['DESC'].strip(),
    'license': metainfo['LICENSE'],
    'author': metainfo['AUTHOR'],
    'keywords': 'markdown checklist extension',
    'classifiers': [
        'Development Status :: 4 - Beta',
        'Operating System :: OS Independent',
        'License :: OSI Approved :: BSD License',
        'Intended Audience :: Developers',
        'Environment :: Web Environment',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: Implementation :: CPython',
        'Programming Language :: Python :: Implementation :: PyPy',
        'Topic :: Text Processing :: Filters',
        'Topic :: Text Processing :: Markup',
        'Topic :: Text Processing :: Markup :: HTML'
    ],
    'author_email': '',
    'maintainer': metainfo['AUTHOR'],
    'packages': find_packages(exclude=['test']),
    'platforms': 'Posix; MacOS X; Windows',
    'include_package_data': True,
    'zip_safe': False,
    'install_requires': ['Markdown>=2.3.1'],
    'tests_require': ['tox', 'pytest'],
    'extras_require': {
        'testing': ['pytest'],
        'coverage': ['figleaf', 'coverage']
    }
}


if __name__ == '__main__':
    setup(**META)
