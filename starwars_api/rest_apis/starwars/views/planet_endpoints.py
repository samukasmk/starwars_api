from typing import Optional

from flask_restful import Resource


class PlanetResource(Resource):
    """Enpoint to expose /planet resources"""

    def get(self, planet_pk: int) -> list[Optional[dict]]:
        return {"id": planet_pk,
                "name": "hello world"}
