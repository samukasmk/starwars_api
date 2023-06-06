import click
from flask.cli import FlaskGroup

from starwars_api.base import create_app


@click.group(cls=FlaskGroup, create_app=create_app)
def main():
    """Management script for the starwars_api application."""


if __name__ == "__main__":  # pragma: no cover
    main()
