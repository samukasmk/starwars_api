import mongoengine


class Planet(mongoengine.Document):
    """StarWars Planet model object"""

    name = mongoengine.StringField(required=True)
    rotation_period = mongoengine.IntField(required=True)
    orbital_period = mongoengine.IntField(required=True)
    diameter = mongoengine.IntField(required=True)
    climate = mongoengine.StringField(required=True)
    gravity = mongoengine.StringField(required=True)
    terrain = mongoengine.StringField(required=True)
    surface_water = mongoengine.IntField(required=True)
    population = mongoengine.IntField(required=True)

    # TODO: move this: IntegerField to: mongoengine.ReferenceField(User, reverse_delete_rule=mongoengine.CASCADE)
    movies = mongoengine.ListField(mongoengine.IntField())
