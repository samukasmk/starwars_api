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
def planet_fields(require_all_fields: bool = True) -> Model:
    """OpenAPI field schemas for Planet"""
    return api.model(  # type:ignore
        "Planet",
        {
            "name": fields.String(required=require_all_fields, default="Tatooine"),
            "rotation_period": fields.Integer(required=require_all_fields, default=23),
            "orbital_period": fields.Integer(required=require_all_fields, default=304),
            "diameter": fields.Integer(required=require_all_fields, default=10465),
            "climate": fields.String(required=require_all_fields, default="arid"),
            "gravity": fields.String(required=require_all_fields, default="1 standard"),
            "terrain": fields.String(required=require_all_fields, default="desert"),
            "surface_water": fields.Integer(required=require_all_fields, default=1),
            "population": fields.Integer(required=require_all_fields, default=200000),
        },
    )


# REST API query string validators
planet_parameters = reqparse.RequestParser()
planet_parameters.add_argument(
    "movies_details",
    choices=("true", "false"),
    default="",
    help="Shows detailed information about related movies in field (movies_details).",
)


class PlanetAPIValidator:
    # payload validators
    creating_payload = planet_fields(require_all_fields=True)
    updating_payload = planet_fields(require_all_fields=True)
    partial_updating_payload = planet_fields(require_all_fields=False)

    # querystring validators
    displaying_parameters = planet_parameters
