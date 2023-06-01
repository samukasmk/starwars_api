from typing import Optional

from flask_restful import Resource


class MovieResource(Resource):
    """Enpoint to expose /movie resources"""

    def get(self, movie_pk: int) -> list[Optional[dict]]:
        return {"id": movie_pk,
                "name": "hello world"}
