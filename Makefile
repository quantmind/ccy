.PHONY: help clean docs install lint test codecov

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:		## remove python cache files
	find . -name '__pycache__' | xargs rm -rf
	find . -name '*.pyc' -delete
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf .coverage


docs:		## build docs
	cd docs && make docs

install-dev:	## install packages for development
	@./dev/install

lint:		## Run linters
	@poetry run ./dev/lint fix


lint-check:	## Run linters in check mode
	@poetry run ./dev/lint


test:		## test with python 3.8 with coverage
	@poetry run pytest -x -v --cov --cov-report xml

publish:	## release to pypi and github tag
	@poetry publish --build -u lsbardel -p $(PYPI_PASSWORD)

notebook:	## Run Jupyter notebook server
	@poetry run ./dev/start-jupyter 9095

book:		## Build static jupyter {book}
	poetry run jupyter-book build docs --all

publish-book:	## publish the book to github pages
	poetry run ghp-import -n -p -f notebooks/_build/html
