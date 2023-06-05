import copy
from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from tests.datasets.movies import sample_movies_api_requests


def test_starwars_movie_retrieve_not_found(app, client):
    # check empty state
    assert len(Movie.objects()) == 0

    # check empty response
    response = client.get("/api/starwars/movie/64544700cea03ff1eedb3735/")
    assert response.status_code == 404
    assert response.json == {
        "message": "Movie resource not found. You have requested this URI "
        "[/api/starwars/movie/64544700cea03ff1eedb3735/] but did you mean "
        "/api/starwars/movie/<regex('[a-fA-F0-9]{24}'):movie_id>/ or "
        "/api/starwars/movie/ ?"
    }


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_movie_retrieve_many(client, mock_planet_models, planets_objects_ids, mock_movie_models):
    # check creation
    assert len(Movie.objects()) == 6

    for idx, movie_model in enumerate(mock_movie_models):

        # check http response
        response = client.get(f"/api/starwars/movie/{movie_model['id']}/")
        assert response.status_code == 200

        # check results
        response_json = copy.deepcopy(response.json)

        # check dynamic object ids fields
        assert response_json.pop("id", None)
        assert response_json.pop("created_at", None) == datetime.now().isoformat()
        assert response_json.pop("updated_at", None) == datetime.now().isoformat()
        assert all(response_json.pop("planets", None))
