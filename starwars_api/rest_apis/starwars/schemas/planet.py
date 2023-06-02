from marshmallow_mongoengine import ModelSchema

from starwars_api.models.starwars.planet import Planet


class PlanetSchema(ModelSchema):
    class Meta:
        model = Planet
