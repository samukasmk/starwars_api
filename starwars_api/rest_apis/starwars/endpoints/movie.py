from flask import Response
from flask_restx import Resource, abort
from werkzeug.exceptions import HTTPException
from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.serializers.movie import MovieSerializer
from starwars_api.rest_apis.starwars.schemas.movie import movie_patch_fields, movie_post_fields, movie_put_fields


class MovieListCreateAPIResource(Resource):
    """API Endpoint to create and list many movies resource"""

    def get(self) -> Response | HTTPException:
        """List all movies data"""
        # get movies documents from mongo
        try:
            movies = Movie.objects()
        except Exception:
            return abort(code=500, message="Error on get Movies resources")

        # serialize found mongo documents to json response
        serializer = MovieSerializer()
        response_dict = serializer.dump(movies, many=True)

        return Response(status=200, response=response_dict)

    @api.expect(movie_post_fields, validate=True)
    def post(self) -> Response | HTTPException:
        """Create a movie data"""
        # deserialize json payload to create a new mongo document
        serializer = MovieSerializer()
        movie = serializer.load(api.payload)

        # create mongo document
        try:
            movie.save()
        except Exception:
            return abort(code=500, message="Error on create Movie resource")

        # serialize created mongo document to json response
        response_dict = serializer.dump(movie)

        return Response(status=200, response=response_dict)


class MovieDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific movie resource"""

    def get(self, movie_id: str) -> Response | HTTPException:
        """Retrieve a movie data"""
        # get movie document from mongo by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(code=500, message="Error on get Movie resource")

        # check if movie document was found
        if not movie:
            return abort(code=404, message="Movie resource not found")

        # serialize found mongo document to json response
        serializer = MovieSerializer()
        response_dict = serializer.dump(movie)

        return Response(status=200, response=response_dict)

    @api.expect(movie_put_fields, validate=True)
    def put(self, movie_id: str) -> Response | HTTPException:
        """Update a movie data"""
        # get movie document from mongo by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(code=500, message="Error on get Movie resource")

        # check if movie document was found
        if not movie:
            return abort(code=404, message="Movie resource not found")

        # remove id field to prevent duplicity failures
        api.payload.pop('id', None)

        # update movie document in mongo with new data
        try:
            updated_movie = movie.update(**api.payload)
        except Exception:
            return abort(code=500, message="Error on update Movie resource data")

        # serialize updated mongo document to json response
        serializer = MovieSerializer()
        response_dict = serializer.dump(updated_movie)

        return Response(status=200, response=response_dict)

    @api.expect(movie_patch_fields, validate=True)
    def patch(self, movie_id: str) -> Response | HTTPException:
        """Partial update a movie data"""
        # get movie document from mongo by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(code=500, message="Error on get Movie resource")

        # check if movie document was found
        if not movie:
            return abort(code=404, message="Movie resource not found")

        # remove id field to prevent duplicity failures
        api.payload.pop('id', None)

        # update movie document in mongo with new data
        try:
            updated_movie = movie.update(**api.payload)
        except Exception:
            return abort(code=500, message="Error on update Movie resource data")

        # serialize updated mongo document to json response
        serializer = MovieSerializer()
        response_dict = serializer.dump(updated_movie)

        return Response(status=200, response=response_dict)

    def delete(self, movie_id: str) -> Response | HTTPException:
        """Delete a movie data"""
        # get movie document from mongo by objectId
        try:
            movie = Movie.objects.with_id(object_id=movie_id)
        except Exception:
            return abort(code=500, message="Error on search Movie resource")

        # check if movie document exists
        if not movie:
            return abort(code=404, message="Movie resource not found")

        # delete movie document from mongo
        try:
            movie.delete()
        except Exception:
            return abort(code=500, message="Error on delete Movie resource")

        return Response(status=204)
