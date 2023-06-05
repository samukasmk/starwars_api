"""
flask builtin fixtures
"""

import pytest

from starwars_api.base import create_app


@pytest.fixture(scope="session")
def app():
    """Flask app fixture forcing [testing] settings.toml scope"""
    return create_app(FORCE_ENV_FOR_DYNACONF="testing")
