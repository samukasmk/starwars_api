import mongoengine

from starwars_api.models.starwars.planet import Planet


class Movie(mongoengine.Document):
    """StarWars Movie model object"""

    title = mongoengine.StringField(required=True)
    opening_crawl = mongoengine.StringField(required=True)
    episode_id = mongoengine.IntField(required=True)
    director = mongoengine.StringField(required=True)
    producer = mongoengine.StringField(required=True)
    release_date = mongoengine.DateField(required=True)
    planets = mongoengine.ListField(mongoengine.ReferenceField(Planet, reverse_delete_rule=mongoengine.CASCADE))
