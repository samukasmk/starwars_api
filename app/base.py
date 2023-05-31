from dynaconf import FlaskDynaconf
from flask import Flask


def load_settings_file(app, **extra_config):
    # load Dynaconf settings (from settings.toml) merging with env variables (FLASK_*)
    FlaskDynaconf(app, envvar_prefix="FLASK")

    # Initialize project extensions defined in settings.toml
    app.config.load_extensions("EXTENSIONS")

    # Overwrite Dynaconf settings from extra config on app creation
    app.config.update(extra_config)


def create_app(**extra_config) -> Flask:
    app = Flask(__name__)

    load_settings_file(app, **extra_config)
    return app
