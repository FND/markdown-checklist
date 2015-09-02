## Tools und deren Optionen
#PYTHON     = /cygdrive/d/Applications/Python/Python34/python.exe
PYTHON     = /usr/bin/python
#PYTEST     = /cygdrive/d/Applications/Python/Python34/Scripts/py.test.exe
PYTEST     = /cygdrive/d/Applications/Python/Python34/Scripts/py.test-2.7.exe
OMNIMARKUPPREVIEWER_INSTALL_PATH_WINDOWS = "$(APPDATA)\Sublime Text 3\Packages\OmniMarkupPreviewer"
OMNIMARKUPPREVIEWER_INSTALL_PATH = `/usr/bin/cygpath.exe -ua $(OMNIMARKUPPREVIEWER_INSTALL_PATH_WINDOWS)`

define exmapleHtmlChecklistBuildScript
from markdown import markdown;
from markdown_checklists.extension import ChecklistsExtension;
html="";
with open("example/testFile.md", "r") as mdfile:
  source = mdfile.read();
tplsource="";
with open("markdown_checklists/checklists.tpl", "r") as tplfile:
  tplsource = tplfile.read();
htmlsource = markdown(source, extensions=[ChecklistsExtension()]);
html = tplsource.replace("{{!html_part}}", htmlsource);
html = html.replace("/public/","public/");
html = html.replace("%if mathjax_enabled:","");
html = html.replace("%end","");
print(html);
endef
export exmapleHtmlChecklistBuildScript

.PHONY: release dist readme test lint coverage clean

OmniMarkupPreviewerRelease: readme clean test
	mkdir target/
	mkdir -p target/public
	mkdir -p target/templates
	mkdir -p target/OmniMarkupLib/Renderers/libs/markdown/extensions

	cp -rf markdown_checklists/extension.py target/OmniMarkupLib/Renderers/libs/markdown/extensions/checklists.py
	cp -rf markdown_checklists/checklists.js target/public/checklists.js
	cp -rf markdown_checklists/checklists.css target/public/checklists.css
	cp -rf markdown_checklists/checklists.tpl target/templates/checklists.tpl
	cp -rf markdown_checklists/checklists-export.tpl target/templates/checklists-export.tpl

OmniMarkupPreviewerInstall: OmniMarkupPreviewerRelease
	cp -rf target/* "$(OMNIMARKUPPREVIEWER_INSTALL_PATH)"

release: readme clean test
	git diff --exit-code # ensure there are no uncommitted changes
	git tag -a \
			-m v`python -c 'import markdown_checklists; print(markdown_checklists.__version__)'` \
			v`python -c 'import markdown_checklists; print(markdown_checklists.__version__)'`
	git push origin master --tags
	# XXX: duplicates dist target
	rm -r dist || true
	$(PYTHON) setup.py sdist upload

dist: clean test
	rm -r dist || true
	$(PYTHON) setup.py sdist

readme: example-html
	$(PYTHON) -c "import markdown_checklists as cl; print(cl.__doc__.strip())" > README
	sed -i "2i[![Build Status](https://travis-ci.org/tobiashochguertel/markdown-checklists.svg?branch=master)](https://travis-ci.org/tobiashochguertel/markdown-checklists)" README
	sed -i "3i<!--[![coverage](https://coveralls.io/repos/FND/markdown-checklist/badge.png)](https://coveralls.io/r/FND/markdown-checklist)-->" README

example-html:
	@echo "$$exmapleHtmlChecklistBuildScript"> build.example-thml.py
	pyminifier --gzip  build.example-thml.py > mini-build.example-thml.py && $(PYTHON) mini-build.example-thml.py | tail -n +5 > example/testFile.html

test: clean
	py.test -s --tb=short test -vv

lint:
	find . -name "*.py" -not -path "./venv/*" | while read filepath; do \
		pep8 --ignore=E128,E261 $$filepath; \
	done
	#upyflakes $$filepath; \
	#pylint --reports=n --include-ids=y $$filepath; \

coverage: clean
	# option #1: figleaf
	find . test -name "*.py" > coverage.lst
	figleaf `which py.test` test
	figleaf2html -f coverage.lst
	# option #2: coverage
	coverage run `which py.test` test
	coverage html
	# reports
	coverage report
	@echo "[INFO] additional reports in \`html/index.html\` (figleaf) and" \
			"\`htmlcov/index.html\` (coverage)"

clean:
	find . -name "*.pyc" -print0 | xargs -0 rm || true
	rm -rf html .figleaf coverage.lst # figleaf
	rm -rf htmlcov .coverage # coverage
	rm -rf test/__pycache__ # pytest
	rm -r markdown_checklists.egg-info || true
	rm -rf target/
	rm -rf dist/
