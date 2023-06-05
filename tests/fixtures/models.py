import pytest

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from tests.datasets.movies import sample_movies_api_requests
from tests.datasets.planets import sample_planet_api_requests


@pytest.fixture(scope="function")
def mock_planet_models(app):
    """Create planet model objects in mongodb"""
    # ensure clean test case
    assert Planet.objects().count() == 0

    # create planet models
    mocked_planet_models = [Planet(**planet_requested_payload).save()
                            for planet_requested_payload in sample_planet_api_requests()]

    # ensure test case is builted success
    assert Planet.objects().count() == 6

    return mocked_planet_models


@pytest.fixture(scope="function")
def mock_movie_models(app, mock_planet_models):
    """Create planet model objects in mongodb"""

    # ensure clean test case
    assert Movie.objects().count() == 0

    # get dynamic object ids from planets
    planets_objects_ids = [str(planet.id) for planet in mock_planet_models]

    # create movies models
    mocked_movies_models = [
        Movie(**movie_requested_payload).save()
        for movie_requested_payload in sample_movies_api_requests(planets_objects_ids)
    ]

    # ensure test case is builted success
    assert Movie.objects().count() == 6

    return mocked_movies_models
