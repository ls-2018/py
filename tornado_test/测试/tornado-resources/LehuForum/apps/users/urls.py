from tornado.web import url

from apps.users.handlers import SmsHandler, RegisterHandler, LoginHandler, ProfileHandler, AvatarHandler, PasswordHandler


urlpattern = [
    url("/code/", SmsHandler),
    url("/register/", RegisterHandler),
    url("/login/", LoginHandler),
    url("/info/", ProfileHandler),
    url("/avatar/", AvatarHandler),
    url("/password/", PasswordHandler),
]