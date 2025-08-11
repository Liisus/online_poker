from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from flask import request, session

from .config import Config

db = SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()

babel = Babel()

supported_languages = Config.LANGUAGES


def get_locale():
    try:
        language = session['language']
    except KeyError:
        language = None
    if language not in supported_languages:
        language = None
    if language is None:
        language = request.accept_languages.best_match(supported_languages)
    print("Selected Language", language)
    return language
