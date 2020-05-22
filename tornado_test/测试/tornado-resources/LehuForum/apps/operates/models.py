from peewee import *

from LehuForum.models import BaseModel
from apps.users.models import User

MESSAGE_TYPE = ((1, '评论'), (2, '回答'), (3, '点赞'))


class Message(BaseModel):
    sender = ForeignKeyField(User, verbose_name='发送者')
    # reciever = ForeignKeyField(User, verbose_name='接受者')
    msg_type = IntegerField(choices=MESSAGE_TYPE, verbose_name='消息类型')
    message = CharField(max_length=500, null=True, verbose_name='消息内容')
    parent = CharField(max_length=500, null=True, verbose_name='标题')
