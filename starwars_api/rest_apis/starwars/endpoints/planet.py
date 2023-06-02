from flask_restx import Resource

from starwars_api.extensions.openapi import api
from starwars_api.rest_apis.starwars.schemas.planet import planet_patch_fields, planet_post_fields, planet_put_fields


class PlanetListCreateAPIResource(Resource):
    """
    API Endpoint to create and list many planets resource
    """

    def get(self) -> list[dict[str, object]]:
        """List all planets data"""
        ...

    @api.expect(planet_post_fields, validate=True)
    def post(self) -> dict[str, object]:
        """Create a Planet data"""
        ...


class PlanetDetailAPIResource(Resource):
    """
    API Endpoint to retrieve, update, partial update
    and delete a specific planet resource
    """

    def get(self, planet_id: int) -> dict[str, object]:
        """Retrieve a Planet data"""
        ...

    @api.expect(planet_put_fields, validate=True)
    def put(self, planet_id: int) -> dict[str, object]:
        """Update a Planet data"""
        ...

    @api.expect(planet_patch_fields, validate=True)
    def patch(self, planet_id: int) -> dict[str, object]:
        """Partial update a Planet data"""
        ...

    def delete(self, planet_id: int) -> dict[str, object]:
        """Delete a Planet data"""
        ...
