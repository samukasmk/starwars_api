from marshmallow_mongoengine import fields, ModelSchema as ModelSerializer

from starwars_api.models.starwars.movie import Movie


class MovieSerializer(ModelSerializer):
    _id = fields.Str(attribute='id', dump_only=True)

    class Meta:
        model = Movie



