from datetime import datetime

import pytest

from starwars_api.models.starwars.planet import Planet
from tests.datasets.planets import sample_planets_api_requests


def test_starwars_planet_list_empty(app, client):
    # check empty state
    assert len(Planet.objects()) == 0

    # check empty response
    response = client.get("/api/starwars/planet/")
    assert response.status_code == 200
    assert response.json == []


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_planet_list_many(client, mock_planet_models):
    # check creation
    assert len(Planet.objects()) == 6

    # check http response
    response = client.get("/api/starwars/planet/")
    assert response.status_code == 200

    # check results
    response_json = list(response.json)
    assert len(response_json) == 6
    for idx, json_resource in enumerate(response_json):
        # check dynamic object ids fields
        assert json_resource.pop("id", None)
        assert json_resource.pop("created_at", None) == datetime.now().isoformat()
        assert json_resource.pop("updated_at", None) == datetime.now().isoformat()
        # check static values
        assert json_resource == sample_planets_api_requests()[idx]
