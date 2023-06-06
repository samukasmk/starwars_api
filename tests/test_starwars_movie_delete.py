import pytest

from starwars_api.models.starwars.movie import Movie


def test_starwars_movie_delete_not_found(app, client):
    # check empty state
    assert Movie.objects().count() == 0

    # check empty response
    response = client.delete("/api/starwars/movie/64544700cea03ff1eedb3735/")
    assert response.status_code == 404
    assert response.json == {
        "message": "Movie resource not found. You have requested this URI "
        "[/api/starwars/movie/64544700cea03ff1eedb3735/] but did you mean "
        "/api/starwars/movie/<regex('[a-fA-F0-9]{24}'):movie_id>/ or "
        "/api/starwars/movie/ ?"
    }


@pytest.mark.freeze_time("2023-05-05")
def test_starwars_movie_delete_document(client, mock_planet_models, planets_objects_ids, mock_movie_models):
    movies_counter = 6

    # check creation
    assert Movie.objects().count() == movies_counter
    for movie_model in mock_movie_models:
        # check http response
        response = client.delete(f"/api/starwars/movie/{movie_model['id']}/")
        assert response.status_code == 204
        # check deletion on mongo
        movies_counter -= 1
        assert Movie.objects().count() == movies_counter
