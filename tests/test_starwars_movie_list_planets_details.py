from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from tests.datasets.movies import sample_movies_api_requests


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_movie_list_planets_details(client, mock_planet_models, mock_movie_models, planets_objects_ids):
    # check creation
    assert Movie.objects().count() == 6

    # check http response
    response = client.get("/api/starwars/movie/?movies_details=true")
    assert response.status_code == 200

    # check results
    response_json = list(response.json)
    assert len(response_json) == 6
    for idx, json_resource in enumerate(response_json):
        # check dynamic object ids fields
        assert json_resource.pop("id", None)
        assert json_resource.pop("created_at", None) == datetime.now().isoformat()
        assert json_resource.pop("updated_at", None) == datetime.now().isoformat()
        # check movies details id existence
        assert all([movie_detailed["id"] for movie_detailed in json_resource.pop("planets_details", [])])
        # check field associations
        assert json_resource == sample_movies_api_requests(planets_objects_ids)[idx]
