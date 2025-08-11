import os


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')
    BABEL_TRANSLATION_DIRECTORIES = os.environ.get(
        'BABEL_TRANSLATION_DIRECTORIES')
    LANGUAGES = {
        'en': 'English',
        'ru': 'Russian'
    }
