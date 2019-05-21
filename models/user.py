from models.base_model import BaseModel
from flask_login import LoginManager, UserMixin
import peewee as pw
import re


class User(BaseModel, UserMixin):

    email = pw.CharField(unique=True, null=False)
    password = pw.CharField(null=False)

    def validate(self):
        duplicate_email = User.get_or_none(User.email == self.email)

        if duplicate_email:
            self.errors.append('An account with that email already exists')
