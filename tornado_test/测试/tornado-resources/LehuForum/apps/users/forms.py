from wtforms_tornado import Form
from wtforms import StringField, TextAreaField
from wtforms.validators import DataRequired, Regexp, AnyOf

MOBILE_REGEX = "^1[358]\d{9}$|^1[48]7\d{8}$|^176\d{8}$"


class SmsCodeForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"),
                                     Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])


class RegisterForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"),
                                     Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])
    code = StringField("验证码", validators=[DataRequired(message="请输入手机验证码")])
    password = StringField("密码", validators=[DataRequired(message="请输入密码")])


class LoginForm(Form):
    mobile = StringField("手机号码",
                         validators=[DataRequired(message="请输入手机号码"),
                                     Regexp(MOBILE_REGEX, message="请输入合法的手机号码")])
    password = StringField("密码", validators=[DataRequired(message="请输入密码")])


class ProfileForm(Form):
    nick_name = StringField("昵称", validators=[DataRequired(message="请输入昵称")])
    address = StringField("地址", validators=[DataRequired(message="请输入地址")])
    desc = TextAreaField("简介", validators=[DataRequired(message="请输入简介")])
    gender = StringField("性别", validators=[DataRequired(message="请输入性别"),
                                           AnyOf(values=["female", "male"])])


class PasswordForm(Form):
    oldPassword = StringField("旧密码", validators=[DataRequired(message="请输入旧密码")])
    newPassword = StringField("新密码", validators=[DataRequired(message="请输入新密码")])
    checkPassword = StringField("确认密码", validators=[DataRequired(message="请输入确认密码")])
