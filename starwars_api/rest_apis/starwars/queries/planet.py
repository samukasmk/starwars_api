# aggregate db.planet.movies from db.movie.planets (array)
planet_movies_aggregation = [
    {
        "$lookup": {
            "from": "movie",
            "localField": "_id",
            "foreignField": "planets",
            "as": "movies_details",
            "pipeline": [{"$unset": "planets"}, {"$set": {"movie_id": {"$toString": "$_id"}}}, {"$unset": "_id"}],
        }
    },
    {"$set": {"movies": "$movies_details.movie_id"}},
    {"$unset": "movies_details"},
    # TODO: Remove this enforcement of redefining `id` field as string \
    #       when solving wrong behavior in the serialization stage of \
    #       ignoring `_id` field for special cases of serialization \
    #       from CommandCursor objects of `.aggregation([pipeline])` to JSON format
    {"$set": {"id": {"$toString": "$_id"}}},
]
