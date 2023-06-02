from flask_restx import Model, fields

from starwars_api.extensions.openapi import api


def movie_fields(require_all_fields: bool = True) -> Model:
    """OpenAPI field definitions for Movie"""
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
            "planets": fields.List(fields.Integer(min=1), default=[1, 2, 3]),
        },
    )


movie_post_fields = movie_fields(require_all_fields=True)
movie_put_fields = movie_fields(require_all_fields=True)
movie_patch_fields = movie_fields(require_all_fields=False)
