from flask import Flask
from flask_restx import Api

api = None  # NOQA


def init_app(app: Flask) -> None:  # NOQA
    global api  # NOQA
    api = Api(
        app,
        version=app.config['SWAGGER_API_VERSION'],
        title=app.config['SWAGGER_API_TITLE'],
        description=app.config['SWAGGER_API_DESCRIPTION'],
        license=app.config['SWAGGER_API_LICENSE'],
        license_url=app.config['SWAGGER_API_LICENSE_URL'],
        contact=app.config['SWAGGER_API_CONTACT'],
        contact_url=app.config['SWAGGER_API_CONTACT_URL'],
        contact_email=app.config['SWAGGER_API_CONTACT_EMAIL'],
    )
