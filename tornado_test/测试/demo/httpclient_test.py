from tornado import httpclient, ioloop


# http_client = httpclient.HTTPClient()
# try:
#     response = http_client.fetch("http://www.tornadoweb.org/en/stable/")
#     print(response.body)
# except httpclient.HTTPError as e:
#     # HTTPError is raised for non-200 responses; the response
#     # can be found in e.response.
#     print("Error: " + str(e))
# except Exception as e:
#     # Other errors are possible, such as IOError.
#     print("Error: " + str(e))
# http_client.close()


async def f():
    http_client = httpclient.AsyncHTTPClient()
    try:
        response = await http_client.fetch("http://www.tornadoweb.org/en/stable/")
    except Exception as e:
        print("Error: %s" % e)
    else:
        print(response.body.decode('utf8'))


if __name__ == "__main__":
    ioloop = ioloop.IOLoop.current()  # 单例模式，全局唯一
    # run_sync 方法可以在运行完某个协程后停止事件循环
    ioloop.run_sync(f)
    # import asyncio
    # asyncio.ensure_future(f())# 注册coroutine
    # asyncio.get_event_loop().run_forever()
    # asyncio.get_event_loop().run_until_complete(f())
