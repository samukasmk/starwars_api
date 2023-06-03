"""
Provides (API schema definitions) for validating input data into API methods like
(POST, PUT, and PATCH) and automatically building API documentation with Swagger.

Please do not confuse (api.model) fields with:
- (marshmallow schemas): for serialization and deserialization of json format
- (mongoengine models): management interface for pymongo documents as pythonic objects
"""

from flask_restx import Model, fields

from starwars_api.extensions.openapi import api


def planet_fields(all_fields_is_required: bool = True) -> Model:
    """OpenAPI field schemas for Planet"""
    return api.model(  # type:ignore
        "Planet",
        {
            "name": fields.String(required=all_fields_is_required, default="Tatooine"),
            "rotation_period": fields.Integer(required=all_fields_is_required, default=23),
            "orbital_period": fields.Integer(required=all_fields_is_required, default=304),
            "diameter": fields.Integer(required=all_fields_is_required, default=10465),
            "climate": fields.String(required=all_fields_is_required, default="arid"),
            "gravity": fields.String(required=all_fields_is_required, default="1 standard"),
            "terrain": fields.String(required=all_fields_is_required, default="desert"),
            "surface_water": fields.Integer(required=all_fields_is_required, default=1),
            "population": fields.Integer(required=all_fields_is_required, default=200000),
        },
    )


# build field requirements to assign in @api.expect(...) decorators
class PlanetAPIFields:
    post = planet_fields(all_fields_is_required=True)
    put = planet_fields(all_fields_is_required=True)
    patch = planet_fields(all_fields_is_required=False)
