
from peewee import *

from LehuForum.settings import database


class BaseModel(Model):
    add_time = DateTimeField(default=datetime.now, verbose_name='添加时间')

    class Meta:
        database = database
