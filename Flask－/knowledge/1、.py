from flask import Flask, Markup,render_template

app = Flask(__name__)

@app.template_global()
def ab(a, b):
    return a + b


@app.template_filter()
def axb(a, b):
    return a * b  # 模板{{ 2| axb(3) }} 有些像偏函数


@app.route('/', methods=[])
def index():
    return render_template('index.html')


app.run(debug=True)
