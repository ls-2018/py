"""
pip install aioredis

"""

import asyncio
from aioredis import Redis
import aioredis


async def execute(address, password):
    redis = await aioredis.create_redis(address, password=password)

    await redis.hmset_dict("car", key1=1, key2=2, key3=3)
    result = await redis.hgetall('car', encoding='utf8')
    print(result)

    redis.close()
    await redis.wait_closed()
    print('end')


async def execute2(address, password):
    pool = await aioredis.ConnectionsPool(address, password=password, minsize=1, maxsize=10)
    conn = await pool.acquire()
    redis = Redis(conn)
    await redis.hmset_dict("car", key1=1, key2=2, key3=3)
    result = await redis.hgetall('car', encoding='utf8')
    print(result)

    pool.release(conn)
    print('end')


asyncio.run(execute('redis://127.0.0.1:6379', None))
