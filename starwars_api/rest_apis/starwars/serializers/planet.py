from marshmallow_mongoengine import fields

from starwars_api.models.starwars.planet import Planet
from starwars_api.rest_apis.starwars.serializers.base import BaseSerializer


class PlanetSerializer(BaseSerializer):
    movies = fields.List(fields.String, dump_only=True)

    class Meta:
        model = Planet
