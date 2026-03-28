
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

.PHONY: docs
docs:		## Build mkdocs site
	uv run mkdocs build

.PHONY: docs-serve
docs-serve:	## Serve docs locally with live reload
	uv run mkdocs serve --livereload --watch ccy --watch docs

.PHONY: publish-docs
publish-docs:	## Publish docs to github pages
	uv run mkdocs gh-deploy --force

.PHONY: outdated
outdated:	## Show outdated packages
	uv tree --outdated
