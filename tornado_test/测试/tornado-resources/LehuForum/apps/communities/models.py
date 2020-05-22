from datetime import datetime

from peewee import *

from LehuForum.models import BaseModel
from apps.users.models import User


class CommunityGroup(BaseModel):
    creator = ForeignKeyField(User, verbose_name="创建者")
    name = CharField(max_length=100, null=True, verbose_name="名称")
    category = CharField(max_length=20, verbose_name="分类", null=True)
    cover = CharField(max_length=200, null=True, verbose_name="封面图")
    desc = TextField(verbose_name="简介")
    notice = TextField(verbose_name="公告")

    # 小组的信息
    member_nums = IntegerField(default=0, verbose_name="成员数")
    post_nums = IntegerField(default=0, verbose_name="帖子数")

    @classmethod
    def extend(cls):
        return cls.select(cls, User.id, User.nick_name).join(User)


HANDLE_STATUS = (
    ("agree", "同意"),
    ("refuse", "拒绝")
)


class CommunityGroupMember(BaseModel):
    user = ForeignKeyField(User, verbose_name="用户")
    group = ForeignKeyField(CommunityGroup, verbose_name="小组")
    status = CharField(choices=HANDLE_STATUS, max_length=10, null=True, verbose_name="处理结果")
    handle_msg = CharField(max_length=200, null=True, verbose_name="拒绝理由")
    apply_reason = CharField(max_length=200, verbose_name="申请理由")
    handle_time = DateTimeField(default=datetime.now(), verbose_name="加入时间")

    @classmethod
    def extend(cls):
        return cls.select(cls, User, CommunityGroup).join(User).switch(cls).join(CommunityGroup)

class Post(BaseModel):
    user = ForeignKeyField(User, verbose_name="用户")
    title = CharField(max_length=200, verbose_name="标题", null=True)
    group = ForeignKeyField(CommunityGroup, verbose_name="小组")
    comment_nums = IntegerField(default=0, verbose_name="评论数")
    is_excellent = BooleanField(default=0, verbose_name="是否精华")
    is_hot = BooleanField(default=0, verbose_name="是否热门")
    content = TextField(verbose_name="内容")

    @classmethod
    def extend(cls):
        return cls.select(cls, User.id, User.nick_name).join(User)


class PostComment(BaseModel):
    # 评论和回复
    # user = ForeignKeyField(User, verbose_name="用户", related_name="author")
    post = ForeignKeyField(Post, null=True, verbose_name="帖子")
    parent_comment = ForeignKeyField('self', null=True, verbose_name="评论", related_name="comments_parent")
    # reply_user = ForeignKeyField(User, verbose_name="用户", related_name="replyed_author", null=True)
    content = TextField(verbose_name="评论内容")
    reply_nums = IntegerField(default=0, verbose_name="回复数")
    like_nums = IntegerField(default=0, verbose_name="点赞数")

    @classmethod
    def extend(cls):
        # 1. 多表join
        # 2. 多字段映射同一个model
        author = User.alias()
        relyed_user = User.alias()
        return cls.select(cls, Post, relyed_user.id, relyed_user.nick_name, author.id, author.nick_name).join(
            Post, join_type=JOIN.LEFT_OUTER, on=cls.post).switch(cls).join(author, join_type=JOIN.LEFT_OUTER,
                                                                           on=cls.user).switch(cls).join(
            relyed_user, join_type=JOIN.LEFT_OUTER, on=cls.reply_user
        )

class CommentLike(BaseModel):
    # 评论点赞
    user = ForeignKeyField(User, verbose_name="用户")
    post_comment = ForeignKeyField(PostComment, verbose_name="评论")