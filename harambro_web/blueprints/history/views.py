from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from models.history import History
from flask_bootstrap import Bootstrap


history_blueprint = Blueprint('history',
                              __name__,
                              template_folder='templates/history')


@login_required
@history_blueprint.route('/show/<name>', methods=['GET'])
def show(name):
    user = User.get_or_none(User.name == name)

    if current_user == user:
        return render_template('show.html', name=current_user.name)
