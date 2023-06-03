from marshmallow_mongoengine import fields, ModelSchema as ModelSerializer

from starwars_api.models.starwars.planet import Planet


class PlanetSerializer(ModelSerializer):
    id = fields.Str(dump_only=True)
    movies = fields.List(fields.ObjectId(dump_only=True), dump_only=True)

    class Meta:
        model = Planet
