import json
import os
import uuid

import aiofiles
from playhouse.shortcuts import model_to_dict

from LehuForum.handlers import RedisHandler
from apps.operates.models import Message
from apps.questions.forms import QuestionForm, AnswerForm
from apps.questions.models import Question, Answer
from apps.users.models import User
from apps.utils.async_decorators import authenticated_async
from apps.utils.util_funcs import json_serial


class QuestionHandler(RedisHandler):
    async def get(self, *args, **kwargs):
        # 获取问题列表
        ret_data = []
        question_query = Question.extend()

        # 根据用户进行过滤
        userid = self.get_argument("userid", None)
        if userid:
            question_query = question_query.filter(Question.user_id == int(userid))

        # 根据类别进行过滤
        ctg = self.get_argument("ctg", None)
        if ctg:
            question_query = question_query.filter(Question.category == ctg)
        # 根据参数进行排序
        order = self.get_argument("order", None)
        if order:
            if order == "new":
                question_query = question_query.order_by(Question.add_time.desc())
            elif order == "hot":
                question_query = question_query.order_by(Question.answer_nums.desc())
        questions = await self.application.objects.execute(question_query)
        for question in questions:
            question_dict = model_to_dict(question)
            question_dict["image"] = "{}/media/{}".format(self.settings["SITE_URL"], question_dict["image"])
            ret_data.append(question_dict)

        self.finish(json.dumps(ret_data, default=json_serial))

    @authenticated_async
    async def post(self, *args, **kwargs):
        # 添加问题
        ret_data = {}
        # 不能使用json form
        question_form = QuestionForm(self.request.body_arguments)
        if question_form.validate():
            # 自己完成图片字段的验证
            files_meta = self.request.files.get("image", None)
            if not files_meta:
                self.set_status(400)
                ret_data["image"] = "请上传图片!"
            else:
                # 完成图片保存并将值设置给对应的记录
                # 通过aiofiles写文件
                # 1. 文件名
                new_filename = ""
                for meta in files_meta:
                    filename = meta["filename"]
                    new_filename = "{uuid}_{filename}".format(uuid=uuid.uuid1(), filename=filename)
                    file_path = os.path.join(self.settings["MEDIA_ROOT"], new_filename)
                    async with aiofiles.open(file_path, 'wb') as f:
                        await f.write(meta['body'])
                question = await self.application.objects.create(
                    Question, user=self.current_user, category=question_form.category.data,
                    title=question_form.title.data, content=question_form.content.data,
                    image=new_filename
                )
                ret_data['question_id'] = question.id
        else:
            self.set_status(400)
            for field in question_form.errors:
                ret_data[field] = question_form.errors[field][0]

        self.finish(ret_data)


class QuestionDetailHandler(RedisHandler):
    async def get(self, question_id, *args, **kwargs):
        #获取某一个问题的详情
        ret_data = {}
        question_query = Question.extend().where(Question.id == int(question_id))
        questions = await self.application.objects.execute(question_query)
        counter = 0
        for data in questions:
            item_dict = model_to_dict(data)
            # item_dict["image"] = "{}/media/{}".format(self.settings["SITE_URL"], item_dict["image"])
            item_dict["image"] = f'{self.settings["SITE_URL"]}/media/{item_dict["image"]}'
            item_dict["add_time"] = item_dict["add_time"].strftime('%Y-%m-%d')
            ret_data = item_dict
            counter += 1
        if counter == 0:
            self.set_status(404)

        self.finish(ret_data)


class AnswerHandler(RedisHandler):
    @authenticated_async
    async def get(self, question_id, *args, **kwargs):
        # 获取问题的的所有答案
        ret_data = []
        try:
            question = await self.application.objects.get(Question, id=int(question_id))
            answers_query = Answer.extend().where(Answer.question == question, Answer.parent_answer.is_null(True))
            answers_query = answers_query.order_by(Answer.add_time.desc())
            answers = await self.application.objects.execute(answers_query)
            for item in answers:
                item_dict = {
                    "id": item.id, "content": item.content, "reply_nums": item.reply_nums,
                    "add_time": item.add_time,
                    "user": model_to_dict(item.user),
                }
                ret_data.append(item_dict)
        except Question.DoesNotExist as e:
            self.set_status(404)

        self.finish(json.dumps(ret_data, default=json_serial))

    @authenticated_async
    async def post(self, question_id, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode("utf8")
        param = json.loads(param)
        form = AnswerForm.from_json(param)
        if form.validate():
            try:
                question = await self.application.objects.get(Question, id=int(question_id))
                answer = await self.application.objects.create(Answer, user=self.current_user,
                                                               question=question,
                                                               content=form.content.data)
                ret_data['answer_id'] = answer.id
                ret_data['user'] = {'id': self.current_user.id, 'nick_name': self.current_user.nick_name}
                question.answer_nums += 1
                await self.application.objects.update(question)
                # 写入回答问题类型的消息
                reciever = await self.application.objects.get(User, id=question.user_id)
                await self.application.objects.create(Message, sender=self.current_user, reciever=reciever,
                                                      msg_type=2, parent=question.title, message=form.content.data)
            except Question.DoesNotExist as e:
                self.set_status(404)
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]