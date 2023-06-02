from flask import Response
from flask_restx import Resource, abort

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.serializers.movie import MovieSerializer
from starwars_api.rest_apis.starwars.schemas.movie import movie_patch_fields, movie_post_fields, movie_put_fields


class MovieListCreateAPIResource(Resource):
    """API Endpoint to create and list many movies resource"""

    def get(self) -> list[dict[str, object]]:
        """List all movies data"""
        # get movies documents from mongodb
        try:
            movies = Movie.objects()
        except Exception:
            return abort(500, "Error on get Movies endpoints")

        # serialize to json response
        serializer = MovieSerializer()
        dict_response = serializer.dump(movies, many=True)
        return dict_response

    @api.expect(movie_post_fields, validate=True)
    def post(self) -> dict[str, object]:
        """Create a movie data"""
        ...


class MovieDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    def get(self, movie_id: str) -> dict[str, object]:
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
        serializer = MovieSerializer()
        dict_response = serializer.dump(movie, many=True)
        return dict_response

    @api.expect(movie_put_fields, validate=True)
    def put(self, movie_id: str) -> dict[str, object]:
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
        serializer = MovieSerializer()
        dict_response = serializer.dump(movie, many=True)
        return dict_response

    @api.expect(movie_patch_fields, validate=True)
    def patch(self, movie_id: str) -> dict[str, object]:
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
        serializer = MovieSerializer()
        dict_response = serializer.dump(movie, many=True)
        return dict_response

    def delete(self, movie_id: str) -> Response:
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
