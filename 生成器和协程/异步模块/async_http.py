"""
pip install aiohttp

"""
import asyncio
import aiohttp


async def fetch(session, url):
    print('url')
    async with session.get(url, verify_ssl=False) as res:
        text = await res.text()
        print('ok', url, len(text))
        return 'ok'


async def start():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www.baidu.com'
        ]

        tasks = [asyncio.create_task(fetch(session, url)) for url in url_list]
        await asyncio.wait(tasks)


if __name__ == '__main__':
    asyncio.run(start())
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(start())
