import json
import os
import uuid

import aiofiles
from playhouse.shortcuts import model_to_dict

from LehuForum.handlers import RedisHandler
from apps.communities.forms import CommunityGroupForm, GroupApplyForm, PostForm, CommentForm, ApplysForm
from apps.communities.models import CommunityGroup, CommunityGroupMember, Post, PostComment
from apps.operates.models import Message
from apps.users.models import User
from apps.utils.async_decorators import authenticated_async
from apps.utils.util_funcs import json_serial


class GroupHandler(RedisHandler):

    async def get(self, *args, **kwargs):
        ret_data = []
        group_query = CommunityGroup.extend()

        # 根据用户进行过滤
        userid = self.get_argument("userid", None)
        if userid:
            group_query = group_query.filter(CommunityGroup.creator_id == int(userid))

        # 根据类别进行过滤
        ctg = self.get_argument('ctg', None)
        if ctg:
            group_query = group_query.filter(CommunityGroup.category == ctg)

        # 根据参数进行排序
        order = self.get_argument('order', None)
        if order:
            if order == 'post_nums':
                group_query = group_query.order_by(CommunityGroup.post_nums.desc())
            if order == 'member_nums':
                group_query = group_query.order_by(CommunityGroup.member_nums.desc())
            if order == 'add_time':
                group_query = group_query.order_by(CommunityGroup.add_time.desc())

        groups = await self.application.objects.execute(group_query)
        for group in groups:
            group_dict = model_to_dict(group)
            group_dict['cover'] = "{}/media/{}".format(self.settings["SITE_URL"], group_dict['cover'])
            ret_data.append(group_dict)

        self.finish(json.dumps(ret_data, default=json_serial))

    @authenticated_async
    async def post(self, *args, **kwargs):
        ret_data = {}
        group_form = CommunityGroupForm(self.request.body_arguments)
        if group_form.validate():
            # 自己完成图片字段的验证
            files_meta = self.request.files.get('cover', None)
            if not files_meta:
                self.set_status(400)
                ret_data['cover'] = "请上传封面图像！"
            else:
                # 完成图片保存并将值设置给对应的记录
                # 通过aiofiles写文件
                # 1. 文件名
                new_filename = ""
                for meta in files_meta:
                    filename = meta["filename"]
                    new_filename = "{uuid}_{filename}".format(uuid=uuid.uuid1(), filename=filename)
                    file_path = os.path.join(self.settings["MEDIA_ROOT"], new_filename)
                    async with aiofiles.open(file_path, mode='wb') as f:
                        await f.write(meta['body'])

                group = await self.application.objects.create(CommunityGroup, creator=self.current_user,
                                                              name=group_form.name.data,
                                                              category=group_form.category.data,
                                                              desc=group_form.desc.data,
                                                              notice=group_form.notice.data,
                                                              cover=new_filename)
                ret_data["group_id"] = group.id

        else:
            self.set_status(400)
            for field in group_form.errors:
                ret_data[field] = group_form.errors[field][0]

        self.finish(ret_data)


class GroupMemberHandler(RedisHandler):
    @authenticated_async
    async def post(self, group_id, *args, **kwargs):
        # 申请加入小组
        ret_data = {}
        param = self.request.body.decode("utf8")
        param = json.loads(param)
        form = GroupApplyForm.from_json(param)
        if form.validate():
            try:
                group = await self.application.objects.get(CommunityGroup, id=int(group_id))
                existed = await self.application.objects.get(CommunityGroupMember, group=group, user=self.current_user)
                self.set_status(400)
                ret_data["non_fields"] = "用户已经加入该小组！"
            except CommunityGroup.DoesNotExist as e:
                self.set_status(404)
            except CommunityGroupMember.DoesNotExist as e:
                group_member = await self.application.objects.create(CommunityGroupMember, group=group,
                                                                     user=self.current_user,
                                                                     apply_reason=form.apply_reason.data)
                ret_data['member_id'] = group_member.id
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]

        self.finish(ret_data)


class GroupDetailHandler(RedisHandler):
    @authenticated_async
    async def get(self, group_id, *args, **kwargs):
        # 获取小组的基本信息
        ret_data = {}
        try:
            group = await self.application.objects.get(CommunityGroup, id=int(group_id))
            item_dict = dict()
            item_dict["name"] = group.name
            item_dict["id"] = group.id
            item_dict["desc"] = group.desc
            item_dict["notice"] = group.notice
            item_dict["member_nums"] = group.member_nums
            item_dict["post_nums"] = group.post_nums
            item_dict["cover"] = "{}/media/{}".format(self.settings["SITE_URL"], group.cover)
            ret_data = item_dict
        except CommunityGroup.DoesNotExist as e:
            self.set_status(404)

        self.finish(ret_data)


class PostHandler(RedisHandler):
    @authenticated_async
    async def get(self, group_id, *args, **kwargs):
        # 获取指定小组的帖子列表
        ret_data = []
        try:
            group = await self.application.objects.get(CommunityGroup, id=int(group_id))
            group_member = await self.application.objects.get(CommunityGroupMember,
                                                              user=self.current_user, group=group, status='agree')

            posts_query = Post.extend().filter(Post.group == group)

            # 根据excellent字段进行过滤
            excellent = self.get_argument('excellent', None)
            if excellent:
                posts_query = posts_query.filter(Post.is_excellent == True)

            # 根据参数进行排序
            order = self.get_argument('order', None)
            if order:
                if order == '-add_time':
                    posts_query = posts_query.order_by(Post.add_time.desc())

            posts = await self.application.objects.execute(posts_query)
            for post in posts:
                item_dict = {
                    "id": post.id,
                    "title": post.title,
                    "content": post.content,
                    "comment_nums": post.comment_nums,
                    "add_time": post.add_time,
                    "user": {
                        "id": post.user.id,
                        "nick_name": post.user.nick_name
                    }
                }
                ret_data.append(item_dict)

        except CommunityGroup.DoesNotExist as e:
            self.set_status(404)
        except CommunityGroupMember.DoesNotExist as e:
            self.set_status(403)

        self.finish(json.dumps(ret_data, default=json_serial))

    @authenticated_async
    async def post(self, group_id, *args, **kwargs):
        # 给指定小组发表帖子
        ret_data = {}
        param = self.request.body.decode("utf8")
        param = json.loads(param)
        form = PostForm.from_json(param)
        if form.validate():
            try:
                group = await self.application.objects.get(CommunityGroup, id=int(group_id))
                group_member = await self.application.objects.get(CommunityGroupMember,
                                                                  user=self.current_user, group=group, status='agree')
                post = await self.application.objects.create(Post, user=self.current_user, group=group,
                                                             title=form.title.data, content=form.content.data)
                ret_data['post_id'] = post.id
            except CommunityGroup.DoesNotExist as e:
                self.set_status(404)
            except CommunityGroupMember.DoesNotExist as e:
                self.set_status(403)
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]

        self.finish(ret_data)


class PostDetailHandler(RedisHandler):
    @authenticated_async
    async def get(self, post_id, *args, **kwargs):
        # 获取帖子的详细信息
        ret_data = {}
        # post = await self.application.objects.get(Post, id=int(post_id))
        posts_query = Post.extend().where(Post.id == int(post_id))
        posts = await self.application.objects.execute(posts_query)
        for data in posts:
            item_dict = dict()
            item_dict['user'] = model_to_dict(data.user)
            item_dict["title"] = data.title
            item_dict["content"] = data.content
            item_dict["comment_nums"] = data.comment_nums
            item_dict["add_time"] = data.add_time.strftime('%Y-%m-%d')
            ret_data = item_dict
        if len(posts) == 0:
            self.set_status(404)

        self.finish(ret_data)


class PostCommentHandler(RedisHandler):
    @authenticated_async
    async def get(self, post_id, *args, **kwargs):
        """获取指定帖子的评论列表"""
        ret_data = []
        try:
            post = await self.application.objects.get(Post, id=int(post_id))
            comments_query = PostComment.extend().where(PostComment.post == post,
                                                        PostComment.parent_comment.is_null(True)).order_by(
                PostComment.add_time.desc()
            )
            post_coments = await self.application.objects.execute(comments_query)
            for item in post_coments:
                item_dict = {
                    "user": model_to_dict(item.user),
                    "content": item.content,
                    "reply_nums": item.reply_nums,
                    "like_nums": item.like_nums,
                    "add_time": item.add_time,
                    "id": item.id,
                }
                ret_data.append(item_dict)
        except Post.DoesNotExist as e:
            self.set_status(404)

        self.finish(json.dumps(ret_data, default=json_serial))

    @authenticated_async
    async def post(self, post_id, *args, **kwargs):
        """为指定帖子提交评论"""
        ret_data = {}
        param = self.request.body.decode("utf8")
        param = json.loads(param)
        form = CommentForm.from_json(param)
        if form.validate():
            try:
                post = await self.application.objects.get(Post, id=int(post_id))
                comment = await self.application.objects.create(PostComment, user=self.current_user, post=post,
                                                                content=form.content.data)
                post.comment_nums += 1
                await self.application.objects.update(post)
                ret_data['comment_id'] = comment.id
                ret_data['user_name'] = self.current_user.nick_name
                ret_data['user_id'] = self.current_user.id
                # 写入帖子评论类型的消息
                reciever = await self.application.objects.get(User, id=post.user_id)
                await self.application.objects.create(Message, sender=self.current_user, reciever=reciever,
                                                      msg_type=1, parent=post.title, message=form.content.data)
            except Post.DoesNotExist as e:
                self.set_status(404)
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]

        self.finish(ret_data)


class ApplysHandler(RedisHandler):
    @authenticated_async
    async def get(self, *args, **kwargs):
        ret_data = []
        group_query = CommunityGroup.select().where(CommunityGroup.creator_id == self.current_user.id)
        all_groups = await self.application.objects.execute(group_query)
        all_group_ids = [group.id for group in all_groups]

        member_query = CommunityGroupMember.extend().where(CommunityGroupMember.group_id.in_(all_group_ids)).order_by(
            CommunityGroupMember.add_time.desc())
        all_members = await self.application.objects.execute(member_query)
        for member in all_members:
            item_dict = dict()
            item_dict["id"] = member.id
            item_dict["group"] = member.group.name
            item_dict["apply_reason"] = member.apply_reason
            item_dict["status"] = member.status
            item_dict["add_time"] = member.add_time.strftime("%Y-%m-%d %H:%M")
            item_dict["user"] = {
                "id": member.user.id,
                "nick_name": member.user.nick_name,
                "head_url": "{}/media/{}".format(self.settings["SITE_URL"], member.user.head_url)
            }
            ret_data.append(item_dict)

        self.finish(json.dumps(ret_data))


class ProcessApplysHandler(RedisHandler):
    @authenticated_async
    async def patch(self, apply_id, *args, **kwargs):
        """修改申请加入小组的状态：agree or refuse"""
        ret_data = {}
        param = self.request.body.decode("utf8")
        param = json.loads(param)
        form = ApplysForm.from_json(param)
        if form.validate():
            status = form.status.data
            handle_msg = form.handle_msg.data
            try:
                member = await self.application.objects.get(CommunityGroupMember, id=int(apply_id))
                member.status = status
                member.handle_msg = '' if status == 'agree' else handle_msg
                await self.application.objects.update(member)
            except CommunityGroupMember.DoseNotExist as e:
                self.set_status(404)
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]

        self.finish(ret_data)
