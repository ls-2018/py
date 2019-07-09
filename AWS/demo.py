# encoding=utf-8
from flask import Flask, render_template, request
import pandas as pd
import pandas as pd
import numpy as np

app = Flask(__name__)
app.template_folder = 'templates'


@app.route("/", methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        link_user = '515743265704'
        target_name = 'AmazonEC2'  # 服务名字
        tag_name = 'user:appenv'  # 标签名
        data = pd.read_csv(r'D:\Destop\123.csv', dtype={'LinkedAccountId': np.object})

        user_tag = []  # 标签
        for i in list(data.columns):
            if i.startswith('user:'):
                user_tag.append(i)

        user_unique = list(data['LinkedAccountId'].unique())
        if user_unique[-1] == np.nan:
            user_unique.remove(np.nan)

        user_i = [True if i == link_user else False for i in list(data['LinkedAccountId'])]
        data = data.loc[user_i]

        target_i = [True if i == target_name else False for i in list(data['ProductCode'])]
        data = data.loc[target_i]

        b = data[tag_name].sort_values()  # 将标签的值排序

        demo = {}
        for k, v in b.items():
            if demo.get(v):
                demo[v].append(k)
            else:
                demo[v] = [k, ]
        res = []
        for k, v in demo.items():
            temp = dict()
            temp['CostBeforeTax'] = data.loc[v, 'CostBeforeTax'].sum()
            temp['Credits'] = data.loc[v, 'Credits'].sum()
            temp['TaxAmount'] = data.loc[v, 'TaxAmount'].sum()
            res.append(res)
        return render_template('index.html', **{"user_tag": user_tag, "res": res, "user_unique": user_unique})

    # print(data['user: appenv'].isnull())
    # print(data.isnull())


if __name__ == '__main__':
    app.run()
