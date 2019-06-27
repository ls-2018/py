"""
@Time: 2019/6/27 17:58 
@Author: liushuo
@File: day01.py 
@Desc: 第一天入职
@Software: PyCharm
"""
import boto3
from botocore.client import Config
import os
import sys
import threading

# 创建s3链接，如果s3服务器是第四代，则需要设置signature_version='s3v4'
s3_client = boto3.client('s3', endpoint_url='s3服务器地址',
                         aws_access_key_id='s3服务器的access_key_id',
                         aws_secret_access_key='s3服务器的secret_access_key',
                         region_name='s3服务器的时区，这里可以填写cn-north-1',
                         config=Config(signature_version='s3'))
# 3.获取s3中bucket列表

bucket_list = s3_client.list_buckets()

print(bucket_list)

# 4.创建bucket

bucket = s3_client.create_bucket(Bucket='bucket的名称')

print(bucket)

# 5.获取bucket信息
bucket_info = s3_client.head_bucket(Bucket='bucket的名称')

print(bucket_info)

# 6.删除bucket
# bucket_delete = s3_client.delete_bucket(Bucket='bucket的名称')

# 7.上传文件到s3服务器

# s3_client.upload_file("上传的源文件地址", "bucket名称", "上传文件在s3上对应的key名称", ExtraArgs={'ACL': 'public-read'})

# 或者

s3_client.upload_file("上传的源文件地址", "bucket名称", "上传文件在s3上对应的key名称", ExtraArgs={'ACL': 'public-read'},
                      Callback=UploadProgressPercentage("上传的源文件地址"))


# Callback属性对应的类方法如下，该类方法在控制台中打印了上传文件的进度

class UploadProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            sys.stdout.write(
                "\r%s  %s / %s  (%.2f%%)" % (
                    self._filename, self._seen_so_far, self._size,
                    percentage))
            sys.stdout.flush()


# 8.获取bucket下文件列表

object_list = s3_client.list_objects(Bucket='bucket名称')
print(object_list)

# 9.查看bucket下的某个文件信息
object_info = s3_client.get_object(Bucket='bucket名称', Key='文件对应的key名称')
print(object_info)
# 10.删除文件
object_delete = s3_client.delete_object(Bucket='bucket名称', Key='文件对应的key名称')

# 11.下载文件

s3_client.download_file("bucket名称", "文件对应的key名称", "文件下载到的地址")


# 或者
#
# s3client.download_file("bucket名称", "文件对应的key名称", "文件下载到的地址",Callback=DownloadProgressPercentage("文件下载到的地址"))
#
# Callback属性对应的类方法如下，该类方法在控制台中打印了下载文件的进度

class _DownloadProgressPercentage(object):
    def __init__(self, filename):
        self._filename = filename
        self._seen_so_far = 0
        self._lock = threading.Lock()

    def __call__(self, bytes_amount):
        # To simplify we'll assume this is hooked up
        # to a single filename.
        with self._lock:
            self._seen_so_far += bytes_amount
            sys.stdout.write(
                "\r%s --> %s bytes transferred" % (
                    self._filename, self._seen_so_far))
            sys.stdout.flush()
