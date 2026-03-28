
.PHONY: help
help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

.PHONY: clean
clean:		## Remove python cache files
	find . -name '__pycache__' | xargs rm -rf
	find . -name '*.pyc' -delete
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf .coverage

.PHONY: docs
docs:		## Build docs
	cd docs && make docs

.PHONY: install-dev
install-dev:	## Install packages for development
	@./dev/install

.PHONY: lint
lint:		## Run linters
	@uv run ./dev/lint fix

.PHONY: lint-check
lint-check:	## Run linters in check mode
	@uv run ./dev/lint

.PHONY: test
test:		## Test with python 3.8 with coverage
	@uv run pytest -x -v --cov --cov-report xml

.PHONY: publish
publish:	## Release to pypi
	@uv build && uv publish --token $(PYPI_TOKEN)

.PHONY: notebook
notebook:	## Run Jupyter notebook server
	@uv run ./dev/start-jupyter 9095

.PHONY: book
book:		## Build static jupyter {book}
	uv run jupyter-book build docs --all

.PHONY: publish-book
publish-book:	## Publish the book to github pages
	uv run ghp-import -n -p -f docs/_build/html

.PHONY: outdated
outdated:	## Show outdated packages
	uv tree --outdated
