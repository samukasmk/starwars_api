from flask_restx import Resource

from starwars_api.extensions.openapi import api
from starwars_api.rest_apis.starwars.openapi_definitions.planet import (
    planet_patch_fields,
    planet_post_fields,
    planet_put_fields,
)
from starwars_api.rest_apis.starwars.types import PlanetPayload, PlanetsPayload


class PlanetListCreateAPIResource(Resource):
    """API Endpoint to create and list many planets resource"""

    def get(self) -> PlanetsPayload:
        """List all planets data"""
        return [{"id": 1, "name": "hello world"}, {"id": 2, "name": "hello world 2"}]

    @api.expect(planet_post_fields, validate=True)
    def post(self) -> PlanetPayload:
        """Create a Planet data"""
        return {"id": 1, "name": "hello world"}


class PlanetDetailAPIResource(Resource):
    """API Endpoint to retrieve, update, partial update and delete a specific planet resource"""

    def get(self, planet_id: int) -> PlanetPayload:
        """Retrieve a Planet data"""
        return {"id": planet_id, "name": "hello world"}

    @api.expect(planet_put_fields, validate=True)
    def put(self, planet_id: int) -> PlanetPayload:
        """Update a Planet data"""
        return {"id": planet_id, "name": "hello world"}

    @api.expect(planet_patch_fields, validate=True)
    def patch(self, planet_id: int) -> PlanetPayload:
        """Partial update a Planet data"""
        return {"id": planet_id, "name": "hello world"}

    def delete(self, planet_id: int) -> PlanetPayload:
        """Delete a Planet data"""
        return {"id": planet_id, "name": "hello world"}
