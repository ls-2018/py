#_*_coding:utf-8_*_
__author__ = 'jieli'
from CrazyEye import settings
import os, tempfile, zipfile
from django.http import HttpResponse
#from django.core.servers.basehttp import FileWrapper
from wsgiref.util import FileWrapper #from django.core.servers.basehttp import FileWrapper
from web import models
import django
from django.db.models import Count,Sum
from backend import utils
import random,json,datetime,time
# from django.contrib.auth.models import User
from django.contrib.sessions.models import Session

def handle_upload_file(request,random_str,response_dic):
    upload_dir = '%s/task_data/tmp/%s' %(settings.FileUploadDir,random_str)
    if not os.path.isdir(upload_dir):
        os.makedirs(upload_dir,exist_ok=True)

    for k,file_obj in request.FILES.items():
        if len(os.listdir(upload_dir)) <= settings.MaxUploadFiles:
            with open('%s/%s' %(upload_dir,file_obj.name),'wb') as destination :
                for chunk in file_obj.chunks():
                    destination.write(chunk)
        else:
            response_dic['error'] = "can only upload no more than %s files." % (settings.MaxUploadFiles)


def send_file(request):
    """
    Send a file through Django without loading the whole file into
    memory at once. The FileWrapper will turn the file object into an
    iterator for chunks of 8KB.
    """
    filename = __file__ # Select your file here.
    wrapper = FileWrapper(file(filename))
    response = HttpResponse(wrapper, content_type='text/plain')
    response['Content-Length'] = os.path.getsize(filename)
    return response


def send_zipfile(request,task_id,file_path):
    """
    Create a ZIP file on disk and transmit it in chunks of 8KB,
    without loading the whole file into memory. A similar approach can
    be used for large dynamic PDF files.
    """
    zip_file_name = 'task_id_%s_files' % task_id
    archive = zipfile.ZipFile(zip_file_name , 'w', zipfile.ZIP_DEFLATED)
    file_list = os.listdir(file_path)
    for filename in file_list:
        archive.write('%s/%s' %(file_path,filename),arcname=filename)
    archive.close()
    wrapper = FileWrapper(open(zip_file_name,'rb'))
    response = HttpResponse(wrapper, content_type='application/zip')
    response['Content-Disposition'] = 'attachment; filename=%s.zip' % zip_file_name
    response['Content-Length'] = os.path.getsize(zip_file_name)
    #temp.seek(0)
    return response

class Token(object):
    def __init__(self,request):
        self.request = request
        self.token_type = request.POST.get('token_type')
        self.token = {'token':None}
    def generate(self):
        func = getattr(self,self.token_type)
        return func()
    def host_token(self):
        bind_host_id = self.request.POST.get('bind_host_id')
        host_obj = models.BindHosts.objects.get(id=int(bind_host_id))
        latest_token_obj = models.Token.objects.filter(host_id = int(bind_host_id),user_id=self.request.user.id).last()
        token_gen_flag = False

        if latest_token_obj:

            token_gen_time_stamp = time.mktime(latest_token_obj.date.timetuple())
            current_time = time.mktime(django.utils.timezone.now().timetuple() )
            if current_time - token_gen_time_stamp >latest_token_obj.expire:#token expired
                token_gen_flag = True
        else:
            token_gen_flag = True

        if token_gen_flag:
            token = ''.join(random.sample('zyxwvutsrqponmlkjihgfedcba1234567890',6))
            models.Token.objects.create(
                user = self.request.user,
                host = host_obj,
                token = token
            )
        else:
            token = latest_token_obj.token
        self.token['token'] = token
        return  json.dumps(self.token)

def get_all_logged_in_users():
    # Query all non-expired sessions
    # use timezone.now() instead of datetime.now() in latest versions of Django
    sessions = Session.objects.filter(expire_date__gte=django.utils.timezone.now())
    uid_list = []

    # Build a list of user ids from that query
    for session in sessions:
        data = session.get_decoded()
        uid_list.append(data.get('_auth_user_id', None))

    # Query all logged in users based on id list
    return models.UserProfile.objects.filter(id__in=uid_list)

class Dashboard(object):
    def __init__(self,request):
        self.request = request

    def get(self):
        data_type = self.request.GET.get("data_type")
        assert  data_type is not None
        func = getattr(self,data_type)
        return func()
    def get_online_users(self):
        return  get_all_logged_in_users().values('name','department__name','last_login','id')

    def get_online_hosts(self):
        return   models.Session.objects.filter(closed=0).values('bind_host__host__hostname',
                                                                 'user__name',
                                                                 'bind_host__host__ip_addr',
                                                                 'bind_host__host__id',
                                                                 'bind_host__host_user__username',
                                                                 'tag',
                                                                 'cmd_count',
                                                                'stay_time',
                                                                 'id','date')
def dashboard_summary(request):
    data_dic = {
        'user_login_statistics' :[],
        'recent_active_users':[],
        'recent_active_users_cmd_count':[],
        'summary':{}
    }
    days_before_30 = django.utils.timezone.now() +django.utils.timezone.timedelta(days=-30)
    #data_dic['user_login_statistics'] = list(models.AuditLog.objects.filter(action_type=1).extra({"login_date":"date(date)"}).values_list('login_date').annotate(count=Count('pk')))
    data_dic['user_login_statistics'] = list(models.Session.objects.filter(date__gt=days_before_30).extra({'login_date':'date(date)'}).values_list('login_date').annotate(count=Count('pk')))
    days_before_7 = django.utils.timezone.now() +django.utils.timezone.timedelta(days=-7)
    #recent_active_users= models.Session.objects.all()[0:10].values('user','user__name','cmd_count').annotate(Count('user'))
    recent_active_users= models.Session.objects.all()[0:10].values("user",'user__name').annotate(Sum('cmd_count'),Count('id'))
    recent_active_users_cmd_count= models.AuditLog.objects.filter(date__gt = days_before_7,action_type=0).values('user','user__name').annotate(Count('cmd'))
    data_dic['recent_active_users'] = list(recent_active_users)
    data_dic['recent_active_users_cmd_count'] = list(recent_active_users_cmd_count)
    data_dic['summary']['total_servers'] = models.Hosts.objects.count()
    data_dic['summary']['total_users'] = models.UserProfile.objects.count()
    data_dic['summary']['current_logging_users'] = get_all_logged_in_users().count()

    #current_connection servers
    current_connected_hosts = models.Session.objects.filter(closed=0).count()

    #current_connected_hosts = login_times - logout_times
    data_dic['summary']['current_connected_hosts'] = current_connected_hosts


    return  data_dic


def recent_accssed_hosts(request):
    days_before_14 = django.utils.timezone.now() +django.utils.timezone.timedelta(days=-14)
    recent_logins = models.AuditLog.objects.filter(date__gt = days_before_14,user_id=request.user.id,action_type=1).order_by('date')
    unique_bindhost_ids = set([i[0] for i in recent_logins.values_list('host_id')])
    recent_login_hosts = []
    for h_id in unique_bindhost_ids:
        recent_login_hosts.append(recent_logins.filter(host_id=h_id).latest('date'))

    return  set(recent_login_hosts)
