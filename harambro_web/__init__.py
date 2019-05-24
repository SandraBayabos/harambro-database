from app import app
from flask import Flask, render_template
from flask_login import LoginManager
from models.user import User
from harambro_web.blueprints.users.views import users_blueprint
from harambro_web.blueprints.sessions.views import sessions_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles
from harambro_web.util.google_oauth import oauth

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")
app.register_blueprint(sessions_blueprint, url_prefix="/sessions")

#FLASK LOGIN FUNCTION#
login_manager = LoginManager()
login_manager.init_app(app)

# GOOGLE OAUTH
oauth.init_app(app)

#user_loader used to reload the user object from the user ID stored in the session#

# change back to get_by_id after done with flask login
@login_manager.user_loader
def load_user(user_id):
    return User.get_or_none(id=user_id)

# error handlers


@app.route('/')
def home():
    return render_template('home.html')


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
