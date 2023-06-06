import mongoengine
from flask import Flask


def init_app(app: Flask) -> None:  # NOQA
    """Connect in mongodb by MONGODB_HOST flask settings"""
    mongoengine.connect(host=app.config["MONGODB_HOST"])
