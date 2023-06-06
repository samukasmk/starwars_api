from marshmallow_mongoengine import fields

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from starwars_api.rest_apis.starwars.serializers.base import BaseSerializer


class MovieRelatedPlanetsDetailsSerializer(BaseSerializer):
    class Meta:
        model = Planet


class MovieSerializer(BaseSerializer):
    planets_details = fields.List(fields.Nested(MovieRelatedPlanetsDetailsSerializer), dump_only=True)

    class Meta:
        model = Movie
