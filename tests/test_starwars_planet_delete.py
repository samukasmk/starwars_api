import pytest

from starwars_api.models.starwars.planet import Planet


def test_starwars_planet_delete_not_found(app, client):
    # check empty state
    assert Planet.objects().count() == 0

    # check empty response
    response = client.delete("/api/starwars/planet/64544700cea03ff1eedb3735/")
    assert response.status_code == 404
    assert response.json == {
        "message": "Planet resource not found. You have requested this URI "
        "[/api/starwars/planet/64544700cea03ff1eedb3735/] but did you mean "
        "/api/starwars/planet/<regex('[a-fA-F0-9]{24}'):planet_id>/ or "
        "/api/starwars/planet/ ?"
    }


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_planet_delete_document(client, mock_movie_models, movies_objects_ids, mock_planet_models):
    planets_counter = 6

    # check creation
    assert Planet.objects().count() == planets_counter
    for planet_model in mock_planet_models:
        # check http response
        response = client.delete(f"/api/starwars/planet/{planet_model['id']}/")
        assert response.status_code == 204
        # check deletion on mongo
        planets_counter -= 1
        assert Planet.objects().count() == planets_counter
