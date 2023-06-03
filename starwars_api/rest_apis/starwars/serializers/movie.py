from marshmallow_mongoengine import fields, ModelSchema as ModelSerializer

from starwars_api.models.starwars.movie import Movie


class MovieSerializer(ModelSerializer):
    id = fields.Str(dump_only=True)

    class Meta:
        model = Movie



