.PHONY: help

help:
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -e 's/\\$$//' | sed -e 's/##//'

clean:		## remove python cache files
	find . -name '__pycache__' | xargs rm -rf
	find . -name '*.pyc' -delete
	rm -rf build
	rm -rf dist
	rm -rf .pytest_cache
	rm -rf .coverage


black:		## black formatting
	black ccy tests

py36:		## build python 3.6 image for testing
	docker build -f dev/Dockerfile --build-arg PY_VERSION=python:3.6.10 -t ccy36 .

py37:		## build python 3.7 image for testing
	docker build -f dev/Dockerfile --build-arg PY_VERSION=python:3.7.7 -t ccy37 .

py38:		## build python 3.8 image for testing
	docker build -f dev/Dockerfile --build-arg PY_VERSION=python:3.8.3 -t ccy38 .

test-py36:	## test with python 3.6
	@docker run --rm --network=host ccy36 pytest

test-py37:	## test with python 3.7
	@docker run --rm --network=host ccy37 pytest

test-py38:	## test with python 3.8 with coverage
	@docker run --rm \
		-v $(PWD)/build:/workspace/build \
		ccy38 \
		pytest --cov --cov-report xml

test-docs: 	## run docs in CI
	@docker run --rm \
		-v $(PWD)/build:/workspace/build \
		ccy38 \
		make docs

test-black: 	## run black check in CI
	@docker run --rm \
		-v $(PWD)/build:/workspace/build \
		ccy38 \
		black ccy tests --check

test-flake8: 	## run flake8 in CI
	@docker run --rm \
		-v $(PWD)/build:/workspace/build \
		ccy38 \
		flake8

test-codecov:	## upload code coverage
	@docker run --rm \
		-v $(PWD):/workspace \
		ccy38 \
		codecov --token $(CODECOV_TOKEN) --file ./build/coverage.xml

test-version:	## validate version with pypi
	@docker run \
		-v $(PWD):/workspace \
		ccy38 \
		agilekit git validate

bundle:		## build python 3.8 bundle
	@docker run --rm \
		-v $(PWD):/workspace \
		ccy38 \
		python setup.py sdist bdist_wheel

github-tag:	## new tag in github
	@docker run \
		-v $(PWD):/workspace \
		-e GITHUB_TOKEN=$(GITHUB_SECRET) \
		ccy38 \
		agilekit git release --yes

pypi:		## release to pypi and github tag
	@docker run --rm \
		-v $(PWD):/workspace \
		ccy38 \
		twine upload dist/* --username lsbardel --password $(PYPI_PASSWORD)

release:	## release to pypi and github tag
	make pypi
	make github-tag
