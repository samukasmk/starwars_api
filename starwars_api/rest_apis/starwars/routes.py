from flask import Blueprint, Flask
from flask_restful import Api, Resource

from starwars_api.rest_apis.starwars.views import movie_endpoints, planet_endpoints

bp = Blueprint("starwars", __name__, url_prefix="/api/starwars")
api = Api(bp)


def load_routes(app: Flask) -> None:
    """Load starwars url routes"""
    api.add_resource(movie_endpoints.MovieResource, "/movie/<int:movie_pk>")
    api.add_resource(planet_endpoints.PlanetResource, "/planet/<int:planet_pk>")

    app.register_blueprint(bp)
