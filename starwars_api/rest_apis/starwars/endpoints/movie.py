from collections import namedtuple
from typing import Any

from flask import Request, request

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.endpoints.base import DetailAPIResource, ListCreateAPIResource
from starwars_api.rest_apis.starwars.queries import movie as aggregration_pipelines
from starwars_api.rest_apis.starwars.serializers.movie import MovieSerializer
from starwars_api.rest_apis.starwars.validators.movie import MovieAPIValidator

RelatedObjectId = namedtuple("ObjectId", "pk")


def get_aggregation_pipeline(flask_request: Request) -> list[object]:
    """Get aggregation pipeline for planet collection depending on which display parameter is defined"""
    if flask_request.args.get("planets_details", "").lower() == "true":
        return aggregration_pipelines.movie_related_planets_details


def normalize_aggregated_object_ids_without_pk(self, document):
    if "planets" in document.keys():
        document["planets"] = [RelatedObjectId(pk=str(object_id)) for object_id in document["planets"]]
    return document


class MovieListCreateAPIResource(ListCreateAPIResource):
    """API Endpoint to create and list movies resources"""

    model_class = Movie
    serializer_class = MovieSerializer
    normalize_document_to_serialize = normalize_aggregated_object_ids_without_pk

    @api.expect(MovieAPIValidator.displaying_parameters)
    def get(self) -> dict[Any, Any]:  # TODO: fix typing to list[dict[Any, Any]]
        """List all movies resources"""
        self.aggregations = get_aggregation_pipeline(request)
        return super().list()

    @api.expect(MovieAPIValidator.creating_payload, validate=True)
    def post(self) -> dict[Any, Any]:
        """Create a movie resource"""
        return super().create()


class MovieDetailAPIResource(DetailAPIResource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    model_class = Movie
    serializer_class = MovieSerializer
    normalize_document_to_serialize = normalize_aggregated_object_ids_without_pk

    @api.expect(MovieAPIValidator.displaying_parameters)
    def get(self, movie_id: str) -> dict[Any, Any]:
        """Retrieve a movie resource"""
        self.aggregations = get_aggregation_pipeline(request)
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

    def get_documents(self):
        documents = super().get_documents()
        return documents
