from dynaconf import FlaskDynaconf
from flask import Flask


def load_settings_file(app: Flask, **extra_config) -> None:
    """
    Load Dynaconf settings (from settings.toml) merging with env variables (FLASK_*)
    """
    FlaskDynaconf(app, envvar_prefix="FLASK", **extra_config)
    # Initialize project extensions defined in settings.toml
    app.config.load_extensions("EXTENSIONS")  # NOQA[attr-defined]


def create_app(**extra_config) -> Flask:
    """
    Create Flask app object allowing config overwriting
    """
    app = Flask(__name__)
    load_settings_file(app, **extra_config)
    return app
