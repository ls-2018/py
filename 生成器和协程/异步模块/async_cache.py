'''
pip install aiocache
'''
import asyncio
from aiocache import cached, RedisCache
from aiocache.serializers import PickleSerializer


# 为了体现缓存的速度，首次请求休眠3秒，请求过后，redis中就会将此次json数据缓存进去了，下次去请求就会直接冲redis读取数据。
@cached(ttl=1000, cache=RedisCache, key="rss_json", serializer=PickleSerializer(), port=6379, namespace="main")
async def get_rss():
    print("第一次休眠1秒 体现出和缓存时间上的差别...")
    await asyncio.sleep(1)
    return 'hello'


if __name__ == '__main__':
    print(asyncio.run(get_rss()))
    print(asyncio.run(get_rss()))
