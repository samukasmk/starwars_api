import pytest

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from tests.datasets.movies import sample_movies_api_requests
from tests.datasets.planets import sample_planets_api_requests


@pytest.fixture(scope="function")
def mock_planet_models(app):
    """Create planet model objects in mongodb"""
    # ensure clean test case
    assert Planet.objects().count() == 0

    # create planet models
    mocked_planet_models = [
        Planet(**planet_requested_payload).save() for planet_requested_payload in sample_planets_api_requests()
    ]

    # ensure test case is builted success
    assert Planet.objects().count() == 6

    return mocked_planet_models


@pytest.fixture(scope="function")
def existing_planet_ids(mock_planet_models):
    return [str(planet.id) for planet in mock_planet_models]


@pytest.fixture(scope="function")
def planets_objects_ids(existing_planet_ids):
    return [existing_planet_ids[0:i] for i in range(1, len(existing_planet_ids) + 1)]


@pytest.fixture(scope="function")
def mock_movie_models(app, mock_planet_models, planets_objects_ids):
    """Create planet model objects in mongodb"""

    # ensure clean test case
    assert Movie.objects().count() == 0

    # create movies models
    mocked_movies_models = [
        Movie(**movie_requested_payload).save()
        for movie_requested_payload in sample_movies_api_requests(planets_objects_ids)
    ]

    # ensure test case is builted success
    assert Movie.objects().count() == 6

    return mocked_movies_models


@pytest.fixture(scope="function")
def existing_movies_ids(mock_movie_models):
    return [str(movie.id) for movie in mock_movie_models]


@pytest.fixture(scope="function")
def movies_objects_ids(existing_movies_ids):
    return [existing_movies_ids[0:i] for i in range(1, len(existing_movies_ids) + 1)]
