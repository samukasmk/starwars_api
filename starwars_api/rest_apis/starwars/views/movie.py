from flask import Response
from flask_restx import Resource, abort

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.openapi_definitions.movie import (
    movie_patch_fields,
    movie_post_fields,
    movie_put_fields,
)
from starwars_api.rest_apis.starwars.schemas.movie import MovieSchema
from starwars_api.rest_apis.starwars.types import MoviePayload, MoviesPayload


class MovieListCreateAPIResource(Resource):
    """API Endpoint to create and list many movies resource"""

    def get(self) -> MoviesPayload:
        """List all movies data"""
        # get movies documents from mongodb
        try:
            movies = Movie.objects()
        except Exception:
            return abort(500, "Error on get Movies resources")

        # serialize to json response
        schema = MovieSchema()
        dict_response = schema.dump(movies, many=True)
        return dict_response

    @api.expect(movie_post_fields, validate=True)
    def post(self) -> MoviePayload:
        """Create a movie data"""
        ...


class MovieDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    def get(self, movie_id: str) -> MoviePayload:
        """Retrieve a movie data"""
        # get movie document from mongodb by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(500, "Error on get Movie resource")

        # check if movie document exists
        if not movie:
            return abort(404, "Movie not found")

        # serialize to json response
        schema = MovieSchema()
        dict_response = schema.dump(movie, many=True)
        return dict_response

    @api.expect(movie_put_fields, validate=True)
    def put(self, movie_id: str) -> MoviePayload:
        """Update a movie data"""
        # get movie document from mongodb by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(500, "Error on get Movie resource")

        # check if movie document exists
        if not movie:
            return abort(404, "Movie not found")

        # serialize to json response
        schema = MovieSchema()
        dict_response = schema.dump(movie, many=True)
        return dict_response

    @api.expect(movie_patch_fields, validate=True)
    def patch(self, movie_id: str) -> MoviePayload:
        """Partial update a movie data"""
        # get movie document from mongodb by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(500, "Error on get Movie resource")

        # check if movie document exists
        if not movie:
            return abort(404, "Movie not found")

        # serialize to json response
        schema = MovieSchema()
        dict_response = schema.dump(movie, many=True)
        return dict_response

    def delete(self, movie_id: str) -> MoviePayload:
        """Delete a movie data"""
        # get movie document from mongodb by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(500, "Error on search Movie resource")

        # check if movie document exists
        if not movie:
            return abort(404, "Movie not found")

        # delete document from mongodb
        try:
            movie.delete()
        except Exception:
            return abort(500, "Error on delete Movie resource")
        return Response(status=204)
