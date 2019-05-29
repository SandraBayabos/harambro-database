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


@sessions_api_blueprint.route('/checkpassword', methods=['POST'])
def check_password():
    post_data = request.get_json()
    auth_header = request.headers.get('Authorization')

    # check if user already exists
    if auth_header:
        auth_token = auth_header.split(" ")[1]

    # decode the auth_token here
    user_id = User.decode_auth_token(auth_token)

    current_user = User.get_by_id(user_id)

    if current_user:
        if check_password_hash(current_user.password, post_data.get('password')):
            responseObject = {
                'status': 'success',
                'message': 'Password successfully authenticated'
            }
            print(responseObject)
            return make_response(jsonify(responseObject)), 201

        else:
            responseObject = {
                'status': 'fail',
                'message': 'Password incorrect. Please try again'
            }

            return make_response(jsonify(responseObject)), 201
    else:
        responseObject = {
            'status': 'fail',
            'message': 'Failed at user_id level.'
        }

        return make_response(jsonify(responseObject)), 201
