from sanic import Sanic

from sanic.response import json

app = Sanic()
# app.config.DB_HOST=''
app.config.update({
    'DB_HOST': "localhost",
    'DB_NAME': "online",
    'DB_USER': 'root'
})


@app.route('/')
async def test(request):
    return json({'json': "hello"})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
