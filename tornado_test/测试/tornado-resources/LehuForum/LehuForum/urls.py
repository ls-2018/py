from tornado.web import url, StaticFileHandler

from LehuForum.settings import settings
from apps.users.urls import urlpattern as users_urls
from apps.communities.urls import urlpattern as communities_urls
from apps.questions.urls import urlpattern as questions_urls
from apps.operates.urls import urlpattern as operates_urls
from LehuForum.handlers import BaseHandler


class Handler(BaseHandler):
    def get(self):
        self.write('123')


urlpatterns = [
    url('/', Handler),
    url('/media/(.*)', StaticFileHandler, {'path': settings['MEDIA_ROOT']})
]

urlpatterns += users_urls
urlpatterns += communities_urls
urlpatterns += questions_urls
urlpatterns += operates_urls
