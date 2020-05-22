from apps.communities.models import CommunityGroup, CommunityGroupMember, Post, PostComment, CommentLike
from apps.questions.models import Answer, Question
from apps.users.models import User
from apps.operates.models import Message
from LehuForum.settings import database, settings

from peewee import MySQLDatabase

database = MySQLDatabase(
    settings['db']['name'], host=settings['db']['host'], port=settings['db']['port'], user=settings['db']['user'],
    password=settings['db']['password']
)


def init():
    # 生成表
    database.create_tables([User])
    database.create_tables([CommunityGroup, CommunityGroupMember, Post, PostComment, CommentLike])
    database.create_tables([Question, Answer])
    database.create_tables([Message])


if __name__ == "__main__":
    init()
