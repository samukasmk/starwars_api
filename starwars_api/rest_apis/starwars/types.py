from typing import TypeAlias

MoviePayload: TypeAlias = dict[str, str | int | list[int]]
PlanetPayload: TypeAlias = dict[str, str | int | list[int]]

MoviesPayload: TypeAlias = list[MoviePayload]
PlanetsPayload: TypeAlias = list[PlanetPayload]
