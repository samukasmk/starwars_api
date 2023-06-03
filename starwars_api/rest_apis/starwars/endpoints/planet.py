from flask import Response
from werkzeug.exceptions import HTTPException

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.planet import Planet
from starwars_api.rest_apis.starwars.endpoints.base import DetailAPIResource, ListCreateAPIResource
from starwars_api.rest_apis.starwars.fields.planet import PlanetAPIFields
from starwars_api.rest_apis.starwars.serializers.planet import PlanetSerializer


class PlanetListCreateAPIResource(ListCreateAPIResource):
    """API Endpoint to create and list planets resources"""

    model_class = Planet
    serializer_class = PlanetSerializer

    def get(self) -> Response | HTTPException:
        """List all planets resources"""
        return super().list()

    @api.expect(PlanetAPIFields.post, validate=True)
    def post(self) -> Response | HTTPException:
        """Create a planet resource"""
        return super().create()


class PlanetDetailAPIResource(DetailAPIResource):
    """API Endpoint to retrieve, update, partial update and delete a specific planet resource"""

    model_class = Planet
    serializer_class = PlanetSerializer

    def get(self, planet_id: str) -> Response | HTTPException:
        """Retrieve a planet resource"""
        return super().retrieve(planet_id)

    @api.expect(PlanetAPIFields.put, validate=True)
    def put(self, planet_id: str) -> Response | HTTPException:
        """Update a planet resource"""
        return super().update(planet_id)

    @api.expect(PlanetAPIFields.patch, validate=True)
    def patch(self, planet_id: str) -> Response | HTTPException:
        """Partial update a planet resource"""
        return super().update(planet_id)

    def delete(self, planet_id: str) -> Response | HTTPException:
        """Delete a planet resource"""
        return super().destroy(planet_id)
