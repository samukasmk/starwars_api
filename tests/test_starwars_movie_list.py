from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from tests.datasets.movies import sample_movies_api_requests


def test_starwars_movie_list_empty(app, client):
    # check empty state
    assert len(Movie.objects()) == 0

    # check empty response
    response = client.get("/api/starwars/movie/")
    assert response.status_code == 200
    assert response.json == []


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_movie_list_many(client, mock_planet_models, planets_objects_ids, mock_movie_models):
    # check creation
    assert len(Movie.objects()) == 6

    # check http response
    response = client.get("/api/starwars/movie/")
    assert response.status_code == 200

    requested_movies_data = sample_movies_api_requests(planets_objects_ids)

    # check results
    response_json = list(response.json)
    assert len(response_json) == 6
    for idx, json_resource in enumerate(response_json):
        # check dynamic object ids fields
        assert json_resource.pop("id", None)
        assert json_resource.pop("created_at", None) == datetime.now().isoformat()
        assert json_resource.pop("updated_at", None) == datetime.now().isoformat()
        # check static values
        assert json_resource == requested_movies_data[idx]
