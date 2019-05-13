from django.conf.urls import url
from .views import *
from .user import *
from .code import *
from .test import *
from .com import *
from .project import *
from .host import *

urlpatterns = [
    url(r'login/$', login, name="login"),
    url(r'logout/$', logout_view, name="logout"),
    url(r'index/$', index, name="index"),
    url(r'userall/$', user_all, name="userall"),
    url(r'updateall/$', update_all, name='updateall'),
    url(r'backall/$', update_all, name='backall'),
    url(r'testall/$', test_all, name='testall'),
    url(r'comall/$', command_all, name='comall'),
    url(r'projectall/$', project_all, name='projectall'),
    url(r'hostall/$', host_all, name='hostall'),
    url(r'hostcreate/$', host_create, name='hostcreate'),
    url(r'usercreate/$', user_create, name='usercreate'),
    url(r'testcreate/$', test_create, name='testcreate'),
    url(r'gitcreate/$', git_create, name='gitcreate'),
    url(r'filecreate/$', file_create, name='filecreate'),
    url(r'projectcreate/$', project_create, name='projectcreate'),
    url(r'commcreate/$', command_create, name='commandcreate'),
    url(r'hostdelete/(?P<pk>\d+)/$', host_delete, name="hostdelete"),
    url(r'testdelete/(?P<pk>\d+)/$', test_delete, name="testdelete"),
    url(r'userdelete/(?P<pk>\d+)/$', user_delete, name="userdelete"),
    url(r'comdelete/(?P<pk>\d+)/$', command_delete, name="comdelete"),
    url(r'teamdelete/(?P<pk>\d+)/$', project_delete, name="teamdelete"),
    url(r'hostedit/(?P<pk>\d+)/$', host_create, name="hostedit"),
    url(r'projectedit/(?P<pk>\d+)/$', project_create, name="projectedit"),
    url(r'codedetail/(?P<pk>\d+)/$', code_detail, name="codedetail"),
    url(r'teamdetail/(?P<pk>\d+)/$', team_detail, name="teamdetail"),
    url(r'testdetail/(?P<pk>\d+)/$', test_detail, name="testdetail"),
    url(r'update/(?P<pk>\d+)/$', update, name="update"),
    url(r'updateagain/(?P<pk>\d+)/$', update_again, name="updateagain"),
    url(r'successful/(?P<pk>\d+)/$', successful, name="successful"),
    url(r'backup/(?P<pk>\d+)/$', backup, name="backup"),

]
