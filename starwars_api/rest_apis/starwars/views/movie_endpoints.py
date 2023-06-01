from flask_restful import Resource


class MovieResource(Resource):
    """Enpoint to expose /movie resources"""

    def get(self, movie_pk: int) -> dict[str, object]:
        """Retrieve a movie data"""
        return {"id": movie_pk, "name": "hello world"}
