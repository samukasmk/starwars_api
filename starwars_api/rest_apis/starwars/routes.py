from flask import Blueprint, Flask
from flask_restx import Api

from starwars_api.rest_apis.starwars.views import movie, planet

bp = Blueprint("starwars", __name__, url_prefix="/api/starwars")
api = Api(bp)


def load_routes(app: Flask) -> None:
    """Load url routes for star wars rest api"""

    # movie endpoints
    api.add_resource(movie.MovieListCreateAPIResource, "/movie/")
    api.add_resource(movie.MovieDetailAPIResource, "/movie/<int:movie_pk>/")

    # planet endpoints
    api.add_resource(planet.PlanetListCreateAPIResource, "/planet/")
    api.add_resource(planet.PlanetDetailAPIResource, "/planet/<int:planet_pk>/")

    app.register_blueprint(bp)
