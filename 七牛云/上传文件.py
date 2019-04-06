# -*- coding: utf-8 -*-
'''
上传文件夹到七牛
'''

from qiniu import Auth, put_file
import os
import traceback

AK = ' '
SK = ' '
# 要上传的文件夹绝对路径
dir = r'D:\Destop\线上部署\线上部署\test\myblog\media'
# /static//bootstrap/css/
bucket_name = 'online_193'
q = Auth(AK, SK)
token = q.upload_token(bucket_name)


def updir(dirpath):
    if os.path.isdir(dirpath):  # 文件夹
        sublist = os.listdir(dirpath)
        for sub in sublist:
            updir(dirpath + '\\' + sub)
    else:  # 文件
        fpath, fname = os.path.split(dirpath)
        try:
            key = getKey(dirpath)
            print(key)
            ret, info = put_file(token, key, dirpath)
            if ret:
                print(ret)
        except:
            traceback.print_exc()


def getKey(file: str):
    key = ''
    demo1 = file.split('\\')
    fpath = '/'.join(demo1[demo1.index('media'):-1])

    return fpath + '/' + demo1[-1]


# D:\Destop\线上部署\线上部署\test\myblog\static\plugins\bootstrap\css

if __name__ == '__main__':
    updir(dir)

# import qiniu
#
#
# access_key = '*******************************'
# secret_key = '*******************************'
# url = '***************************'
# bucket_name = '*******************'
# q = qiniu.Auth(access_key, secret_key)
#
# def qiniu_upload(key, localfile):
#     token = q.upload_token(bucket_name, key, 3600)
#
#     ret, info = qiniu.put_file(token, key, localfile)
#
#     if ret:
#         return '{0}{1}'.format(url, ret['key'])
#     else:
#         raise UploadError('上传失败，请重试')
#
#
# key = '微信图片_20180408124226.jpg'
# localfile = 'C:/Users/Administrator.SKY-20180408LJB/Desktop/微信图片_20180408124226.jpg'
#
# res = qiniu_upload(key, localfile)
# print(res)
