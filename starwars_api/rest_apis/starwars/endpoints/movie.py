from flask import Response
from werkzeug.exceptions import HTTPException

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.endpoints.base import DetailAPIResource, ListCreateAPIResource
from starwars_api.rest_apis.starwars.fields.movie import MovieAPIFields
from starwars_api.rest_apis.starwars.serializers.movie import MovieSerializer


class MovieListCreateAPIResource(ListCreateAPIResource):
    """API Endpoint to create and list movies resources"""

    model_class = Movie
    serializer_class = MovieSerializer

    def get(self) -> Response | HTTPException:
        """List all movies resources"""
        return super().list()

    @api.expect(MovieAPIFields.post, validate=True)
    def post(self) -> Response | HTTPException:
        """Create a movie resource"""
        return super().create()


class MovieDetailAPIResource(DetailAPIResource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    model_class = Movie
    serializer_class = MovieSerializer

    def get(self, movie_id: str) -> Response | HTTPException:
        """Retrieve a movie resource"""
        return super().retrieve(movie_id)

    @api.expect(MovieAPIFields.put, validate=True)
    def put(self, movie_id: str) -> Response | HTTPException:
        """Update a movie resource"""
        return super().update(movie_id)

    @api.expect(MovieAPIFields.patch, validate=True)
    def patch(self, movie_id: str) -> Response | HTTPException:
        """Partial update a movie resource"""
        return super().update(movie_id)

    def delete(self, movie_id: str) -> Response | HTTPException:
        """Delete a movie resource"""
        return super().destroy(movie_id)
