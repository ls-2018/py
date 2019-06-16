from sanic import Sanic

from sanic.response import json, text

app = Sanic()


# @app.route('/<tag:int>')
@app.route('/<tag:[\d]+>')  # str
# @app.route('/<tag>',host='localhost')# str
# @app.route('/<tag:number>')# float
async def test(request, tag):
    print(tag, type(tag))
    return json({'json': "hello"}, )


@app.route('/')
async def test2(request):
    response = text('1/')
    # response.headers['host'] = 'localhost'
    return response


@app.route('/a', host='localhost')  # 该函数必须由该域名访问
async def test3(request):
    return text('x')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=80)
