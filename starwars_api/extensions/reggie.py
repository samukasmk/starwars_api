from flask import Flask
from flask_reggie import Reggie

reggie = Reggie()


def init_app(app: Flask) -> None:  # NOQA
    """Enable regex validation in url routes"""
    reggie.init_app(app)
