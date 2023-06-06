import copy
from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from tests.datasets.movies import sample_movies_api_requests


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_movie_create(client, mock_planet_models, planets_objects_ids):
    # check creation
    assert Planet.objects().count() == 6
    assert Movie.objects().count() == 0

    requested_movies_data = sample_movies_api_requests(planets_objects_ids)

    for idx, requested_movie in enumerate(requested_movies_data):
        # check http response
        response = client.post("/api/starwars/movie/", json=requested_movie)
        assert response.status_code == 200
        # check dynamic object ids fields
        response_json = copy.deepcopy(response.json)
        assert response_json.pop("id", None)
        assert response_json.pop("created_at", None) == datetime.now().isoformat()
        assert response_json.pop("updated_at", None) == datetime.now().isoformat()
        # check static values
        assert response_json == requested_movies_data[idx]
