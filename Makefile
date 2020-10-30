.PHONY: clean clean-build clean-pyc lint test setup help
.DEFAULT_GOAL := help

define PRINT_HELP_PYSCRIPT
import re, sys

for line in sys.stdin:
	match = re.match(r'^([a-zA-Z_-]+):.*?## (.*)$$', line)
	if match:
		target, help = match.groups()
		print("%-20s %s" % (target, help))
endef
export PRINT_HELP_PYSCRIPT

help:
	@python -c "$$PRINT_HELP_PYSCRIPT" < $(MAKEFILE_LIST)


define install_dependencies
	pip install --upgrade pip wheel
	pip install --upgrade -r requirements.$(1).txt
	pip install -e .
endef


install:  ## Install minimalist requirements to run test requirements.test.txt
	$(call install_dependencies,test)

install-dev:  ## Install requirements.dev.txt
	$(call install_dependencies,dev)

setup: ## install python project dependencies for tests
	anyblok_createdb -c app.cfg || anyblok_updatedb -c app.cfg

clean: clean-build clean-pyc clean-test ## remove all build, test, coverage and Python artifacts

clean-build: ## remove build artifacts
	rm -fr build/
	rm -fr dist/
	rm -fr .eggs/
	find . -name '*.egg-info' -exec rm -fr {} +
	find . -name '*.egg' -exec rm -f {} +

clean-pyc: ## remove Python file artifacts
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -exec rm -fr {} +

clean-test: ## remove test artifacts
	rm -fr htmlcov
	rm -fr .pytest_cache
	rm -f .coverage

lint: ## check style using pre-commit
	pre-commit install
	pre-commit run --all-files --show-diff-on-failure

test: ## run tests
	ANYBLOK_CONFIG_FILE=app.cfg py.test -v -s anyblok_background_tasks

documentation: ## generate documentation
	anyblok_doc -c app.cfg --doc-format RST --doc-output doc/source/apidoc.rst
	make -C doc/ html
