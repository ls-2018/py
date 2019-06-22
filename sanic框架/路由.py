from sanic import Sanic
from sanic.response import json, text
import pytest
app = Sanic(__name__)


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



# if __name__ == '__main__':
#     app.run(host='127.0.0.1', port=7777,debug=True)
@pytest.yield_fixture
def app():
    app = Sanic("test_sanic_app")

    @app.route("/test_get", methods=['GET'])
    async def test_get(request):
        return json({"GET": True})

    @app.route("/test_post", methods=['POST'])
    async def test_post(request):
        return json({"POST": True})

    yield app


@pytest.fixture
def test_cli(loop, app, test_client):
    return loop.run_until_complete(test_client(app, protocol=WebSocketProtocol))


#########
# Tests #
#########

async def test_fixture_test_client_get(test_cli):
    """
    GET request
    """
    resp = await test_cli.get('/')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"GET": True}

async def test_fixture_test_client_post(test_cli):
    """
    POST request
    """
    resp = await test_cli.post('/')
    assert resp.status == 200
    resp_json = await resp.json()
    assert resp_json == {"POST": True}
