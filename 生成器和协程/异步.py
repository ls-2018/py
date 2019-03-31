async def download(url):
    return 'eva'


def run(coroutine):
    try:
        coroutine.send(None)
    except StopIteration as e:
        return e.value


coro = download('http://www.baidu.com/')
ret = run(coro)
print(ret)

"""
async关键字不能和yield一起使用，
"""