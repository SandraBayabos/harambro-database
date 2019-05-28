from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from flask_login import current_user, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from models.user import User
from flask_bootstrap import Bootstrap

users_blueprint = Blueprint('users',
                            __name__,
                            template_folder='templates/users')


@users_blueprint.route('/new', methods=['GET'])
def new():
    return render_template('new.html')


@users_blueprint.route('/', methods=['POST'])
def create():
    name = request.form.get('name')
    email = request.form.get('email')
    password = request.form.get('password')
    hashed_password = generate_password_hash(password)

    newuser = User(
        name=name,
        email=email,
        password=hashed_password
    )

    if newuser.save():
        flash('Welcome to Harambro.')
        return redirect(url_for('home'))

    else:
        flash(f'{user_email} is already taken. Please try again.')
        return render_template('new.html', errors=newuser.errors)


# @login_required
# @users_blueprint.route('/show/<name>', methods=['GET'])
# def show(name):
#     user = User.get_or_none(User.name == name)

#     if current_user == user:
#         return render_template('show.html', name=current_user.name)

@users_blueprint.route('/<id>/edit', methods=["GET"])
def edit(id):
    user = User.get_by_id(id)
    if current_user == user:
        return render_template('edit.html', user=user)
    else:
        flash('You cannot do this action.')
        return redirect(url_for('home'))


@users_blueprint.route('/<id>', methods=["POST"])
def update(id):
    user = User.get_by_id(id)

    if not current_user == user:
        flash('Unauthorised')
        return render_template('edit.html', user=user)

    else:
        new_name = request.form.get('new_name')
        new_email = request.form.get('new_email')
        new_password = request.form.get('new_password')
        hashed_password = generate_password_hash(new_password)

        update_user = User.update(
            name=new_name,
            email=new_email,
            password=hashed_password
        ).where(User.id == id)

        if not update_user.execute():
            flash(f"Unable to update, please try again")
            return render_template('edit.html', user=user)

        flash('Successfully updated')
        return redirect(url_for('home'))
