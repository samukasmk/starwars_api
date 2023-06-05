from typing import Any

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.endpoints.base import DetailAPIResource, ListCreateAPIResource
from starwars_api.rest_apis.starwars.serializers.movie import MovieSerializer
from starwars_api.rest_apis.starwars.validators.movie import MovieAPIValidator


class MovieListCreateAPIResource(ListCreateAPIResource):
    """API Endpoint to create and list movies resources"""

    model_class = Movie
    serializer_class = MovieSerializer

    @api.expect(MovieAPIValidator.displaying_parameters)
    def get(self) -> dict[Any, Any]:  # TODO: fix typing to list[dict[Any, Any]]
        """List all movies resources"""
        return super().list()

    @api.expect(MovieAPIValidator.creating_payload, validate=True)
    def post(self) -> dict[Any, Any]:
        """Create a movie resource"""
        return super().create()


class MovieDetailAPIResource(DetailAPIResource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    model_class = Movie
    serializer_class = MovieSerializer

    @api.expect(MovieAPIValidator.displaying_parameters)
    def get(self, movie_id: str) -> dict[Any, Any]:
        """Retrieve a movie resource"""
        return super().retrieve(movie_id)

    @api.expect(MovieAPIValidator.updating_payload, validate=True)
    def put(self, movie_id: str) -> dict[Any, Any]:
        """Update a movie resource"""
        return super().update(movie_id)

    @api.expect(MovieAPIValidator.partial_updating_payload, validate=True)
    def patch(self, movie_id: str) -> dict[Any, Any]:
        """Partial update a movie resource"""
        return super().update(movie_id)

    def delete(self, movie_id: str) -> tuple:
        """Delete a movie resource"""
        return super().destroy(movie_id)
