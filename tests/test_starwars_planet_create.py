import copy
from datetime import datetime

import pytest

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from tests.datasets.planets import sample_planets_api_requests


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_planet_create(client):
    # check creation
    assert Movie.objects().count() == 0
    assert Planet.objects().count() == 0

    requested_planets_data = sample_planets_api_requests()

    for idx, requested_planet in enumerate(requested_planets_data):
        # check http response
        response = client.post("/api/starwars/planet/", json=requested_planet)
        assert response.status_code == 200
        # check dynamic object ids fields
        response_json = copy.deepcopy(response.json)
        assert response_json.pop("id", None)
        assert response_json.pop("created_at", None) == datetime.now().isoformat()
        assert response_json.pop("updated_at", None) == datetime.now().isoformat()
        # check static values
        assert response_json == requested_planets_data[idx]
