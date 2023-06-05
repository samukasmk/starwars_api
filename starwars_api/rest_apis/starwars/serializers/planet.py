from marshmallow_mongoengine import ModelSchema as ModelSerializer
from marshmallow_mongoengine import fields

from starwars_api.models.starwars.planet import Planet
from starwars_api.rest_apis.starwars.serializers.movie import MovieSerializer


class PlanetSerializer(ModelSerializer):
    id = fields.String(dump_only=True)
    movies = fields.List(fields.String, dump_only=True)

    class Meta:
        model = Planet
