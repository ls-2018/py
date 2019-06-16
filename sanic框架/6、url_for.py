from sanic import Sanic

from sanic.response import json, redirect, text

app = Sanic()

app.config.SERVER_NAME = 'www.xxx.com'


@app.route('/')
async def test(request):
    url = app.url_for('post_handler', post_id=4, arg_one='one',
                      arg_two='two')  # /a/4?arg_one=one&arg_two=two
    url = app.url_for('post_handler', post_id=4, arg_one='one',
                      arg_two='two')  # /a/4?arg_one=one&arg_one=two
    url = app.url_for('post_handler', post_id=4, _anchor='anchar')  # http://127.0.0.1:8000/a/4#anchar
    url = app.url_for('post_handler', post_id=4, _external=True)  # http:///a/4  需要配置SERVER_NAME
    print(url)  # http://www.xxx.com/a/4
    url = app.url_for('post_handler', post_id=4, _external=True, _scheme='https', )
    print(url)  # https://www.xxx.com/a/4
    url = app.url_for('post_handler', post_id=4, _external=True, _scheme='https', )
    print(url)  # https://www.xxx.com/a/4
    """
    _scheme=‘http’  协议版本
    _server= 
    """
    return redirect(url)


@app.route('/a/<post_id>')
async def post_handler(request, post_id):
    return json({'a': post_id})


@app.get('/', name='get')
def get(request):
    return text('get')


@app.post('/', name='post')
def get(request):
    return text('post')


@app.put('/', name='put')
def get(request):
    return text('put')


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
