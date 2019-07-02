from flask import Blueprint

from flask import Flask, \
    url_for, \
    Response, render_template, redirect, send_file, jsonify, \
    request, \
    session

# #################         Flask 蓝图   ###########################
# 7-Flask 蓝图        不能run的flask实例
user = Blueprint('user', __name__, url_prefix='/user')

# #################         Flask Router   ###########################
"""
# 4-Flask 路由
endpoint                        反向URL(默认是函数名)
strict_slashes                  是否严格遵循路由规则,最后的/    
redirect_to='/login'            301 临时　　302重定向
defaults={'name': 'value'}      函数关键字传参
"""


@user.route('/<int:id>', )
def id(id):
    return str(id)


@user.route('/user', methods=['GET', 'POST'], endpoint='user_index')
def index():
    # url = url_for('user_index')  # endpoint
    # print(url)  # /index
    # #################         Flask Request   ###########################
    # 3-Flask Request

    data = request.form  # 获取表单数据    K-V
    args = request.args  # url中的数据
    json_data = request.json  # 请求头Content-type:application/json 会自动序列化到这
    raw_data = request.data  # 请求体原始的信息,bytes

    # file = request.files.get('my_file')  # FormData中的文件类型数据
    # file.save(file.filename)

    # cookies_dict = request.cookies

    # #################         Flask Session   ###########################
    # 8-Flask Session
    # Flask中的Session信息存放在客户端        Cookie-Session:*****************************
    # app需要设置secret_key
    # print(session)

    # #################         Flask Response   ###########################
    # return str(url)
    # return redirect('/')
    # return render_template()
    # return send_file('文件的绝对路径')# 自动识别文件类型（image,viedo)
    return jsonify({'a': 21})  # 响应头中加入    Content-type:application/json   由配置文件控制

# 10-Flask 请求上下文


# 智能玩具
# App 功能
# 玩具功能
