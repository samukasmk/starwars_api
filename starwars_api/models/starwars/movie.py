import mongoengine


class Movie(mongoengine.Document):
    """StarWars Movie model object"""

    title = mongoengine.StringField(required=True)
    opening_crawl = mongoengine.StringField(required=True)
    episode_id = mongoengine.IntField(required=True)
    director = mongoengine.StringField(required=True)
    producer = mongoengine.StringField(required=True)
    release_date = mongoengine.DateField(required=True)

    # TODO: move this: IntegerField to: mongoengine.ReferenceField(User, reverse_delete_rule=mongoengine.CASCADE)
    planets = mongoengine.ListField(mongoengine.IntField())
