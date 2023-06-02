from flask import Blueprint, Flask
from flask_restful import Api

from starwars_api.rest_apis.starwars.views import movie_endpoints, planet_endpoints

bp = Blueprint("starwars", __name__, url_prefix="/api/starwars")
api = Api(bp)


def load_routes(app: Flask) -> None:
    """Load url routes for star wars rest api"""

    # movie endpoints
    api.add_resource(movie_endpoints.MovieListCreateAPIResource, "/movie/")
    api.add_resource(movie_endpoints.MovieDetailAPIResource, "/movie/<int:movie_pk>/")

    # planet endpoints
    api.add_resource(planet_endpoints.PlanetListCreateAPIResource, "/planet/")
    api.add_resource(planet_endpoints.PlanetDetailAPIResource, "/planet/<int:planet_pk>/")

    app.register_blueprint(bp)
