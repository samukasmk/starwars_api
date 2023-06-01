import pytest

from tests.datatest.movies_json import sample_movies


@pytest.mark.parametrize("movie_request_payload", sample_movies())
def test_retrieve_movie(client, movie_request_payload):
    """Test get all products"""
    response = client.get(f"/api/starwars/movie/{movie_request_payload['id']}/")
    assert response.status_code == 200
    assert response.get_json() == {"id": movie_request_payload["id"], "name": "hello world"}
    # assert response.get_json() == {
    #     "id": 1,
    #     "title": "A New Hope",
    #     "episode_id": 4,
    #     "opening_crawl": (
    #         "It is a period of civil war.\r\nRebel spaceships, striking\r\n"
    #         "from a hidden base, have won\r\ntheir first victory against\r\n"
    #         "the evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\n"
    #         "spies managed to steal secret\r\nplans to the Empire's\r\n"
    #         "ultimate weapon, the DEATH\r\nSTAR, an armored space\r\n"
    #         "station with enough power\r\nto destroy an entire planet.\r\n\r\n"
    #         "Pursued by the Empire's\r\nsinister agents, Princess\r\n"
    #         "Leia races home aboard her\r\nstarship, custodian of the\r\n"
    #         "stolen plans that can save her\r\npeople and restore\r\n"
    #         "freedom to the galaxy...."
    #     ),
    #     "director": "George Lucas",
    #     "producer": "Gary Kurtz, Rick McCallum",
    #     "release_date": "1977-05-25",
    #     "planets": [
    #         "https://swapi.dev/api/planets/1/",
    #         "https://swapi.dev/api/planets/2/",
    #         "https://swapi.dev/api/planets/3/",
    #     ],
    #     "created": "2014-12-10T14:23:31.880000Z",
    #     "edited": "2014-12-20T19:49:45.256000Z",
    #     "url": "https://swapi.dev/api/films/1/",
    # }
