from sanic import Sanic

from sanic.response import text

app = Sanic()


@app.route('/')
async def test(request):
    response = text('xxxxxx')
    response.cookies['a'] = 'it work'
    response.cookies['a']['domain'] = 'www.baidu.com'
    response.cookies['a']['httponly'] = True
    """
    expires(datetime)   过期时间
    path(str)           默认为/
    comment(str)        注释
    damain(str)         cookie有效的域。
    max-age(number)     cookie应该生存秒数
    secure(bool)        指定cookie是否仅通过https发送
    httponly(bool)      指定JavaScript是否无法读取cookie
    """
    return response

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
