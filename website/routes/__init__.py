from .home import home_bp
from .set_language import lang_bp
from .auth import auth_bp

blueprints = [
  home_bp,
  lang_bp,
  auth_bp
]