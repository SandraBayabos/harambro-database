from flask import Blueprint, jsonify, make_response, request
from flask_jwt import JWT, jwt_required
from models.user import User
from models.history import History
from harambro_api.util.sendgrid import send_email
from datetime import datetime

history_api_blueprint = Blueprint('history_api',
                                  __name__,
                                  template_folder='templates')


@history_api_blueprint.route('/add_entry', methods=['POST'])
def add_history():
    clicked_link = request.get_json()
    auth_header = request.headers.get('Authorization')

    if not auth_header:
        responseObject = {
            'status': 'failed',
            'message': 'No JWT in Authorization Header'
        }
        return make_response(jsonify(responseObject)), 401

    # decode the auth_token to get the user_id
    auth_token = auth_header.split(" ")[1]
    user_id = User.decode_auth_token(auth_token)

    current_user = User.get_by_id(user_id)

    # save link that has been clicked on
    if current_user and clicked_link:
        email = current_user.email
        name = current_user.name
        # sendgrid send email to user.email
        send_email(email)
        history = History(
            link=clicked_link['link'],
            user_id=current_user.id)
        if history.save():
            responseObject = {
                'status': 'success'
            }
            return make_response(jsonify(responseObject)), 201

        else:
            responseObject = {
                'status': 'failed',
                'message': 'History not saved'
            }
            return make_response(jsonify(responseObject)), 401

    else:
        responseObject = {
            'status': 'failed',
            'message': 'No authorization header found'
        }

        return make_response(jsonify(responseObject)), 401
