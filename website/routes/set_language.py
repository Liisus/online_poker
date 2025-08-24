from flask import Blueprint, render_template, session, redirect
from flask_login import current_user
from ..extensions import db

lang_bp = Blueprint('lang', __name__)

from ..extensions import supported_languages

@lang_bp.route('/language/<language>')
def set_language(language=None):
    if language in supported_languages:
        session['language'] = language
        if current_user.is_authenticated:
            current_user.preferred_locale = language;
            db.session.commit()
    return redirect("/")