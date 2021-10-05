"""
第9章/HomeSharing/app/controllers/user.py
"""

from app.db.action_with_db import ActionWithDb
from cms4py.http import Request, Response
import datetime, re
from pymysql.err import IntegrityError
from app.db import auth


class login(ActionWithDb):
    async def execute(self, req: Request, res):
        if req.method == "GET":
            await res.render("user/login.html", title="登录")
        elif req.method == 'POST':
            login_param = req.get_var_as_str(b"login")
            password = req.get_var_as_str(b"password")

            db = self.db
            user_record = (await db(
                (db.auth_user.user_name == login_param) |
                (db.auth_user.user_email == login_param) |
                (db.auth_user.user_phone == login_param)
            ).select()).first()
            _next = None
            if user_record:
                transcode = db.auth_user.user_password.requires(password)[0]
                if transcode == user_record.user_password:
                    # 将登录用户写入 session
                    await req.set_session(
                        "current_user", user_record.as_dict()
                    )
                    await res.redirect("/user/profile")
                else:
                    alert_msg = "用户名或密码错误"
                    await res.render(
                        "user/login.html",
                        title="登录", alert_msg=alert_msg
                    )
        else:
            await res.end(b"Unsupported method")


class register(ActionWithDb):
    async def execute(self, req: Request, res):
        db = self.db
        alert_msg = ""
        if req.method == 'GET':
            await res.render(
                "user/register.html", title="注册",
                alert_msg=alert_msg
            )
        elif req.method == "POST":
            login_name = req.get_var_as_str(b"login_name")
            email = req.get_var_as_str(b"email")
            phone = req.get_var_as_str(b"phone")
            password = req.get_var_as_str(b"password")
            # 将密码进行加密存储
            password = self.db.auth_user.user_password.requires(
                password
            )[0]
            try:
                if (await self.db.auth_user.insert(
                        user_name=login_name, user_email=email,
                        user_phone=phone, user_password=password,
                        reg_time=datetime.datetime.utcnow()
                )):
                    user_record = (
                        await db(
                            db.auth_user.user_name == login_name
                        ).select()
                    ).first()
                    await req.set_session(
                        "current_user", user_record.as_dict()
                    )
                    await res.redirect("/user/profile")
            except IntegrityError as err:
                alert_msg = "注册失败"

                # 错误提示信息如：
                # Duplicate entry 'a@a.a' for key 'user_email'
                # 该正则的目的是将字段名从错误提示信息中提取出来
                result = re.search(
                    "Duplicate entry .* for key '(\\w+)'",
                    err.args[1]
                )
                error_msg = result[1]
                if error_msg == 'user_email':
                    alert_msg = "邮箱已被占用"
                elif error_msg == 'user_name':
                    alert_msg = "用户名已被占用"
                elif error_msg == 'user_phone':
                    alert_msg = "手机号已被占用"
                await res.render(
                    "user/register.html", title="注册",
                    alert_msg=alert_msg
                )
            else:
                alert_msg = "注册失败"
                await res.render(
                    "user/register.html", title="注册",
                    alert_msg=alert_msg
                )
        else:
            await res.end(b"Method not supported")


@auth.require_login()
async def profile(req, res):
    await res.render("user/profile.html", title="用户信息")


async def logout(req: Request, res: Response):
    await req.set_session("current_user", None)
    await res.redirect("/user/login")


class pub_house(ActionWithDb):
    @auth.require_login()
    async def execute(self, req: Request, res):
        if req.method == "GET":
            await res.render("user/pub_house.html", title="发布房源")
        elif req.method == 'POST':
            user = await req.get_session("current_user")
            title = req.get_var_as_str(b"house_res_title")
            content = req.get_var_as_str(b'house_res_content')
            await self.db.house_res.insert(
                res_title=title,
                res_content=content,
                pub_time=datetime.datetime.now(),
                owner_id=user['id']
            )
            await res.redirect(f"/house/by_id/{self.db.lastrowid}")
            pass
        else:
            await res.end(b"Method not supported")
