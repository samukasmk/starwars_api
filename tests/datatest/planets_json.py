def sample_planets():
    """Sample data of starwars planets with fake associations"""
    return [
        {
            "id": 1,
            "name": "Tatooine",
            "rotation_period": "23",
            "orbital_period": "304",
            "diameter": "10465",
            "climate": "arid",
            "gravity": "1 standard",
            "terrain": "desert",
            "surface_water": "1",
            "population": "200000",
            "movies": [6],  # fake associations, just for test
            "created": "2014-12-09T13:50:49.641000Z",
            "edited": "2014-12-20T20:58:18.411000Z",
        },
        {
            "id": 2,
            "name": "Alderaan",
            "rotation_period": "24",
            "orbital_period": "364",
            "diameter": "12500",
            "climate": "temperate",
            "gravity": "1 standard",
            "terrain": "grasslands, mountains",
            "surface_water": "40",
            "population": "2000000000",
            "movies": [  # fake associations, just for test
                5,
                6,
            ],
            "created": "2014-12-10T11:35:48.479000Z",
            "edited": "2014-12-20T20:58:18.420000Z",
        },
        {
            "id": 3,
            "name": "Yavin IV",
            "rotation_period": "24",
            "orbital_period": "4818",
            "diameter": "10200",
            "climate": "temperate, tropical",
            "gravity": "1 standard",
            "terrain": "jungle, rainforests",
            "surface_water": "8",
            "population": "1000",
            "movies": [  # fake associations, just for test
                4,
                5,
                6,
            ],
            "created": "2014-12-10T11:37:19.144000Z",
            "edited": "2014-12-20T20:58:18.421000Z",
        },
        {
            "id": 4,
            "name": "Hoth",
            "rotation_period": "23",
            "orbital_period": "549",
            "diameter": "7200",
            "climate": "frozen",
            "gravity": "1.1 standard",
            "terrain": "tundra, ice caves, mountain ranges",
            "surface_water": "100",
            "population": "unknown",
            "movies": [  # fake associations, just for test
                3,
                4,
                5,
                6,
            ],
            "created": "2014-12-10T11:39:13.934000Z",
            "edited": "2014-12-20T20:58:18.423000Z",
        },
        {
            "id": 5,
            "name": "Dagobah",
            "rotation_period": "23",
            "orbital_period": "341",
            "diameter": "8900",
            "climate": "murky",
            "gravity": "N/A",
            "terrain": "swamp, jungles",
            "surface_water": "8",
            "population": "unknown",
            "movies": [  # fake associations, just for test
                2,
                3,
                4,
                5,
                6,
            ],
            "created": "2014-12-10T11:42:22.590000Z",
            "edited": "2014-12-20T20:58:18.425000Z",
        },
        {
            "id": 6,
            "name": "Bespin",
            "rotation_period": "12",
            "orbital_period": "5110",
            "diameter": "118000",
            "climate": "temperate",
            "gravity": "1.5 (surface), 1 standard (Cloud City)",
            "terrain": "gas giant",
            "surface_water": "0",
            "population": "6000000",
            "movies": [  # fake associations, just for test
                1,
                2,
                3,
                4,
                5,
                6,
            ],
            "created": "2014-12-10T11:43:55.240000Z",
            "edited": "2014-12-20T20:58:18.427000Z",
        },
    ]
