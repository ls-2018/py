# encoding=utf-8
"""
@Time: 2019/7/4 13:01
@Author: liushuo
@File: 获取存储桶的信息.py 
@Desc: 
@Software: PyCharm
"""
import boto3

s3 = boto3.resource('s3')
client = boto3.client('s3')

buckets_list = client.list_buckets()

for bucket_obj in buckets_list['Buckets']:
    bucket = bucket_obj['Name']
    objects_dict = client.list_objects(Bucket=bucket)
    if not objects_dict.get('Contents'):
        continue
    objects_list = objects_dict['Contents']
    read_count = 0
    write_count = 0

    temp = set()

    for obj in objects_list:
        permission = s3.Object(bucket, obj['Key']).Acl().grants[0]['Permission']
        temp.add(permission)
        # Permission = ['FULL_CONTROL', 'WRITE', 'WRITE_ACP', 'READ', 'READ_ACP']
        if permission == 'FULL_CONTROL':
            read_count += 1
            write_count += 1
        elif permission == 'WRITE':
            write_count += 1
        elif permission == 'READ':
            read_count += 1
    print({
        '对象权限': temp,
        '桶': bucket,
        '版本控制': client.get_bucket_versioning(Bucket=bucket).get('Status', 'Disabled'),
        '公共访问': client.get_bucket_acl(Bucket=bucket)['Grants'][0]['Permission'],
        'read_count': read_count,
        'write_count': write_count
    })
