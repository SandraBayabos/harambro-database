from app import app
from flask import Flask, render_template
from flask_login import LoginManager
from models.user import User
from harambro_web.blueprints.users.views import users_blueprint
from flask_assets import Environment, Bundle
from .util.assets import bundles

assets = Environment(app)
assets.register(bundles)

app.register_blueprint(users_blueprint, url_prefix="/users")

#FLASK LOGIN FUNCTION#
login_manager = LoginManager()
login_manager.init_app(app)

#user_loader used to reload the user object from the user ID stored in the session#


@login_manager.user_loader
def load_user(user_id):
    return User.get_by_id(user_id)

# error handlers


@app.errorhandler(500)
def internal_server_error(e):
    return render_template('500.html'), 500


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404


@app.route("/")
def home():
    return render_template('home.html')
