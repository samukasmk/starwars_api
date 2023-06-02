from marshmallow_mongoengine import ModelSchema

from starwars_api.models.starwars.movie import Movie


class MovieSchema(ModelSchema):
    class Meta:
        model = Movie
