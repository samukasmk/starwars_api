from flask_restx import Model, fields

from starwars_api.extensions.openapi import api


def planet_fields(require_all_fields: bool = True) -> Model:
    """OpenAPI field definitions for Planet"""
    return api.model(  # type:ignore
        "Planet",
        {
            "name": fields.String(required=require_all_fields, default="Tatooine"),
            "rotation_period": fields.String(required=require_all_fields, default=23),
            "orbital_period": fields.Integer(required=require_all_fields, default=304),
            "diameter": fields.Integer(required=require_all_fields, default=10465),
            "climate": fields.String(required=require_all_fields, default="arid"),
            "gravity": fields.String(required=require_all_fields, default="1 standard"),
            "terrain": fields.String(required=require_all_fields, default="desert"),
            "surface_water": fields.Integer(required=require_all_fields, default=1),
            "population": fields.Integer(required=require_all_fields, default=200000),
            "movies": fields.List(fields.Integer(min=1), default=[1, 2, 3]),
        },
    )


planet_post_fields = planet_fields(require_all_fields=True)
planet_put_fields = planet_fields(require_all_fields=True)
planet_patch_fields = planet_fields(require_all_fields=False)
