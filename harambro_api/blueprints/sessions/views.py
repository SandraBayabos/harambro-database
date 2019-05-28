from flask import Blueprint, jsonify, request, make_response
from flask_jwt import JWT, jwt_required
from models.user import User
from models.history import History
from werkzeug.security import generate_password_hash, check_password_hash

sessions_api_blueprint = Blueprint('sessions_api',
                                   __name__,
                                   template_folder='templates')


@sessions_api_blueprint.route('/login', methods=['POST'])
def sign_in():
    # get the post data
    post_data = request.get_json()
    # check if user already exists
    user = User.get_or_none(email=post_data.get('email'))
    if user and check_password_hash(user.password, post_data.get('password')):
        auth_token = user.encode_auth_token(user.id)
        responseObject = {
            'status': 'success',
            'message': 'Successfully signed in.',
            'auth_token': auth_token.decode(),
            # 'user': user.__dict__
            'email': user.email,
            'user_id': user.id
        }
        print(responseObject)
        return make_response(jsonify(responseObject)), 201

    else:
        responseObject = {
            'status': 'fail',
            'message': 'Some error occurred. Please try again'
        }

        return make_response(jsonify(responseObject)), 401
