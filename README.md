# starwars_api

[./README-pt-br.md](**README: in Portuguese**)

This is an example of use case project for technologies: (**Flask Framework**) with databases **no-sql** (**MongoDB**) oriented to *documents*.

This project implements some simple resources for data management of the StarWars saga movies. And it was inspired by the API: [https://swapi.dev/](https://swapi.dev/).

Unlike [https://swapi.dev/](https://swapi.dev/) which was built in **Django**, this project aims to implement more comprehensive architecture concepts and best practices, structuring the **Framework Flask** for a large project, in the sense of opening up more than one scope of data, not just being restricted to `starwars_api`.


# installing

The most recommended installation is through [Docker](https://docs.docker.com/engine/install/) and [docker-compose](https://docs.docker.com/compose/install/) if you don't have it installed on your machine, arrange the installation through the previous links.

## Installing with docker-compose

Just run the following commands below:

```sh
git clone https://github.com/samukasmk/starwars_api.git

cd starwars_api

docker-compose up --build

http://127.0.0.1:5000
command: make test
```

## Example of running the application with docker-compose
![.docs/assets/docker-install.gif](.docs/assets/docker-install.gif)


# Using the Rest API

After the previous steps have been successfully performed and running, connect to your computer's url: [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

![.docs/assets/api-swagger-listing.png]()

Currently this API implements 2 endpoints:

## planets

Endpoint that manages the basic data of the planets that appear in the Star Wars movies, such as population, diameter, gravity, orbit period, rotation period.

### Applied methods:

**Method** | **Endpoint** | **Description**
------------|------------------------------------- ------|----------------------------------------------------- ------------------------------------------------
**POST** | /api/starwars/planet/ | Create a planet resource
**GET** | /api/starwars/planet/ | List all planets resources
**GET** | /api/starwars/planet/?movies_details=true | List all planets resources (with relate movie informations on field **”movies_details"**)
**GET** | /api/starwars/planet/{planet_id}/ | Retrieve a planet resource
**PUT** | /api/starwars/planet/{planet_id}/ | Update a planet resource
**PATCH** | /api/starwars/planet/{planet_id}/ | Partial update a planet resource
**DELETE** | /api/starwars/planet/{planet_id}/ | Delete a planet resource

### Changeable fields:
- **name** `<StringField>`
- **rotation_period** `<IntField>`
- **orbital_period** `<IntField>`
- **diameter** `<IntField>`
- **climate** `<StringField>`
- **gravity** `<StringField>`
- **terrain** `<StringField>`
- **surface_water** `<IntField>`
- **population** `<StringField>`

### Read-only fields:
- **id** `<objectId>`: Ensures document specification and grants n-to-n external relationship to **Movies**
- **movies** `<array>`: Displays the relation between the planets and the movies as read only, writing must be done by the **Movies** endpoint preventing errors in data management;
- **movies_details** `<object>`: Displays a more detailed version of the relationship with **Movies** resources, to be displayed it needs the parameter: **?movies_details=true**
- **created_at** `<datetime>`: Document creation management;
- **updated_at** `<datetime>`: Document editing management;

Usage examples:

#### Creating a planet
![.docs/assets/swagger-create-planets.png](.docs/assets/swagger-create-planets.png)

#### Listing created planets
![.docs/assets/swagger-planets-listing.png](.docs/assets/swagger-planets-listing.png)

#### Detailed listing of related movies
![.docs/assets/swagger-planets-listing-detailed.png](.docs/assets/swagger-planets-listing-detailed.png)

#### Partial update of planet specific fields
![.docs/assets/swagger-partial-update-plantets.png](.docs/assets/swagger-partial-update-plantets.png)

#### Updating a planet's fields
![.docs/assets/swagger-update-plantets.png](.docs/assets/swagger-update-plantets.png)

## Movies

Endpoint that manages the basic data of `movies` with their respective appearances in each movie.

### Applied methods:
  **Method** | **Endpoint** | **Description**
------------|------------------------------------- ----------|---------------------------------
  **GET** | /api/starwars/movie/ | List all movies resources
  **GET** | /api/starwars/movie/**?planets_details=true** | List all movies resources
  **POST** | /api/starwars/movie/ | Create a movie resource
  **PUT** | /api/starwars/movie/{movie_id}/ | Update a movie resource
  **PATCH** | /api/starwars/movie/{movie_id}/ | Partial update a movie resource
  **GET** | /api/starwars/movie/{movie_id}/ | Retrieve a movie resource
  **DELETE** | /api/starwars/movie/{movie_id}/ | Delete a movie resource

### Changeable fields:
- **title**: `<StringField>`
- **opening_crawl**: `<StringField>`
- **episode_id**: `<IntField>`
- **director**: `<StringField>`
- **producer**: `<StringField>`
- **release_date**: `<DateField>`
- **planets** `<array>`: Displays the relationship between the planets and the movies, the writing must be done by the **Movies** endpoint preventing errors in data management;

### Read-only fields:
- **id** `<objectId>`: Ensures document specification and grants n-to-n external relationship to **Planets**
- **planets_details** `<object>`: Displays a more detailed version of the relationship with **Planets** resources, to be displayed it needs the parameter: **?planets_details=true**
- **created_at** `<datetime>`: Document creation management;
- **updated_at** `<datetime>`: Document editing management;


Usage examples:

#### Creating a Movie already associating it with 2 planets
![.docs/assets/swagger-creating-movies.png](.docs/assets/swagger-creating-movies.png)

#### Detailed listing of related Planets
![.docs/assets/swagger-movie-retrive-detailed.png](.docs/assets/swagger-movie-retrive-detailed.png)

#### And so on...
Visit swagger and find out for yourself



# Architecture and folder structure of the project:

```
├── docker-compose.yml: Services definition file
├── Dockerfile: Container definition file
├── Makefile: Script with repetitive operational commands
├── manage.py: Project execution script
├── pyproject.toml: File with Development settings
├── requirements-dev.txt: Dynamic development dependencies (generated by Poetry)
├── requirements.txt: Dynamic production dependencies (generated by Poetry)
├── scripts:
│ └── git-hooks: Scripts and automations with git
├── settings.toml: **File with the application's production settings**
├── starwars_api: **Application Folder**
│ ├── extensions: Flask initializers that run .init_app(app)
│ ├── models: Define data structures
│ └── rest_apis:
│ └── Star Wars:
│ ├── endpoints: Views and controllers from the rest api
│ ├── queries: Aggregation queries with mongodb
│ ├── routes.py: URL routes from endpoints
│ ├── serializers: JSON input serialization -> MongoDB Document and vice versa
│ └── validators: Defines input field validations the Rest API and swagger must have
└── tests:
     ├── datasets: Test case data
     └── fixtures: Unit Test Fixtures
```

# Development

## Running unit tests locally
```
make test
```

### Formatting python files and imports
``` shell
make fmt
```

### Updated requirements files with poetry:
1.) Add new dependencies in the **pyproject.toml** file

2.) Run poetry through the make command:
```
make build-requirements
```

### Running security checks
```
make sec-check
```