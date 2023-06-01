import pytest

from tests.datatest.planets_json import sample_planets


@pytest.mark.parametrize("movie_request_payload", sample_planets())
def test_retrieve_planet(client, movie_request_payload):
    """Test get all products"""
    response = client.get(f"/api/starwars/planet/{movie_request_payload['id']}/")
    assert response.status_code == 200
    assert response.get_json() == {"id": movie_request_payload["id"], "name": "hello world"}
    # assert response.get_json() == {
    #     "id": 1,
    #     "name": "Tatooine",
    #     "rotation_period": "23",
    #     "orbital_period": "304",
    #     "diameter": "10465",
    #     "climate": "arid",
    #     "gravity": "1 standard",
    #     "terrain": "desert",
    #     "surface_water": "1",
    #     "population": "200000",
    #     "films": [
    #         "https://swapi.dev/api/films/1/",
    #         "https://swapi.dev/api/films/3/",
    #         "https://swapi.dev/api/films/4/",
    #         "https://swapi.dev/api/films/5/",
    #         "https://swapi.dev/api/films/6/",
    #     ],
    #     "created": "2014-12-09T13:50:49.641000Z",
    #     "edited": "2014-12-20T20:58:18.411000Z",
    #     "url": "https://swapi.dev/api/planets/1/",
    # }
