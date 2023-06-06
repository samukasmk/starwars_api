import copy
from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from tests.datasets.movies import sample_movies_api_requests


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_movie_update(client, mock_planet_models, planets_objects_ids, mock_movie_models):
    # check creation
    assert Movie.objects().count() == 6

    requested_movies_data = sample_movies_api_requests(planets_objects_ids)

    for idx, movie_model in enumerate(mock_movie_models):
        request_payload = requested_movies_data[idx]
        request_payload["episode_id"] = 10000000
        # check http response
        response = client.put(f"/api/starwars/movie/{movie_model['id']}/", json=request_payload)
        assert response.status_code == 200
        # check results
        response_json = copy.deepcopy(response.json)
        # check dynamic object ids fields
        assert response_json.pop("id", None)
        assert response_json.pop("created_at", None) == datetime.now().isoformat()
        assert response_json.pop("updated_at", None) == datetime.now().isoformat()
        # check static values
        assert response_json == request_payload
