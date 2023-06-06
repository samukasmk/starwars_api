"""
mongodb cleaning fixtures
"""

import pytest
from pymongo import MongoClient


def pymongo_client(app):
    return MongoClient(app.config["MONGODB_PYTEST"])


def cleanup_testing_database(app):
    """
    Remove existing database for next test
    """
    with pymongo_client(app) as client:
        if "testing_starwars" in client.list_database_names():
            client.drop_database("testing_starwars")


def build_mongodb_testing_env(app):
    """
    Create mongo database and user to clean the test env
    """
    with pymongo_client(app) as client:
        # create app user
        users_id = [user["_id"] for user in client.testing_starwars.command("usersInfo")["users"]]
        if "testing_starwars.testing_starwars" not in users_id:
            client.testing_starwars.command(
                "createUser",
                "testing_starwars",
                pwd="testing_starwars",
                roles=[{"role": "readWrite", "db": "testing_starwars"}],
            )

        # create database by first insert
        client.testing_starwars.auto_created.insert_one({"auto_created": True})


@pytest.fixture(autouse=True)
def run_around_tests(app):
    # run before each test
    cleanup_testing_database(app)
    build_mongodb_testing_env(app)
    yield
    # run after each test
    cleanup_testing_database(app)
