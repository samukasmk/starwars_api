from flask import Blueprint, Flask
from flask_restx import Namespace

from starwars_api.extensions.openapi import api

bp = Blueprint("starwars", __name__, url_prefix="/api/starwars")

from starwars_api.rest_apis.starwars.views import movie, planet


def load_routes(app: Flask) -> None:
    """Load url routes for star wars rest api"""

    # planet endpoints
    planet_namespace = Namespace("Planets", description="StarWars planets operations", path="/api/starwars")
    planet_namespace.add_resource(planet.PlanetListCreateAPIResource, "/planet/")
    planet_namespace.add_resource(planet.PlanetDetailAPIResource, "/planet/<int:planet_id>/")
    api.add_namespace(planet_namespace)

    # movie endpoints
    movie_namespace = Namespace("Movies", description="StarWars planets operations", path="/api/starwars")
    movie_namespace.add_resource(movie.MovieListCreateAPIResource, "/movie/")
    movie_namespace.add_resource(movie.MovieDetailAPIResource, "/movie/<int:movie_id>/")
    api.add_namespace(movie_namespace)

    # register blueprints
    app.register_blueprint(bp)
