from marshmallow_mongoengine import ModelSchema as ModelSerializer

from starwars_api.models.starwars.planet import Planet


class PlanetSerializer(ModelSerializer):
    class Meta:
        model = Planet
