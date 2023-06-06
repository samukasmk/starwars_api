def sample_movies_api_requests(planets_objects_ids):
    """Sample data of starwars movies with fake associations"""
    return [
        {
            "title": "The Phantom Menace",
            "opening_crawl": (
                "Turmoil has engulfed the\r\nGalactic Republic. The taxation\r\nof trade routes to outlying star\r\n"
                "systems is in dispute.\r\n\r\nHoping to resolve the matter\r\nwith a blockade of deadly\r\n"
                "battleships, the greedy Trade\r\nFederation has stopped all\r\nshipping to the small planet\r\n"
                "of Naboo.\r\n\r\nWhile the Congress of the\r\nRepublic endlessly debates\r\n"
                "this alarming chain of events,\r\nthe Supreme Chancellor has\r\nsecretly dispatched two Jedi\r\n"
                "Knights, the guardians of\r\npeace and justice in the\r\ngalaxy, to settle the conflict...."
            ),
            "episode_id": 1,
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "1999-05-19",
            "planets": planets_objects_ids[0],
        },
        {
            "title": "Attack of the Clones",
            "opening_crawl": (
                "There is unrest in the Galactic\r\nSenate. Several thousand solar\r\nsystems have declared their\r\n"
                "intentions to leave the Republic.\r\n\r\nThis separatist movement,\r\nunder the leadership of the\r\n"
                "mysterious Count Dooku, has\r\nmade it difficult for the limited\r\n"
                "number of Jedi Knights to maintain \r\npeace and order in the galaxy.\r\n\r\n"
                "Senator Amidala, the former\r\nQueen of Naboo, is returning\r\nto the Galactic Senate to vote\r\n"
                "on the critical issue of creating\r\nan ARMY OF THE REPUBLIC\r\nto assist the overwhelmed\r\nJedi...."
            ),
            "episode_id": 2,
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2002-05-16",
            "planets": planets_objects_ids[1],
        },
        {
            "title": "Revenge of the Sith",
            "opening_crawl": (
                "War! The Republic is crumbling\r\nunder attacks by the ruthless\r\nSith Lord, Count Dooku.\r\n"
                "There are heroes on both sides.\r\nEvil is everywhere.\r\n\r\nIn a stunning move, the\r\n"
                "fiendish droid leader, General\r\nGrievous, has swept into the\r\nRepublic capital and kidnapped\r\n"
                "Chancellor Palpatine, leader of\r\nthe Galactic Senate.\r\n\r\nAs the Separatist Droid Army\r\n"
                "attempts to flee the besieged\r\ncapital with their valuable\r\nhostage, two Jedi Knights lead a\r\n"
                "desperate mission to rescue the\r\ncaptive Chancellor...."
            ),
            "episode_id": 3,
            "director": "George Lucas",
            "producer": "Rick McCallum",
            "release_date": "2005-05-19",
            "planets": planets_objects_ids[2],
        },
        {
            "title": "A New Hope",
            "opening_crawl": (
                "It is a period of civil war.\r\nRebel spaceships, striking\r\nfrom a hidden base, have won\r\n"
                "their first victory against\r\nthe evil Galactic Empire.\r\n\r\nDuring the battle, Rebel\r\n"
                "spies managed to steal secret\r\nplans to the Empire's\r\nultimate weapon, the DEATH\r\n"
                "STAR, an armored space\r\nstation with enough power\r\nto destroy an entire planet.\r\n\r\n"
                "Pursued by the Empire's\r\nsinister agents, Princess\r\nLeia races home aboard her\r\n"
                "starship, custodian of the\r\nstolen plans that can save her\r\npeople and restore\r\n"
                "freedom to the galaxy...."
            ),
            "episode_id": 4,
            "director": "George Lucas",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1977-05-25",
            "planets": planets_objects_ids[3],
        },
        {
            "title": "The Empire Strikes Back",
            "opening_crawl": (
                "It is a dark time for the\r\nRebellion. Although the Death\r\nStar has been destroyed,\r\n"
                "Imperial troops have driven the\r\nRebel forces from their hidden\r\nbase and pursued them across\r\n"
                "the galaxy.\r\n\r\nEvading the dreaded Imperial\r\nStarfleet, a group of freedom\r\n"
                "fighters led by Luke Skywalker\r\nhas established a new secret\r\nbase on the remote ice world\r\n"
                "of Hoth.\r\n\r\nThe evil lord Darth Vader,\r\nobsessed with finding young\r\n"
                "Skywalker, has dispatched\r\nthousands of remote probes into\r\nthe far reaches of space...."
            ),
            "episode_id": 5,
            "director": "Irvin Kershner",
            "producer": "Gary Kurtz, Rick McCallum",
            "release_date": "1980-05-17",
            "planets": planets_objects_ids[4],
        },
        {
            "title": "Return of the Jedi",
            "opening_crawl": (
                "Luke Skywalker has returned to\r\nhis home planet of Tatooine in\r\nan attempt to rescue his\r\n"
                "friend Han Solo from the\r\nclutches of the vile gangster\r\nJabba the Hutt.\r\n\r\n"
                "Little does Luke know that the\r\nGALACTIC EMPIRE has secretly\r\nbegun construction on a new\r\n"
                "armored space station even\r\nmore powerful than the first\r\ndreaded Death Star.\r\n\r\n"
                "When completed, this ultimate\r\nweapon will spell certain doom\r\nfor the small band of rebels\r\n"
                "struggling to restore freedom\r\nto the galaxy..."
            ),
            "episode_id": 6,
            "director": "Richard Marquand",
            "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum",
            "release_date": "1983-05-25",
            "planets": planets_objects_ids[5],
        },
    ]
