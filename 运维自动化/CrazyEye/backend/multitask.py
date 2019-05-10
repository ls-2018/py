__author__ = 'jieli'

import global_settings
import json
import traceback
import paramiko
from CrazyEye import settings
import django
django.setup()
from web import models
from django.db import connection
import sys,time,os
import multiprocessing

def cmd_exec(task_id,bind_host_id,user_id,cmd ):
    bind_host = models.BindHosts.objects.get(id=bind_host_id)
    s = paramiko.SSHClient()
    s.load_system_host_keys()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        if bind_host.host_user.auth_method == 'ssh-password':
            s.connect(bind_host.host.ip_addr,
                      int(bind_host.host.port),
                      bind_host.host_user.username,
                      bind_host.host_user.password,
                      timeout=5)
        else:#rsa_key

            key = paramiko.RSAKey.from_private_key_file(settings.RSA_PRIVATE_KEY_FILE)
            s.connect(bind_host.host.ip_addr,
                      int(bind_host.host.port),
                      bind_host.host_user.username,
                      pkey=key,
                      timeout=5)
        stdin,stdout,stderr = s.exec_command(cmd)
        result = stdout.read(),stderr.read()
        if any(result):
            #cmd_result = filter(lambda x:len(x.strip())>0,result)[0]
            cmd_result = result[0] if result[0] else result[1]
        else:
            cmd_result = b'execution has no output!'
        res_status = 'success'
        print('----------- HOST:%s  IP:%s -------------' %(bind_host.host.hostname,bind_host.host.ip_addr) )

        # for line in cmd_result.decode():
        #     print(line)
        print(cmd_result.decode())
        s.close()
    except Exception as e:
    #except ValueError as e:
        print('----------- HOST:%s  IP:%s -------------' %(bind_host.host.hostname,bind_host.host.ip_addr))
        print('\033[31;1mError:%s\033[0m' % e)
        print(traceback.print_exc())
        cmd_result = e
        res_status = 'failed'
    log_obj = models.TaskLogDetail.objects.get(child_of_task_id= int(task_id), bind_host_id=bind_host.id)
    log_obj.event_log = cmd_result
    log_obj.result= res_status
    log_obj.save()


def file_tranfer_exec(task_id,bind_host_id,user_id,content ):
    #print '-->',task_id,bind_host_id,user_id,content
    task_type = content[content.index('-task_type') +1]
    remote_path = content[content.index('-remote') +1]
    bind_host = models.BindHosts.objects.get(id=bind_host_id)
    task_obj = models.TaskLog.objects.get(id=task_id)
    print("task obj:",task_obj)
    try:
        t = paramiko.Transport((bind_host.host.ip_addr,int(bind_host.host.port) ))
        if bind_host.host_user.auth_method == 'ssh-password':

            t.connect(username=bind_host.host_user.username,password=bind_host.host_user.password)
        else:
            key = paramiko.RSAKey.from_private_key_file(settings.RSA_PRIVATE_KEY_FILE)
            t.connect(username=bind_host.host_user.username,pkey=key)

        sftp = paramiko.SFTPClient.from_transport(t)

        cmd_result = ''
        if task_type == 'file_send':
            #local_file_list =content[content.index('-local') +1].split()
            local_file_path = "%s/task_data/tmp/%s" %(settings.FileUploadDir, task_obj.files_dir)
            #print("local_file_path",local_file_path)
            if os.path.isdir(local_file_path):
                for filename in os.listdir(local_file_path):
                    local_file = "%s/%s" %(local_file_path,filename)


                    remote_file_path = '%s/%s' %(remote_path,filename)
                    #print(local_file,remote_file_path)

                    sftp.put(local_file,remote_file_path)
                    #cmd_result += '%s  ' %filename
                    cmd_result += "file [%s] sent to remote path [%s] is completed\n" % (filename,remote_path)
            #print("----->cmd result:",cmd_result)
        else:

            local_path = "%s/task_data/%s/" %(settings.FileUploadDir,task_id)


            remote_filename = remote_path.split("/")[-1]
            local_file_path = "%s.%s" %(remote_filename,bind_host.host.ip_addr)
            print('->file get:',local_file_path,remote_filename)
            sftp.get(remote_path,'%s/%s' %(local_path,local_file_path) )
            cmd_result ='download remote file [%s] is completed!' % remote_path

        res_status = 'success'
    except Exception as e:
        print(e)
        cmd_result = e
        res_status = 'failed'
    log_obj = models.TaskLogDetail.objects.get(child_of_task_id= int(task_id), bind_host_id=bind_host.id)
    log_obj.event_log = cmd_result
    log_obj.result= res_status
    log_obj.save()

if __name__ == '__main__':
    require_args= ['-task_type','-task_id','-expire','-uid']
    lack_args = [arg for arg in require_args if arg not in sys.argv[1:]]
    if len(lack_args) >0:
        sys.exit("lack args of: %s"% lack_args)
    task_type = sys.argv[sys.argv.index('-task_type')+1]
    if task_type =='cmd':
        require_args= ['-task',]
    # elif task_type == 'file_send':
    #     require_args = ['-local','-remote']
    elif task_type == 'file_get':
        require_args = ['-remote',]

    lack_args = [arg for arg in require_args if arg not in sys.argv[1:]]
    if len(lack_args) >0:
        sys.exit("lack args of: %s"% lack_args)

    task_id = sys.argv[sys.argv.index('-task_id')+1]
    expire_time = sys.argv[sys.argv.index('-expire')+1]

    if task_type =='cmd':
        content = sys.argv[sys.argv.index('-task')+1]
    else:
        content = sys.argv
    uid = sys.argv[sys.argv.index('-uid')+1]
    task_obj = models.TaskLog.objects.get(id=int(task_id))
    connection.close()

    Pool = multiprocessing.Pool(processes=settings.MaxTaskProcesses)
    res_list = []

    if task_type == 'cmd':
        task_func = cmd_exec
    elif task_type == 'file_send' or task_type == 'file_get':
        task_func = file_tranfer_exec
    else:
        sys.exit("wrong task_type")
    for h in task_obj.hosts.select_related():
        p = Pool.apply_async(task_func,args=(task_id,h.id,uid,content))
        res_list.append(p)

    #get result
    Pool.close()
    Pool.join()
    #for res in res_list:
    #    res.get()