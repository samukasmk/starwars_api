import mongoengine

from starwars_api.models.starwars.base import BaseDocument


class Planet(BaseDocument):
    """StarWars Planet model object"""

    name = mongoengine.StringField(required=True)
    rotation_period = mongoengine.IntField(required=True)
    orbital_period = mongoengine.IntField(required=True)
    diameter = mongoengine.IntField(required=True)
    climate = mongoengine.StringField(required=True)
    gravity = mongoengine.StringField(required=True)
    terrain = mongoengine.StringField(required=True)
    surface_water = mongoengine.IntField(required=True)
    population = mongoengine.StringField(required=True)
