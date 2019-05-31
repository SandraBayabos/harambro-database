from models.base_model import BaseModel
from models.user import User
from flask_login import LoginManager, UserMixin
# from playhouse.hybrid import hybrid_property
import peewee as pw
import datetime
import pytz
import time
from pytz import timezone


class History(BaseModel):
    user = pw.ForeignKeyField(User, backref='links')
    link = pw.CharField(null=True, default=None)

    @staticmethod
    def convert_time(created_at):
        return created_at.strftime('%d '' %B '' %Y '' %H:%M:%S')
        # return created_at.astimezone(pytz.utc).strftime('%d '' %B '' %Y '' %H:%M:%S')
        # return dt.astimezone(timezone(bk)).strftime('%Y-%m-%d %H:%M')
