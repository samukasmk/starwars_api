### actions to install static virtualenv
install:
	@pip install -r requirements.txt

install-dev:
	@pip install -r requirements-dev.txt


### actions to manage packages with poetry
poetry-cmd:
	@pip install -U pip poetry

poetry-recreate-env: poetry-cmd
	@poetry env remove --all
	@poetry env use python

poetry-env-install: poetry-recreate-env
	@poetry install --only main --no-root
	@poetry export --only main -f requirements.txt --without-hashes | sed 's/ ;.*//g' > requirements.txt

poetry-env-install-dev: poetry-recreate-env
	@poetry install --with dev --no-root
	@echo '-r requirements.txt\n' > requirements-dev.txt
	@poetry export --with dev -f requirements.txt --with dev --without-hashes | sed 's/ ;.*//g' >> requirements-dev.txt

poetry-recreate-lock:
	@make poetry-env-install
	@make poetry-env-install-dev
	@poetry env remove --all


### actions to organize and clean project files
clean-cache-files:
	@find . -iname '*.pyc' -delete
	@find . -iname '*.pyo' -delete
	@find . -name '*,cover' -delete
	@find ./ -name '*~' -exec rm -f {} \;
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
