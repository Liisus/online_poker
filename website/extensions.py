from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_babel import Babel
from flask import request, session

from .config import Config

import logging


db = SQLAlchemy()
socketio = SocketIO()
login_manager = LoginManager()

logging.basicConfig(
        format='[%(levelname)s] %(asctime)s\n: %(message)s'
    )
logger = logging.getLogger(__name__)

babel = Babel()

supported_languages = Config.LANGUAGES


from flask_login import current_user
def get_locale():
    if current_user.is_authenticated:
        language = current_user.preferred_locale
    else:
        try:
            language = session['language']
        except KeyError:
            language = None
    
    if language not in supported_languages:
        language = None
    if language is None:
        language = request.accept_languages.best_match(supported_languages)
        session['language'] = language
    logger.debug(f"Loaded Language {language} for user {current_user}")
    return language
