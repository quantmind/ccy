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
	@./dev/install

lint:		## run linters
	isort .
	black .
	flake8

test:		## test with python 3.8 with coverage
	@pytest -x -v --cov --cov-report xml

codecov:	## upload code coverage
	@codecov --token $(CODECOV_TOKEN) --file ./build/coverage.xml

test-version:	## validate version with pypi
	@agilekit git validate

bundle3.6:	## build python 3.6 bundle
	@python setup.py bdist_wheel --python-tag py36

bundle3.7:	## build python 3.7 bundle
	@python setup.py bdist_wheel --python-tag py37

bundle3.8:	## build python 3.8 bundle
	@python setup.py bdist_wheel --python-tag py38

bundle3.9:	## build python 3.9 bundle
	@python setup.py sdist bdist_wheel --python-tag py39

github-tag:	## new tag in github
	@agilekit git release --yes

release-pypi:	## release to pypi and github tag
	@twine upload dist/* --username lsbardel --password $(PYPI_PASSWORD)

release:	## release to pypi and github tag
	make release-pypi
	make github-tag

version:	## display software version
	@python -c "import ccy; print(ccy.__version__)"
