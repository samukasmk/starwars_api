from flask_restx import Resource

from starwars_api.rest_apis.starwars.types import MoviePayload, MoviesPayload


class MovieListCreateAPIResource(Resource):
    """API Endpoint to create and list many movies resource"""

    def get(self) -> MoviesPayload:
        """List all movies data"""
        return [{"id": 1, "name": "hello world"}, {"id": 2, "name": "hello world 2"}]

    def post(self) -> MoviePayload:
        """Create a movie data"""
        return {"id": 1, "name": "hello world"}


class MovieDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    def get(self, movie_pk: int) -> MoviePayload:
        """Retrieve a movie data"""
        return {"id": movie_pk, "name": "hello world"}

    def put(self, movie_pk: int) -> MoviePayload:
        """Update a movie data"""
        return {"id": movie_pk, "name": "hello world"}

    def patch(self, movie_pk: int) -> MoviePayload:
        """Partial update a movie data"""
        return {"id": movie_pk, "name": "hello world"}

    def delete(self, movie_pk: int) -> MoviePayload:
        """Delete a movie data"""
        return {"id": movie_pk, "name": "hello world"}
