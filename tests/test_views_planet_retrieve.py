def test_retrieve_planet(client):  # Arrange
    """Test get all products"""
    response = client.get("/api/starwars/planet/1/")
    assert response.status_code == 200
    assert response.get_json() == {"id": 1, "name": "hello world"}
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
