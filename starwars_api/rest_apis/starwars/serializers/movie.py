from marshmallow_mongoengine import ModelSchema as ModelSerializer

from starwars_api.models.starwars.movie import Movie


class MovieSerializer(ModelSerializer):
    class Meta:
        model = Movie
