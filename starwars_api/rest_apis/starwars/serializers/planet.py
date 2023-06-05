from marshmallow_mongoengine import fields

from starwars_api.models.starwars.movie import Movie
from starwars_api.models.starwars.planet import Planet
from starwars_api.rest_apis.starwars.serializers.base import BaseSerializer


class PlanetRelatedMoviesDetailsSerializer(BaseSerializer):
    class Meta:
        model = Movie


class PlanetSerializer(BaseSerializer):
    movies = fields.List(fields.ObjectId, dump_only=True)
    movies_details = fields.List(fields.Nested(PlanetRelatedMoviesDetailsSerializer), dump_only=True)

    class Meta:
        model = Planet
