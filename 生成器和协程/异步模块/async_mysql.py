'''
pip install aiomysql
'''
import aiomysql
# from tornado import ioloop
import asyncio
import asyncio
from aiomysql.sa import create_engine
import sqlalchemy as sa


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


metadata = sa.MetaData()

user = sa.Table(
    'user',
    metadata,
    sa.Column('id', sa.Integer, autoincrement=True, primary_key=True),
    sa.Column('user_name', sa.String(16), nullable=False),
    sa.Column('pwd', sa.String(32), nullable=False),
    sa.Column('real_name', sa.String(6), nullable=False),
)


async def go(loop):
    """
    aiomysql项目地址：https://github.com/aio-libs/aiomysql
    :param loop:
    :return:
    """
    engine = await create_engine(user='root', db='test_mysql',
                                 host='127.0.0.1', password='123456', loop=loop)
    async with engine.acquire() as conn:
        await conn.execute(user.insert().values(user_name='user_name01', pwd='123456', real_name='real_name01'))
        await conn.execute('commit')

        async for row in conn.execute(user.select()):
            print(row.user_name, row.pwd)

    engine.close()
    await engine.wait_closed()


if __name__ == '__main__':
    # loop = ioloop.IOLoop.current()
    # loop.run_sync(test_example)
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(test_example(loop))
    asyncio.run(test_example())
