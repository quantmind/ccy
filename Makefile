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

install:	## install packages for development
	@pip install -U pip poetry
	@poetry install

lint:		## run linters
	@poetry run dev/lint

test:		## test with python 3.8 with coverage
	@poetry run pytest -x -v --cov --cov-report xml

codecov:	## upload code coverage
	@poetry run codecov --token $(CODECOV_TOKEN) --file ./build/coverage.xml

publish:	## release to pypi and github tag
	@poetry publish --build -u lsbardel -p $(PYPI_PASSWORD)

outdated:	## Show outdated packages
	poetry show -o -a
