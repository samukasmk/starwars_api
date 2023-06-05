from starwars_api.models.starwars.movie import Movie
from starwars_api.rest_apis.starwars.serializers.base import BaseSerializer


class MovieSerializer(BaseSerializer):
    class Meta:
        model = Movie
