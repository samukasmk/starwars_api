import pytest
from flask import Flask
from pymongo import MongoClient
from starwars_api.base import create_app


# flask builtin fixtures
@pytest.fixture(scope="session")
def app() -> Flask:
    """Flask app fixture forcing [testing] settings.toml scope"""
    return create_app(FORCE_ENV_FOR_DYNACONF="testing")


def create_pymongo_client(app):
    return MongoClient(app.config['MONGODB_PYTEST'])


def cleanup_mongodb_testing_env(app):
    client = create_pymongo_client(app)
    if 'testing_starwars' in client.list_database_names():
        client.drop_database('testing_starwars')
    try:
        client.testing_starwars.command('dropUser', 'testing_starwars')
    except:
        ...


def create_mongodb_testing_env(app):
    client = create_pymongo_client(app)
    # create database by first insert
    client.testing_starwars.auto_created.insert_one({"auto_created": True})
    # create app user
    client.testing_starwars.command('createUser', 'testing_starwars', pwd='testing_starwars',
                                    roles=[{'role': 'readWrite', 'db': 'testing_starwars'}])


@pytest.fixture(autouse=True)
def run_around_tests(app):
    cleanup_mongodb_testing_env(app)
    create_mongodb_testing_env(app)
    yield
    cleanup_mongodb_testing_env(app)
