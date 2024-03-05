from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from config import Config

db = SQLAlchemy()
migrate = Migrate()


def create_app(config_class=Config):
    """
    Create a Flask app using the provided configuration class.
    Using Factory pattern to create the app.
    """

    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    register_blueprints(app)

    return app


def register_blueprints(app):
    from app.views.items import search_bp

    app.register_blueprint(search_bp)
