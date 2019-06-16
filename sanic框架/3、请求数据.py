from sanic import Sanic

from sanic.response import json, text

app = Sanic()


@app.route('/1')  # http://127.0.0.1:8000/1/?a=1&b=2
async def test2(request):
    print(request.json, '1')
    print(request.args, '2')
    print(type(request.args))  # <class 'sanic.request.RequestParameters'>
    print(request.query_args, '3')
    print(request.url, '4')
    print(request.query_string, '5')
    print(request.raw_args, '6')
    print(request.host, '7')
    print(request.path, '8')
    print(request.get('url_template'), '9')
    print(request.token, '10')
    """
None 1
{'a': ['1'], 'b': ['2']} 2
[('a', '1'), ('b', '2')] 3
http://127.0.0.1:8000/?a=1&b=2 4
a=1&b=2 5
{'a': '1', 'b': '2'} 6
127.0.0.1:8000 7
/ 8
None 9
None 10
b''
    """

    # test_file = request.files.get('key1')
    # print(test_file.body)
    # print(test_file.name)
    # print(test_file.type)

    # var_form = request.form
    print(request.body)  # post方式提交的原始数据
    return json({'json': "hello"})


@app.route('/')  # http://127.0.0.1:8000/?a=1&a=2
async def test(request):
    print(request.args)
    from sanic.request import RequestParameters
    args = RequestParameters()
    args['titles'] = ['1', '2']
    print(args.get('titles'))
    print(args.getlist('titles'))
    """
{'a': ['1', '2']}
1
['1', '2']
    """
    print(request.endpoint)  # 3、请求数据.test
    from sanic import response
    # return response.raw(b'raw data')

    return response.json({'message':"xxx"},headers={'X-Serverd-By':'sanic'},status=200)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
