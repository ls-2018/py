import json
import os
import uuid
from datetime import datetime
from random import choice

import aiofiles
import jwt

from LehuForum.handlers import RedisHandler
from apps.users.forms import SmsCodeForm, RegisterForm, LoginForm, ProfileForm, PasswordForm
from apps.users.models import User
from apps.utils.AsyncYunPian import AsyncYunPian
from apps.utils.async_decorators import authenticated_async


class SmsHandler(RedisHandler):
    def generate_code(self):
        """
        生成随机4位数字的验证码
        :return:
        """
        seeds = "1234567890"
        random_str = []
        for i in range(4):
            random_str.append(choice(seeds))
        return "".join(random_str)

    async def post(self, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        form = SmsCodeForm.from_json(param)
        if form.validate():
            mobile = form.mobile.data
            yunpian = AsyncYunPian("d6c4ddbf50ab36611d2f52041a0b949e")
            code = self.generate_code()
            re_json = await yunpian.send_single_sms(code, mobile)
            # re_json = {"code": 0 }
            if re_json["code"] != 0:
                self.set_status(400)
                ret_data["mobile"] = re_json["msg"]
            else:
                # 将验证码写入到Redis缓存
                self.redis_conn.set(f'{mobile}_{code}', 1, 10 * 60)
                ret_data = re_json
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]
        await self.finish(ret_data)


class RegisterHandler(RedisHandler):
    async def post2(self, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        form = RegisterForm.from_json(param)
        if form.validate():
            mobile = form.mobile.data
            code = form.code.data
            password = form.password.data
            # 判断验证码是否正确
            if not self.redis_conn.get(f'{mobile}_{code}'):
                self.set_status(400)
                ret_data = {"code": "验证码错误或已失效！"}
            else:

        else:
            self.set_status(400)
            for field in form.errors:
                ret_data = {field: form.errors[field][0]}

        await self.finish(ret_data)

    async def post(self, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        form = RegisterForm.from_json(param)
        if form.validate():
            mobile = form.mobile.data
            code = form.code.data
            password = form.password.data

            try:
                # 判断用户是否已经存在
                existed_user = await self.application.objects.get(User, mobile=mobile)
                self.set_status(400)
                ret_data = {"mobile": "该手机号码已经注册过了！"}
            except User.DoesNotExist as e:
                # 若不存在，则可以注册
                user = await self.application.objects.create(User, mobile=mobile, password=password)
                ret_data = {'id': user.id}
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data = {field: form.errors[field][0]}

        await self.finish(ret_data)


class LoginHandler(RedisHandler):
    async def post(self, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        form = LoginForm.from_json(param)
        if form.validate():
            mobile = form.mobile.data
            password = form.password.data
            try:
                # 判断用户是否已经存在
                user = await self.application.objects.get(User, mobile=mobile)
                if not user.password.check_password(password):
                    self.set_status(400)
                    ret_data["password"] = "密码错误!"
                else:
                    # 登录成功
                    # 1. 是不是rest api只能使用jwt
                    # session实际上是服务器随机生成的一段字符串， 保存在服务器的
                    # jwt 本质上还是加密技术，userid， user.name
                    # 生成json web token
                    payload = {
                        "id": user.id,
                        "nick_name": user.nick_name,
                        "exp": datetime.utcnow()
                    }
                    token = jwt.encode(payload, self.settings["secret_key"], algorithm='HS256')
                    ret_data["user_id"] = user.id
                    ret_data["token"] = token.decode("utf8")
                    if user.nick_name is not None:
                        ret_data["nick_name"] = user.nick_name
                    else:
                        ret_data["nick_name"] = user.mobile

            except User.DoesNotExist as e:
                self.set_status(400)
                ret_data["mobile"] = "用户手机号码尚未注册过!"
        else:
            self.set_status(400)
            ret_data["non_fields"] = "用户名或密码错误!"

        await self.finish(ret_data)


class ProfileHandler(RedisHandler):
    @authenticated_async
    async def get(self, *args, **kwargs):
        ret_data = {
            "id": self.current_user.id,
            "mobile": self.current_user.mobile,
            "nick_name": self.current_user.nick_name,
            "address": self.current_user.address,
            "gender": self.current_user.gender,
            "desc": self.current_user.desc,
        }
        await self.finish(ret_data)

    @authenticated_async
    async def patch(self, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        form = ProfileForm.from_json(param)
        if form.validate():
            self.current_user.nick_name = form.nick_name.data
            self.current_user.address = form.address.data
            self.current_user.gender = form.gender.data
            self.current_user.desc = form.desc.data
            await self.application.objects.update(self.current_user)
            ret_data = {
                "id": self.current_user.id,
                "mobile": self.current_user.mobile,
                "nick_name": self.current_user.nick_name,
                "address": self.current_user.address,
                "gender": self.current_user.gender,
                "desc": self.current_user.desc,
            }
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]

        await self.finish(ret_data)


class AvatarHandler(RedisHandler):
    @authenticated_async
    async def get(self, *args, **kwargs):
        ret_data = dict()
        ret_data['avatarUrl'] = "{}/media/{}".format(self.settings["SITE_URL"], self.current_user.head_url)
        await self.finish(ret_data)

    @authenticated_async
    async def post(self, *args, **kwargs):
        ret_data = {}
        files_meta = self.request.files.get("avatar", None)
        if not files_meta:
            self.set_status(400)
            ret_data["avatar"] = "请上传头像图片!"
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
                self.current_user.head_url = new_filename
                await self.application.objects.update(self.current_user)
                ret_data['avatarUrl'] = "{}/media/{}".format(self.settings["SITE_URL"], self.current_user.head_url)

        await self.finish(ret_data)


class PasswordHandler(RedisHandler):
    @authenticated_async
    async def post(self, *args, **kwargs):
        ret_data = {}
        param = self.request.body.decode('utf-8')
        param = json.loads(param)
        form = PasswordForm.from_json(param)
        if form.validate():
            # 检查旧密码
            if not self.current_user.password.check_password(form.oldPassword.data):
                self.set_status(400)
                ret_data["oldPassword"] = "旧密码错误！"
            else:
                if form.newPassword.data != form.checkPassword.data:
                    self.set_status(400)
                    ret_data["checkPassword"] = "两次输入的密码不一致！"
                else:
                    self.current_user.password = form.newPassword.data
                    await self.application.objects.update(self.current_user)
        else:
            self.set_status(400)
            for field in form.errors:
                ret_data[field] = form.errors[field][0]

        await self.finish(ret_data)
