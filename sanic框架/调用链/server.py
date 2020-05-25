#!/usr/bin/env python
# -*- coding: utf-8 -*-
from basictracer import BasicTracer
from sanic.config import Config
from sanic import Sanic
from sanic.response import json, HTTPResponse
from utils import *
from db import ConnectionPool
from loggers import AioReporter
from service import ServiceManager, service_watcher

config = Config()
config.from_pyfile('./config.py')
app = Sanic(config['APP_ID'], error_handler=CustomHandler())
app.config = config


@app.listener('before_server_start')
async def before_server_start(_app, loop):
    queue = asyncio.Queue()
    _app.queue = queue
    # add event loop
    loop.create_task(consume(queue, _app))
    loop.create_task(service_watcher(_app, loop))
    tracer = BasicTracer(recorder=AioReporter(queue=queue))
    tracer.register_required_propagators()
    opentracing.tracer = tracer
    _app.db = await ConnectionPool(loop=loop).init(_app.config['DB_CONFIG'])
    # service = ServiceManager(loop=loop, host=app.config['CONSUL_AGENT_HOST'])
    # services = await service.discovery_services()
    # app.services = defaultdict(list)
    # for name in services[1].keys():
    #     s = await service.discovery_service(name)
    #     app.services[name].extend(s)


@app.listener('after_server_start')
async def after_server_start(_app, loop):
    service = ServiceManager(_app.name, loop=loop, host=_app.config['CONSUL_AGENT_HOST'])
    await service.register_service(_app.config['PORT'])
    _app.service = service


@app.listener('before_server_stop')
async def before_server_stop(_app, loop):
    await _app.service.deregister()
    _app.queue.join()


@app.middleware('request')
async def cros(request):
    _config = request.app.config
    if request.method == 'OPTIONS':
        headers = {
            'Access-Control-Allow-Origin': _config['ACCESS_CONTROL_ALLOW_ORIGIN'],
            'Access-Control-Allow-Headers': _config['ACCESS_CONTROL_ALLOW_HEADERS'],
            'Access-Control-Allow-Methods': _config['ACCESS_CONTROL_ALLOW_METHODS']
        }
        return json({'code': 0}, headers=headers)
    if request.method == 'POST' or request.method == 'PUT':
        request['data'] = request.json
    span = before_request(request)
    request['span'] = span


@app.middleware('response')
async def cors_res(request, response):
    _config = request.app.config
    span = request['span'] if 'span' in request else None
    if response is None:
        return response
    result = {'code': 0}
    if not isinstance(response, HTTPResponse):
        if isinstance(response, tuple) and len(response) == 2:
            result.update({
                'data': response[0],
                'pagination': response[1]
            })
        else:
            result.update({'data': response})
        response = json(result)
        if span:
            span.set_tag('http.status_code', "200")
    if span:
        span.set_tag('component', request.app.name)
        span.finish()
    response.headers["Access-Control-Allow-Origin"] = _config['ACCESS_CONTROL_ALLOW_ORIGIN']
    response.headers["Access-Control-Allow-Headers"] = _config['ACCESS_CONTROL_ALLOW_HEADERS']
    response.headers["Access-Control-Allow-Methods"] = _config['ACCESS_CONTROL_ALLOW_METHODS']
    return response


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
