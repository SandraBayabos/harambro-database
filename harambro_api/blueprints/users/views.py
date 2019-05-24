from flask import Blueprint, jsonify
from flask_jwt import JWT, jwt_required
from models.user import User

users_api_blueprint = Blueprint('users_api',
                                __name__,
                                template_folder='templates')


@users_api_blueprint.route('/', methods=['GET'])
def index():
    return "USERS API"


@users_api_blueprint.route('/<email>', methods=['GET'])
@jwt_required
def show(email):
    user = User.get_or_none(User.email == email)

    if not user:
        resp = {
            'message': 'No user found with this email',
            'ok': False
        }
        # use jsonify to return a response in a JSON format
        return jsonify(resp)

    resp = {
        'message': 'Found user with this email',
        'user': {
            'id': user.id,
            'name': user.name,
            'email': user.email,

        },
        'ok': True
    }

    return jsonify(resp)

    @users_api_blueprint.route('/password', methods=['GET'])
    @jwt_required
    def verify_password(password):

        # something here blah blah blah

        # return jsonify(resp)

        pass
