from starwars_api.models.starwars.movie import Movie


def test_starwars_planet_list_empty(app, client):
    # check empty state
    assert len(Movie.objects()) == 0

    # check empty response
    response = client.get('/api/starwars/planet/')
    assert response.status_code == 200
    assert response.json == []


def test_starwars_planet_list_empty_2(app, client):
    # check empty state
    assert len(Movie.objects()) == 0

    # check empty response
    response = client.get('/api/starwars/planet/')
    assert response.status_code == 200
    assert response.json == []
