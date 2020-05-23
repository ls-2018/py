'''
pip install aiomysql
'''
import aiomysql
# from tornado import ioloop
import asyncio


async def test_example():
    pool = await aiomysql.create_pool(host='127.0.0.1', port=3306,
                                      user='root', password='12345678',
                                      db='tornado', charset='utf8')
    async with pool.acquire() as conn:
        async with conn.cursor() as cur:
            await cur.execute("SELECT * FROM userinfo;")
            print(cur.description)
            r = await cur.fetchone()
            print(r)
    #         await conn.commit()  # 除了查以外，都需要commit
    pool.close()
    await pool.wait_closed()


async def test_example2():
    conn = await aiomysql.connect(host='127.0.0.1', port=3306,
                                  user='root', password='12345678',
                                  db='tornado', charset='utf8')
    async with conn.cursor() as cur:
        await cur.execute("SELECT * FROM userinfo;")
        print(cur.description)
        r = await cur.fetchone()
        print(r)
        #         await conn.commit()  # 除了查以外，都需要commit
        await cur.close()
    await conn.wait_closed()


if __name__ == '__main__':
    # loop = ioloop.IOLoop.current()
    # loop.run_sync(test_example)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test_example(loop))
    asyncio.run(test_example())
