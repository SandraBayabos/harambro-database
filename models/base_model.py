import os
import peewee as pw
import datetime
from database import db
from datetime import timedelta


class BaseModel(pw.Model):
    created_at = pw.DateTimeField(
        default=datetime.datetime.now + timedelta(hours=8))
    updated_at = pw.DateTimeField(
        default=datetime.datetime.now + timedelta(hours=8))

    def save(self, *args, **kwargs):
        self.errors = []
        self.validate()

        if len(self.errors) == 0:
            self.updated_at = datetime.datetime.now() + timedelta(hours=8)
            return super(BaseModel, self).save(*args, **kwargs)
        else:
            return 0

    def validate(self):
        print(
            f"Warning validation method not implemented for {str(type(self))}")
        return True

    class Meta:
        database = db
        legacy_table_names = False
