import pytest
from flask import Flask
from pymongo import MongoClient
from starwars_api.base import create_app


# flask builtin fixtures
@pytest.fixture(scope="session")
def app() -> Flask:
    """Flask app fixture forcing [testing] settings.toml scope"""
    return create_app(FORCE_ENV_FOR_DYNACONF="testing")


def build_mongodb_testing_env(app):
    with MongoClient(app.config['MONGODB_PYTEST']) as client:
        # remove existing database
        if 'testing_starwars' in client.list_database_names():
            client.drop_database('testing_starwars')

        # create app user
        users_id = [user['_id'] for user in client.testing_starwars.command('usersInfo')['users']]
        if 'testing_starwars.testing_starwars' not in users_id:
            client.testing_starwars.command('createUser', 'testing_starwars', pwd='testing_starwars',
                                            roles=[{'role': 'readWrite', 'db': 'testing_starwars'}])

        # create database by first insert
        client.testing_starwars.auto_created.insert_one({"auto_created": True})


@pytest.fixture(autouse=True)
def run_around_tests(app):
    build_mongodb_testing_env(app)
    yield
