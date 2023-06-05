from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from tests.datasets.planets import sample_planets_api_requests


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_planet_list_movies_details(client, mock_planet_models, mock_movie_models, movies_objects_ids):
    # check creation
    assert len(Planet.objects()) == 6

    # check http response
    response = client.get("/api/starwars/planet/?movies_details=true")
    assert response.status_code == 200

    movies_objects_ids.reverse()

    # check results
    response_json = list(response.json)
    assert len(response_json) == 6
    for idx, json_resource in enumerate(response_json):
        # check dynamic object ids fields
        assert json_resource.pop("id", None)
        assert json_resource.pop("created_at", None) == datetime.now().isoformat()
        assert json_resource.pop("updated_at", None) == datetime.now().isoformat()
        # check movies array list existence
        assert all(json_resource.pop("movies", []))
        # check movies details id existence
        assert all([movie_detailed["id"] for movie_detailed in json_resource.pop("movies_details", [])])
        # check field associations
        assert json_resource == sample_planets_api_requests()[idx]
