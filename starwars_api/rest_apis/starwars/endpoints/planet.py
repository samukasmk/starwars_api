from typing import Any

from starwars_api.extensions.openapi import api
from starwars_api.models.starwars.planet import Planet
from starwars_api.rest_apis.starwars.endpoints.base import DetailAPIResource, ListCreateAPIResource
from starwars_api.rest_apis.starwars.queries.planet import planet_movies_aggregation
from starwars_api.rest_apis.starwars.serializers.planet import PlanetSerializer
from starwars_api.rest_apis.starwars.validators.planet import PlanetAPIValidator


class PlanetListCreateAPIResource(ListCreateAPIResource):
    """API Endpoint to create and list planets resources"""

    model_class = Planet
    serializer_class = PlanetSerializer

    @api.expect(PlanetAPIValidator.displaying_parameters)
    def get(self) -> dict[Any, Any]:  # TODO: fix typing to list[dict[Any, Any]]
        """List all planets resources"""
        self.aggregations = planet_movies_aggregation
        return super().list()

    @api.expect(PlanetAPIValidator.creating_payload, validate=True)
    def post(self) -> dict[Any, Any]:
        """Create a planet resource"""
        return super().create()


class PlanetDetailAPIResource(DetailAPIResource):
    """API Endpoint to retrieve, update, partial update and delete a specific planet resource"""

    model_class = Planet
    serializer_class = PlanetSerializer

    @api.expect(PlanetAPIValidator.displaying_parameters)
    def get(self, planet_id: str) -> dict[Any, Any]:
        """Retrieve a planet resource"""
        self.aggregations = planet_movies_aggregation
        return super().retrieve(planet_id)

    @api.expect(PlanetAPIValidator.updating_payload, validate=True)
    def put(self, planet_id: str) -> dict[Any, Any]:
        """Update a planet resource"""
        return super().update(planet_id)

    @api.expect(PlanetAPIValidator.partial_updating_payload, validate=True)
    def patch(self, planet_id: str) -> dict[Any, Any]:
        """Partial update a planet resource"""
        return super().update(planet_id)

    def delete(self, planet_id: str) -> tuple:
        """Delete a planet resource"""
        return super().destroy(planet_id)
