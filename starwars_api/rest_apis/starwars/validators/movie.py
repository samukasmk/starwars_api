"""
Provides (API schema definitions) for validating input data into API methods like
(POST, PUT, and PATCH) and automatically building API documentation with Swagger.

Please do not confuse (api.model) fields with:
- (marshmallow schemas): for serialization and deserialization of json format
- (mongoengine models): management interface for pymongo documents as pythonic objects
"""

from flask_restx import Model, fields, reqparse

from starwars_api.extensions.openapi import api


# REST API Input payload validators
def movie_fields(require_all_fields: bool = True) -> Model:
    """OpenAPI field schemas for Movie"""
    return api.model(  # type:ignore
        "Movie",
        {
            "title": fields.String(required=require_all_fields, default="The Phantom Menace"),
            "opening_crawl": fields.String(
                required=require_all_fields,
                default=(
                    "Turmoil has engulfed the\r\nGalactic Republic. The taxation\r\n"
                    "of trade routes to outlying star\r\nsystems is in dispute.\r\n\r\nHoping to resolve the matter\r\n"
                    "with a blockade of deadly\r\nbattleships, the greedy Trade\r\nFederation has stopped all\r\n"
                    "shipping to the small planet\r\nof Naboo.\r\n\r\nWhile the Congress of the\r\n"
                    "Republic endlessly debates\r\nthis alarming chain of events,\r\nthe Supreme Chancellor has\r\n"
                    "secretly dispatched two Jedi\r\nKnights, the guardians of\r\npeace and justice in the\r\n"
                    "galaxy, to settle the conflict...."
                ),
            ),
            "episode_id": fields.Integer(required=require_all_fields, default=1),
            "director": fields.String(required=require_all_fields, default="George Lucas"),
            "producer": fields.String(required=require_all_fields, default="Rick McCallum"),
            "release_date": fields.Date(required=require_all_fields, default="1999-05-19"),
            "planets": fields.List(
                fields.String(),
                required=False,
                example=["PlanetIdFKRefToMovie0001", "PlanetIdFKRefToMovie0002", "PlanetIdFKRefToMovie0003"],
            ),
        },
    )


# REST API query string validators
movie_parameters = reqparse.RequestParser()
movie_parameters.add_argument(
    "planets_details",
    choices=("true", "false"),
    default="",
    help="Shows detailed information about related planets in field (planets_details).",
)


class MovieAPIValidator:
    # payload validators
    creating_payload = movie_fields(require_all_fields=True)
    updating_payload = movie_fields(require_all_fields=True)
    partial_updating_payload = movie_fields(require_all_fields=False)

    # querystring validators
    displaying_parameters = movie_parameters
