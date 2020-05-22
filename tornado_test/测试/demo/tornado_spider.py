import time
from urllib.parse import urljoin

from bs4 import BeautifulSoup
from tornado import gen, httpclient, ioloop, queues

base_url = 'http://www.tornadoweb.org/en/stable/'
concurrency = 1000


async def get_url_links(url):
    response = await httpclient.AsyncHTTPClient().fetch(url)
    print("获取：{}".format(url))
    html = response.body.decode("utf8")
    soup = BeautifulSoup(html)
    links = [urljoin(base_url, a.get('href')) for a in soup.find_all('a', href=True)]
    return links


async def main():
    seen_set = set()
    q = queues.Queue()
    start = time.time()

    async def fetch_url(current_url):
        """生产者"""
        if current_url in seen_set:
            return
        seen_set.add(current_url)
        next_urls = await get_url_links(current_url)
        for new_url in next_urls:
            if new_url.startswith(base_url):
                await q.put(new_url)

    async def worker():
        async for url in q:
            if url is None:
                return
            try:
                await fetch_url(url)
            except Exception as e:
                print("exception: ", e)
            finally:
                q.task_done()

    # 放入初始Url到队列
    await q.put(base_url)

    # 启动协程
    workers = gen.multi([worker() for _ in range(concurrency)])
    # 等待上面的所有worker()结束工作
    await q.join()

    # 为了让 main 这个协程可以结束
    for _ in range(concurrency):
        await q.put(None)

    await workers


if __name__ == '__main__':
    # base_url = "http://www.studyai.com"
    # next_url = "/antares"
    # full_url = urljoin(base_url, next_url)
    # print(full_url)
    loop = ioloop.IOLoop.current()
    loop.run_sync(main)
