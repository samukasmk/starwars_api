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
activate-commit-msg-fmt:
	@echo "Installing hook: commit-msg (to format commit messages) ..."
	@find .git/hooks/commit-msg -type l -delete 2> /dev/null || true
	@ln -s ../../scripts/git-hooks/hooks/commit-msg $(GIT_CONFIG_DIR)/hooks/commit-msg

deactivate-commit-msg-fmt:
	@echo "Uninstalling hook: commit-msg ..."
	@find .git/hooks/commit-msg -type l -delete 2> /dev/null || true

activate-commit-checks:
	@echo "Installing hook: pre-commit (to run 'make test' before commit) ..."
	@find .git/hooks/pre-commit -type l -delete 2> /dev/null || true
	@ln -s ../../scripts/git-hooks/hooks/pre-commit $(GIT_CONFIG_DIR)/hooks/pre-commit

deactivate-commit-checks:
	@echo "Uninstalling hook: pre-commit ..."
	@find .git/hooks/pre-commit -type l -delete 2> /dev/null || true

activate-all-git-hooks: activate-commit-msg-fmt activate-commit-checks

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

clean-poetry-lock-file:
	@rm poetry.lock 2> /dev/null || true

poetry-install:
	@$(POETRY) install

poetry-export:
	@echo Building requirements file: requirements.txt
	@$(POETRY) export --only=main -f requirements.txt --without-hashes | sed 's/ ;.*//g' > requirements.txt
	@echo Building requirements file: requirements-dev.txt
	@$(POETRY) export --with=dev -f requirements.txt --without-hashes | sed 's/ ;.*//g' > requirements-dev.txt

build-requirements-local: pip-install-poetry \
                          recreate-poetry-env \
                          clean-poetry-lock-file \
                          poetry-install \
                          poetry-export

build-requirements-venv:
	@make USE_POETRY_IN_VENV=true build-requirements-local

build-requirements: build-requirements-venv


### actions to organize and clean project files
clean-cache-files:
	@find . -iname '*.pyc' -delete 2> /dev/null || true
	@find . -iname '*.pyo' -delete 2> /dev/null || true
	@find . -name '*,cover' -delete 2> /dev/null || true
	@find ./ -name '*~' -delete 2> /dev/null || true
	@find . -iname __pycache__ -delete 2> /dev/null || true
	@rm -rf .cache 2> /dev/null || true
	@rm -rf .mypy_cache 2> /dev/null || true
	@rm -fr .coverage 2> /dev/null || true
	@rm -fr .pytest_cache 2> /dev/null || true
	@rm -rf *.egg-info 2> /dev/null || true

clean-coverage-files:
	@rm -fr htmlcov 2> /dev/null || true
	@rm -fr junit.xml 2> /dev/null || true
	@rm -fr coverage.xml 2> /dev/null || true

fix-coverage-permissions:
	@chmod 777 coverage.xml 2> /dev/null || true
	@chmod -R 777 htmlcov 2> /dev/null || true

clean: clean-cache-files clean-coverage-files


### actions to format the source-code
fmt:
	@isort .
	@black .
	@make clean-cache-files


### actions to run unit tests
test: fmt clean
	@pytest --cov=app --cov-report term:skip-covered --cov-report html:htmlcov --junit-xml=coverage.xml
	@make clean-cache-files
	@make fix-coverage-permissions

### actions to run security checkers
sec-check:
	@pip-audit --requirement requirements.txt
	@pip-check
	@safety check


## actions to run flask app
runserver:
	@gunicorn -b 0.0.0.0:5000 -w 4 'starwars_api.base:create_app_wsgi'

devserver:
	@python manage.py run

debugserver:
	@python manage.py run --debug
