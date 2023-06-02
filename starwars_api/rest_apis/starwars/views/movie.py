from flask_restx import Resource

from starwars_api.extensions.openapi import api
from starwars_api.rest_apis.starwars.openapi_definitions.movie import (
    movie_patch_fields,
    movie_post_fields,
    movie_put_fields,
)
from starwars_api.rest_apis.starwars.types import MoviePayload, MoviesPayload


class MovieListCreateAPIResource(Resource):
    """API Endpoint to create and list many movies resource"""

    def get(self) -> MoviesPayload:
        """List all movies data"""
        return [{"id": 1, "name": "hello world"}, {"id": 2, "name": "hello world 2"}]

    @api.expect(movie_post_fields, validate=True)
    def post(self) -> MoviePayload:
        """Create a movie data"""
        return {"id": 1, "name": "hello world"}


class MovieDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    def get(self, movie_id: int) -> MoviePayload:
        """Retrieve a movie data"""
        return {"id": movie_id, "name": "hello world"}

    @api.expect(movie_put_fields, validate=True)
    def put(self, movie_id: int) -> MoviePayload:
        """Update a movie data"""
        return {"id": movie_id, "name": "hello world"}

    @api.expect(movie_patch_fields, validate=True)
    def patch(self, movie_id: int) -> MoviePayload:
        """Partial update a movie data"""
        return {"id": movie_id, "name": "hello world"}

    def delete(self, movie_id: int) -> MoviePayload:
        """Delete a movie data"""
        return {"id": movie_id, "name": "hello world"}
