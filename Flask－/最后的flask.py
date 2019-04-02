from flask import Flask, url_for, render_template, redirect, send_file, jsonify,request

app = Flask(__name__)

# 3-Flask Request
# 4-Flask 路由
"""
endpoint                        反向URL(默认是函数名)
strict_slashes                  是否严格遵循路由规则,最后的/    
redirect_to='/login'            301 临时　　302重定向
defaults={'name': 'value'}      函数关键字传参
"""


@app.route('/index', methods=['GET', 'POST'], endpoint='index', strict_slashes=True)
def index():
    url = url_for('index')  # endpoint
    print(url)  # /index
    # #################         Flask Response   ###########################
    data = request.form         # 获取表单数据
    args = request.args         # url中的数据
    json_data = request.json    # 请求头Content-type:application/json 会自动序列化到这
    raw_data = request.data     # 请求体原始的信息,bytes



    # #################         Flask Response   ###########################


    # return str(url)
    # return redirect('/')
    # return render_template()
    # return send_file('文件的绝对路径')# 自动识别文件类型（image,viedo)
    return jsonify({'a': 21})  # 响应头中加入    Content-type:application/json








if __name__ == '__main__':
    app.run()

# 5-Flask 实例化配置
# 6-Flask 对象配置
# 7-Flask 蓝图
# 8-Flask Session
# 9-Flask 特殊装饰器   @app.before_request
# 10-Flask 请求上下文


# 智能玩具
# App 功能
# 玩具功能
