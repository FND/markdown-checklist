.PHONY: release dist readme test lint coverage clean

release: readme clean test
	git diff --exit-code # ensure there are no uncommitted changes
	git tag -a \
			-m v`python -c 'import markdown_checklist; print(markdown_checklist.__version__)'` \
			v`python -c 'import markdown_checklist; print(markdown_checklist.__version__)'`
	git push origin master --tags
	# XXX: duplicates dist target
	rm -r dist || true
	python setup.py sdist upload

dist: clean test
	rm -r dist || true
	python setup.py sdist

readme:
	python -c "import markdown_checklist as cl; print(cl.__doc__.strip())" > README
	sed -i "2i[![build status](https://secure.travis-ci.org/FND/markdown-checklist.png)](http://travis-ci.org/FND/markdown-checklist)" README
	sed -i "3i[![coverage](https://coveralls.io/repos/FND/markdown-checklist/badge.png)](https://coveralls.io/r/FND/markdown-checklist)" README

test: clean
	py.test -s --tb=short test

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
	rm -r markdown_checklist.egg-info || true
