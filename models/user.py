from models.base_model import BaseModel
from flask_login import LoginManager, UserMixin
import peewee as pw
import re
import jwt
import datetime
from app import app


class User(BaseModel, UserMixin):
    name = pw.CharField(null=False)
    email = pw.CharField(unique=True, null=False)
    password = pw.CharField(null=False)

    def validate(self):
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_email:
            self.errors.append('An account with that email already exists')

    def encode_auth_token(self, user_id):
        '''
        Generates the Auth Token
        :return: string
        '''
        try:
            payload = {
                'exp': datetime.datetime.utcnow() + datetime.timedelta(days=1, seconds=0),
                'iat': datetime.datetime.utcnow(),
                'sub': user_id
            }
            return jwt.encode(
                payload,
                app.config.get('SECRET_KEY'),
                algorithm='HS256'
            )
        except Exception as e:
            return e

    @staticmethod
    def decode_auth_token(auth_token):
        '''
        Decodes the the auth token
        :param auth_token:
        :return: integer/string
        '''
        try:
            payload = jwt.decode(auth_token, app.config.get('SECRET_KEY'))
            return payload['sub']
        except jwt. ExpiredSignatureError:
            return 0
        except jwt.InvalidTokenError:
            return 0
