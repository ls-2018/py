# encoding=utf-8
from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
import json
import boto3

app = Flask(__name__)
app.template_folder = 'templates'


def get_data():
    PayerAccountId = request.form.get('PayerAccountId')
    s3_bucket = request.form.get('s3_bucket')
    date_time = request.form.get('date_time')
    data = {}
    is_file = int(request.form.get('is_file', '0'))
    if is_file:
        obj = request.files['file']
        data = pd.read_csv(obj, dtype={'LinkedAccountId': np.object})
    else:
        s3 = boto3.resource('s3')
        client = boto3.client('s3')
        response = client.list_buckets()
        if s3_bucket not in [item['Name'] for item in response['Buckets']]:
            return {}

        bucket = s3.Bucket(s3_bucket)
        for obj in bucket.objects.all():
            if f'{PayerAccountId}-aws-billing-csv-{date_time}.csv' == obj.key:
                data = pd.read_csv(obj.get()['Body'], dtype={'LinkedAccountId': np.object})
    return data


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        link_user = request.form.get('link_user')
        tag_name = request.form.get('tag_name')  # 标签名
        tag_value = request.form.get('tag_value')  # 标签值

        data = get_data()

        if isinstance(data, dict):
            return redirect('/')
        if tag_name not in data.columns:
            return redirect('/')
        finally_dict = dict(
            CostBeforeTax=[],
            Credits=[],
            TaxAmount=[],
            UsageQuantity=[],
            TotalCost=[]
        )
        finally_dict['tag_name'] = tag_name
        finally_dict['tag_value'] = tag_value
        finally_dict['date_time'] = request.form.get('date_time')

        # 过滤用户数据
        user_i = [True if i == link_user else False for i in list(data['LinkedAccountId'])]
        data = data.loc[user_i]
        # 过滤标签数据

        if tag_value not in list(data[tag_name].unique()):
            return redirect('/')
        tag_i = [True if i == tag_value else False for i in list(data[tag_name])]

        data = data.loc[tag_i]
        # 获取所有的服务名
        service_list = list(data['ProductCode'].unique())

        for service in service_list:
            service_i = [True if i == service else False for i in list(data['ProductCode'])]

            CostBeforeTax = data.loc[service_i, 'CostBeforeTax'].sum()
            Credits = data.loc[service_i, 'Credits'].sum()
            TaxAmount = data.loc[service_i, 'TaxAmount'].sum()
            UsageQuantity = data.loc[service_i, 'UsageQuantity'].sum()
            TotalCost = data.loc[service_i, 'TotalCost'].sum()
            finally_dict['CostBeforeTax'].append({'name': service, 'y': CostBeforeTax})
            finally_dict['Credits'].append({'name': service, 'y': Credits})
            finally_dict['TaxAmount'].append({'name': service, 'y': TaxAmount})
            finally_dict['UsageQuantity'].append({'name': service, 'y': UsageQuantity})
            finally_dict['TotalCost'].append({'name': service, 'y': TotalCost})

        finally_dict['TotalCost'] = sorted(finally_dict['TotalCost'], key=lambda x: x['y'], reverse=True)
        finally_dict['TotalCost'][0]['sliced'] = True
        finally_dict['TotalCost'][0]['selected'] = True

        finally_dict['CostBeforeTax'] = sorted(finally_dict['CostBeforeTax'], key=lambda x: x['y'], reverse=True)
        finally_dict['CostBeforeTax'][0]['sliced'] = True
        finally_dict['CostBeforeTax'][0]['selected'] = True

        finally_dict['TaxAmount'] = sorted(finally_dict['TaxAmount'], key=lambda x: x['y'], reverse=True)
        finally_dict['TaxAmount'][0]['sliced'] = True
        finally_dict['TaxAmount'][0]['selected'] = True

        finally_dict['UsageQuantity'] = sorted(finally_dict['UsageQuantity'], key=lambda x: x['y'], reverse=True)
        finally_dict['UsageQuantity'][0]['sliced'] = True
        finally_dict['UsageQuantity'][0]['selected'] = True

        finally_dict['Credits'] = sorted(finally_dict['Credits'], key=lambda x: x['y'], reverse=True)
        finally_dict['Credits'][0]['sliced'] = True
        finally_dict['Credits'][0]['selected'] = True

        return render_template('raw_index.html', **{"finally_dict": json.dumps(finally_dict), "flag": True})
    else:
        return render_template('raw_index.html', **{"flag": False})


if __name__ == '__main__':
    app.run(debug=True)
