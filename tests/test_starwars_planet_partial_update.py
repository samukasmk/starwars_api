import copy
from datetime import datetime

import pytest

from starwars_api.models.starwars.planet import Planet
from tests.datasets.planets import sample_planets_api_requests


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_planet_partial_update(client, mock_movie_models, movies_objects_ids, mock_planet_models):
    # check creation
    assert Planet.objects().count() == 6

    requested_planets_data = sample_planets_api_requests()

    for idx, planet_model in enumerate(mock_planet_models):
        request_payload = requested_planets_data[idx]
        request_payload["diameter"] = 10000000
        # check http response
        response = client.patch(
            f"/api/starwars/planet/{planet_model['id']}/", json={"diameter": request_payload["diameter"]}
        )
        assert response.status_code == 200
        # check results
        response_json = copy.deepcopy(response.json)
        # check dynamic object ids fields
        assert response_json.pop("id", None)
        assert response_json.pop("created_at", None) == datetime.now().isoformat()
        assert response_json.pop("updated_at", None) == datetime.now().isoformat()
        # check static values
        assert response_json == request_payload
