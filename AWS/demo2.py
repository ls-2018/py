# encoding=utf-8
from flask import Flask, render_template, request
import pandas as pd
import numpy as np

app = Flask(__name__)
app.template_folder = 'templates'


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        link_user = '515743265704'
        tag_name = 'user:appenv'  # 标签名
        tag_value = 'dac-uat'  # 标签值
        finally_dict = {"data": {}}
        data = pd.read_csv(r'D:\Destop\123.csv', dtype={'LinkedAccountId': np.object})
        # 过滤用户数据
        user_i = [True if i == link_user else False for i in list(data['LinkedAccountId'])]
        data = data.loc[user_i]
        # 过滤标签数据
        tag_i = [True if i == tag_value else False for i in list(data[tag_name])]
        data = data.loc[tag_i]
        # 获取所有的服务名
        service_list = list(data['ProductCode'].unique())

        for service in service_list:
            service_i = [True if i == service else False for i in list(data['ProductCode'])]
            temp = dict()
            temp['CostBeforeTax'] = data.loc[service_i, 'CostBeforeTax'].sum()
            temp['Credits'] = data.loc[service_i, 'Credits'].sum()
            temp['TaxAmount'] = data.loc[service_i, 'TaxAmount'].sum()
            temp['UsageQuantity'] = data.loc[service_i, 'UsageQuantity'].sum()
            temp['TotalCost'] = data.loc[service_i, 'TotalCost'].sum()
            finally_dict['data'][service] = temp

        return render_template('index.html', **{})
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
