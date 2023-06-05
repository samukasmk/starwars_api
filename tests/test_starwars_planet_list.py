import pytest
from starwars_api.models.starwars.planet import Planet


def test_starwars_planet_list_empty(app, client):
    # check empty state
    assert len(Planet.objects()) == 0

    # check empty response
    response = client.get('/api/starwars/planet/')
    assert response.status_code == 200
    assert response.json == []


@pytest.mark.freeze_time('2023-05-05')
def test_starwars_planet_list_one(app, client):
    # check empty state
    assert len(Planet.objects()) == 0

    # create as object
    Planet(**{"name": "Tatooine",
              "rotation_period": "23",
              "orbital_period": "304",
              "diameter": "10465",
              "climate": "arid",
              "gravity": "1 standard",
              "terrain": "desert",
              "surface_water": "1",
              "population": "200000"
              }).save()

    # check creation
    assert len(Planet.objects()) == 1

    # check http response
    response = client.get('/api/starwars/planet/')
    assert response.status_code == 200

    # check results
    response_json = list(response.json)
    object_id = response_json[0].pop('id', None)
    assert object_id is not None
    assert response_json == [{'climate': 'arid',
                              'created_at': '2023-05-05T00:00:00',
                              'diameter': 10465,
                              'gravity': '1 standard',
                              'name': 'Tatooine',
                              'orbital_period': 304,
                              'population': 200000,
                              'rotation_period': 23,
                              'surface_water': 1,
                              'terrain': 'desert',
                              'updated_at': '2023-05-05T00:00:00'}]

