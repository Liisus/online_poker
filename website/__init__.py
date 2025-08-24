from flask import Flask
from flask_socketio import SocketIO
import logging
from os import path

from .extensions import login_manager, db, socketio, babel, get_locale, logger

from .models import User


def create_app() -> tuple[Flask, SocketIO]:
    app = Flask(__name__, instance_relative_config=True)

    from .config import Config
    app.config.from_object(Config)

    logger.setLevel(logging.DEBUG)

    logger.debug(f"Secret key: {Config.SECRET_KEY}")

    # Initialize extensions
    db.init_app(app)

    socketio.init_app(app)

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return models.User.query.get(int(id))

    babel.init_app(app, locale_selector=get_locale)

    # register blueprints
    from .routes import blueprints
    for bp in blueprints:
        app.register_blueprint(bp)
    
    create_database(app)

    return app, socketio


def create_database(app):
    with app.app_context():
        db.create_all()
    logger.debug('Created database!')
