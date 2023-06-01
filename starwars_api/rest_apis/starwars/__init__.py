from flask import Flask

from .routes import load_routes


def init_app(app: Flask) -> None:  # NOQA
    """Load starwars rest api"""
    load_routes(app)
