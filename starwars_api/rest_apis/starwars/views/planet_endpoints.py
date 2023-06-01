from flask_restful import Resource


class PlanetResource(Resource):
    """Enpoint to expose /planet resources"""

    def get(self, planet_pk: int) -> dict[str, object]:
        """Retrieve a planet data"""
        return {"id": planet_pk, "name": "hello world"}
