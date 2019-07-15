# encoding=utf-8
from flask import Flask, render_template, request, redirect
import pandas as pd
import numpy as np
import boto3
import calendar
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.template_folder = 'templates'
app.config['SQLALCHEMY_DATABASE_URI'] = "mysql+mysqlconnector://root:1234@127.0.0.1:3306/l2cloud?charset=utf8"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Billing(db.Model):
    __tablename__ = 'billings'
    id = db.Column(db.Integer, primary_key=True)
    InvoiceID = db.Column(db.String(256), index=True, nullable=True)
    PayerAccountId = db.Column(db.String(256), nullable=True)
    LinkedAccountId = db.Column(db.String(256), nullable=True)
    ProductCode = db.Column(db.String(256), nullable=True)
    AvailabilityZone = db.Column(db.String(256), nullable=True)
    UsageStartDate = db.Column(db.String(256), nullable=True)
    UsageEndDate = db.Column(db.String(256), nullable=True)

    UsageQuantity = db.Column(db.Float(), nullable=True)
    CostBeforeTax = db.Column(db.Float(), nullable=True)
    Credits = db.Column(db.Float(), nullable=True)
    TaxAmount = db.Column(db.Float(), nullable=True)
    TotalCost = db.Column(db.Float(), nullable=True)

    Tag_Name = db.Column(db.String(256), nullable=True)
    Tag_Value = db.Column(db.String(256), nullable=True)

    def __init__(self, kwarg):
        for k, v in kwarg.items():
            setattr(self, k, v)


def save_data(kwarg):
    admin = Billing(kwarg)
    db.session.add(admin)
    db.session.commit()


def get_time():
    date_time = request.form.get('date_time')
    year, month = date_time.split('-')[0], date_time.split('-')[1]
    end = calendar.monthrange(int(year), int(month))[1]
    start_date = '%s-%s-01' % (year, month)
    end_date = '%s-%s-%s' % (year, month, end)
    return start_date, end_date


def get_data():
    PayerAccountId = request.form.get('PayerAccountId')
    s3_bucket = request.form.get('s3_bucket')
    date_time = request.form.get('date_time')
    data = {}
    type = {
        'CostBeforeTax': np.float,
        'Credits': np.float,
        'TaxAmount': np.float,
        'UsageQuantity': np.float,
        'TotalCost': np.float,
        'UsageStartDate': np.object,
        'UsageEndDate': np.object,
        'PayerAccountId': np.object,
        'LinkedAccountId': np.object,
        'InvoiceID': np.object,
    }
    is_file = int(request.form.get('is_file', '0'))
    if is_file:
        obj = request.files['file']
        data = pd.read_csv(obj, dtype=type, skiprows=0)
    else:
        s3 = boto3.resource('s3')
        client = boto3.client('s3')
        response = client.list_buckets()
        if s3_bucket not in [item['Name'] for item in response['Buckets']]:
            return {}

        bucket = s3.Bucket(s3_bucket)
        for obj in bucket.objects.all():
            if f'{PayerAccountId}-aws-billing-csv-{date_time}.csv' == obj.key:
                data = pd.read_csv(obj.get()['Body'],
                                   dtype=type, skiprows=0)
    return data


def get_zone(demo_list):
    if isinstance(demo_list[0], np.float):
        return ""
    return demo_list[0]


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
            TotalCost=[],
            data=[]
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
            temp = dict()
            temp['Tag_Name'] = tag_name
            temp['Tag_Value'] = tag_value
            temp['AvailabilityZone'] = get_zone(list(data.loc[service_i, 'AvailabilityZone'].unique()))
            temp['ProductCode'] = list(data.loc[service_i, 'ProductCode'].unique())[0]
            temp['LinkedAccountId'] = list(data.loc[service_i, 'LinkedAccountId'].unique())[0]
            temp['PayerAccountId'] = list(data.loc[service_i, 'PayerAccountId'].unique())[0]
            temp['InvoiceID'] = list(data.loc[service_i, 'InvoiceID'].unique())[0]

            temp['UsageStartDate'] = get_time()[0]
            temp['UsageEndDate'] = get_time()[1]

            temp['CostBeforeTax'] = float(data.loc[service_i, 'CostBeforeTax'].sum())
            temp['Credits'] = float(data.loc[service_i, 'Credits'].sum())
            temp['TaxAmount'] = float(data.loc[service_i, 'TaxAmount'].sum())
            temp['UsageQuantity'] = float(data.loc[service_i, 'UsageQuantity'].sum())
            temp['TotalCost'] = float(data.loc[service_i, 'TotalCost'].sum())
            finally_dict['data'].append(temp)

            save_data(temp)
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
        import json
        return render_template('raw_index.html', **{"finally_dict": json.dumps(finally_dict), "flag": True})
    else:
        return render_template('raw_index.html', **{"flag": False})


if __name__ == '__main__':
    app.run(debug=True)
