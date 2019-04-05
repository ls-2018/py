from flask import Flask, Markup

app = Flask(__name__)


@app.add_template_global()
def ab(a, b):
    return a + b


@app.add_template_filter()
def axb(a, b):
    return a * b  # 模板{{ 2| axb(3) }} 有些像偏函数


app.run(debug=True)
