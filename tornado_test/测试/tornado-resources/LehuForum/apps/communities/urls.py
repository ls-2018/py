from tornado.web import url

from apps.communities.handlers import GroupHandler, GroupMemberHandler, GroupDetailHandler, PostHandler, \
    PostDetailHandler, PostCommentHandler, ApplysHandler, ProcessApplysHandler

urlpattern = [
    url("/groups/", GroupHandler),
    url("/groups/([0-9]+)/", GroupDetailHandler),
    url("/groups/([0-9]+)/members/", GroupMemberHandler),
    url("/groups/([0-9]+)/posts/", PostHandler),
    url("/posts/([0-9]+)/", PostDetailHandler),
    url("/posts/([0-9]+)/comments/", PostCommentHandler),
    url("/applys/", ApplysHandler),
    url("/members/([0-9]+)/", ProcessApplysHandler)
]
