from flask import Flask, Markup, render_template,url_for

app = Flask(__name__)


@app.template_global()
def ab(a, b):
    return a + b


@app.template_filter()
def axb(a, b):
    print(a, b)  # 2 3
    return a * b  # 模板{{ 2| axb(3) }} 有些像偏函数


@app.route('/', endpoint='index')  # 用来反向生成url,绝对不能一样，
def index():
    print(url_for(index))
    return render_template('index.html')

@app.before_request
def auth():
    """
函数将在没有任何参数的情况下被调用。如果返回
非空值，处理该值时将其视为返回值
停止视图和进一步的请求处理。
    :return:
    """
    pass


app.run(debug=True)
