"""
aggregations from external relations of db.movie.planets to db.planet.movies
"""

# TODO: Remove this enforcement of redefining `id` fields as string \
#       when solving wrong behavior in the specific serialization stages \
#       from CommandCursor objects of `.aggregation([pipeline])` to JSON format

planet_related_movies_details = [
    # normalize: id field as string value
    {"$set": {"id": {"$toString": "$_id"}}},
    # join: detailed information about external relations of movies to new field: planet.movies_details
    {
        "$lookup": {
            "from": "movie",
            "localField": "_id",
            "foreignField": "planets",
            "as": "movies_details",
            "pipeline": [
                # remove related fields
                {"$unset": "planets"},
                # convert _id (objectId) to movie_id (string)
                {"$set": {"id": {"$toString": "$_id"}}},
                # remove _id (objectId) field
                {"$unset": "_id"},
            ],
        }
    },
    # merge: related movies_details._id in a single array field
    {"$set": {"movies": "$movies_details.id"}},
]

planet_related_movies = planet_related_movies_details + [
    # remove: detailed information of related movies_details
    {"$unset": "movies_details"}
]
