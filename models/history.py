from models.base_model import BaseModel
from models.user import User
from flask_login import LoginManager, UserMixin
# from playhouse.hybrid import hybrid_property
import peewee as pw


class History(BaseModel):
    user = pw.ForeignKeyField(User, backref='links')
    link = pw.CharField(null=True, default=None)
