"""
aggregations to display detailed information in db.planet.movies_details
"""

# TODO: Remove this enforcement of redefining `id` fields as string \
#       when solving wrong behavior in the specific serialization stages \
#       from CommandCursor objects of `.aggregation([pipeline])` to JSON format

movie_related_planets_details = [
    # normalize: id field as string value
    {"$set": {"id": {"$toString": "$_id"}}},
    {"$unset": "_id"},
    # join: detailed information about planet details to new field: movie.planets_details
    {
        "$lookup": {
            "from": "planet",
            "localField": "planets",
            "foreignField": "_id",
            "as": "planets_details",
            "pipeline": [
                # convert _id (objectId) to movie_id (string)
                {"$set": {"id": {"$toString": "$_id"}}},
                # remove _id (objectId) field
                {"$unset": "_id"},
            ],
        }
    },
]
