# using poetry from external venv
USE_POETRY_IN_VENV ?= false
POETRY_VENV ?= .poetry-venv

# set poetry command parameters
PIP_BIN := pip
POETRY_BIN := poetry
# overwrite pip and poetry command definitions
ifeq ($(USE_POETRY_IN_VENV),true)
POETRY_HOME := $(POETRY_VENV)
COMMAND_PREFIX := $(POETRY_VENV)/bin/
# or use pip and poetry in local folder
else
COMMAND_PREFIX :=
POETRY_HOME := .
endif
# set poetry command
POETRY := $(COMMAND_PREFIX)$(POETRY_BIN) --directory=$(POETRY_HOME)
PIP := $(COMMAND_PREFIX)$(PIP_BIN)
# git configs
GIT_CONFIG_DIR := $(shell git rev-parse --git-dir)


### actions to install static virtualenv
install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements-dev.txt


### actions to manage git hooks
activate-git-hook-commit-msg:
	@echo "Installing hooks: commit-msg ..."
	@find .git/hooks/commit-msg -type l -delete 2> /dev/null || true
	@ln -s ../../scripts/git-hooks/hooks/commit-msg $(GIT_CONFIG_DIR)/hooks/commit-msg

activate-git-hook-pre-commit:
	@echo "Installing hooks: pre-commit ..."
	@find .git/hooks/pre-commit -type l -delete 2> /dev/null || true
	@ln -s ../../scripts/git-hooks/hooks/pre-commit $(GIT_CONFIG_DIR)/hooks/pre-commit

activate-git-hooks: git-hook-commit-msg git-hook-pre-commit

deactivate-git-hooks:
	@find .git/hooks -type l -delete 2> /dev/null


### actions to manage packages with poetry
pip-install-poetry:
	@if [ $(USE_POETRY_IN_VENV) = true ]; then \
		python -m venv $(POETRY_VENV); \
	fi
	@$(PIP) install -U pip poetry

recreate-poetry-env:
	@$(POETRY) env remove --all
	@$(POETRY) env use python

poetry-install:
	@$(POETRY) install --no-root

poetry-export:
	@echo Building requirements file: requirements.txt
	@$(POETRY) export --only=main -f requirements.txt --without-hashes | sed 's/ ;.*//g' > requirements.txt
	@echo Building requirements file: requirements-dev.txt
	@$(POETRY) export --with=dev -f requirements.txt --without-hashes | sed 's/ ;.*//g' > requirements-dev.txt

build-requirements-local: pip-install-poetry \
                          recreate-poetry-env \
                          poetry-install \
                          poetry-export

build-requirements-venv:
	@make USE_POETRY_IN_VENV=true build-requirements-local

build-requirements: build-requirements-venv


### actions to organize and clean project files
clean-cache-files:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -name '*,cover' -delete
	@find ./ -name '*~' -delete
	@find . -iname __pycache__ -delete
	@rm -rf .cache
	@rm -rf .mypy_cache
	@rm -fr .coverage
	@rm -fr .pytest_cache
	@rm -rf *.egg-info

clean-coverage-files:
	@rm -fr htmlcov
	@rm -fr junit.xml coverage.xml

fix-coverage-permissions:
	@chmod 777 ./coverage.xml
	@chmod -R 777 ./htmlcov

clean: clean-cache-files clean-coverage-files


### actions to format the source-code
fmt:
	@isort app
	@black app
	@make clean-cache-files


### actions to run unit tests
test: clean
	@pytest --cov=app --cov-report term:skip-covered --cov-report html:htmlcov --junit-xml=coverage.xml
	@make clean-cache-files
	@make fix-coverage-permission


### actions to run security checkers
sec-check:
	@pip-audit --requirement requirements.txt
	@pip-check
	@safety check
