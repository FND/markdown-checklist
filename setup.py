import sys
import os

from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand


META = {
    'name': 'markdown-checklists',
    'url': 'https://github.com/tobiashochguertel/markdown-checklists',
    'version': "0.5.1",
    'description': 'Fork of Markdown-checklist: Python Markdown extension for task lists with checkboxes',
    'long_description': "Extended Version of Markdown-checklist.",
    'license': "MIT",
    'author': "Tobias Hochgürtel; FND@innoq",
    'author_email': 'tobias.hochguertel@googlemail.com',
    'maintainer': "tobias.hochguertel@googlemail.com",
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


# entry point for tests (required because `coverage` fails to invoke `py.test`
# in Travis CI's virtualenv)

class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        import pytest
        errno = pytest.main(self.test_args)
        sys.exit(errno)

META['cmdclass'] = { 'test': PyTest }


if __name__ == '__main__':
    setup(**META)
