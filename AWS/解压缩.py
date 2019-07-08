import zipfile
import boto3
import pandas as pd

#
s3 = boto3.resource('s3')
bucket = s3.Bucket('s3-billing')
data1 = data2 = None
for obj in bucket.objects.all():
    # if '936669166135-aws-billing-detailed-line-items-ACTS-2017-08.csv.zip' == obj.key:
    if '936669166135-aws-billing-csv-2017-09.csv' == obj.key:
        data1 = pd.read_csv(obj.get()['Body'])

print(data1)
