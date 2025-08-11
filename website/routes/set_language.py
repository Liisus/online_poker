from flask import Blueprint, render_template, session, redirect
from flask_login import current_user

lang_bp = Blueprint('lang', __name__)

from ..extensions import supported_languages

@lang_bp.route('/language/<language>')
def set_language(language=None):
    if language in supported_languages:
        session['language'] = language
    return redirect("/")