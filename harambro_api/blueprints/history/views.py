from flask import Blueprint, jsonify
from flask_jwt import JWT, jwt_required
from models.user import User
from models.history import History

history_api_blueprint = Blueprint('history_api',
                                  __name__,
                                  template_folder='templates')


@history_api_blueprint.route('/add_entry', methods=['POST'])
def add_history():
    auth_header = request.headers.get('Authorization')

    if auth_header:
        auth_token = auth_header.split(" ")[1]

    else:
        responseObject = {
            'status': 'failed',
            'message': 'No authorization header found'
        }

        return make_response(jsonify(responseObject)), 401

    user_id = User.decode_auth_token(auth_token)

    user = User.get_by_id(user_id)

    # sendgrid send email to user.email

    clicked_link = request.get_json('link')
    history = History(link=clicked_link, user_id=user.id)
    history.save()
