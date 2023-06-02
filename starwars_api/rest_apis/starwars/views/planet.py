from flask_restx import Resource

from starwars_api.rest_apis.starwars.types import PlanetPayload, PlanetsPayload


class PlanetListCreateAPIResource(Resource):
    """API Endpoint to create and list many planets resource"""

    def get(self) -> PlanetsPayload:
        """List all planets data"""
        return [{"id": 1, "name": "hello world"}, {"id": 2, "name": "hello world 2"}]

    def post(self) -> PlanetPayload:
        """Create a planet data"""
        return {"id": 1, "name": "hello world"}


class PlanetDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific planet resource"""

    def get(self, planet_pk: int) -> PlanetPayload:
        """Retrieve a planet data"""
        return {"id": planet_pk, "name": "hello world"}

    def put(self, planet_pk: int) -> PlanetPayload:
        """Update a planet data"""
        return {"id": planet_pk, "name": "hello world"}

    def patch(self, planet_pk: int) -> PlanetPayload:
        """Partial update a planet data"""
        return {"id": planet_pk, "name": "hello world"}

    def delete(self, planet_pk: int) -> PlanetPayload:
        """Delete a planet data"""
        return {"id": planet_pk, "name": "hello world"}
