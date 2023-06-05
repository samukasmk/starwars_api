from marshmallow_mongoengine import ModelSchema as ModelSerializer
from marshmallow_mongoengine import fields

from starwars_api.models.starwars.movie import Movie


class MovieSerializer(ModelSerializer):
    id = fields.Str(dump_only=True)

    class Meta:
        model = Movie
