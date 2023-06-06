import copy
from datetime import datetime

import pytest

from starwars_api.models.starwars.planet import Planet


def test_starwars_planet_retrieve_movies_details_not_found(app, client):
    # check empty state
    assert Planet.objects().count() == 0

    # check empty response
    response = client.get("/api/starwars/planet/64544700cea03ff1eedb3735/?movies_details=true")
    assert response.status_code == 404
    assert response.json == {
        "message": "Planet resource not found. You have requested this URI "
        "[/api/starwars/planet/64544700cea03ff1eedb3735/] but did you mean "
        "/api/starwars/planet/<regex('[a-fA-F0-9]{24}'):planet_id>/ or "
        "/api/starwars/planet/ ?"
    }


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_planet_retrieve_movies_details(client, mock_movie_models, movies_objects_ids, mock_planet_models):
    # check creation
    assert Planet.objects().count() == 6

    for planet_model in mock_planet_models:
        # check http response
        response = client.get(f"/api/starwars/planet/{planet_model['id']}/?movies_details=true")
        assert response.status_code == 200
        # check results
        response_json = copy.deepcopy(response.json)
        # check dynamic object ids fields
        assert response_json.pop("id", None)
        assert response_json.pop("created_at", None) == datetime.now().isoformat()
        assert response_json.pop("updated_at", None) == datetime.now().isoformat()
        assert all(response_json.pop("movies", None))
        assert all([movie["id"] for movie in response_json.pop("movies_details", None)])
