from concurrent.futures.thread import ThreadPoolExecutor
from concurrent.futures.process import ProcessPoolExecutor
from concurrent.futures import Future

'''
使用线程池、进程池 来实现异步编程

asyncio orm + 同步mysql(使用concurrent 来结合两者)
'''
import time


def download_one(url):
    time.sleep(2)
    print(url)


def download_all(sites):
    pool = ThreadPoolExecutor(max_workers=5)
    for i in sites:
        print(pool.submit(download_one, i))
    # with ThreadPoolExecutor(max_workers=5) as executor:
    #     executor.map(download_one, sites)  # 对sites里的每个元素，执行download_one
    # with  ThreadPoolExecutor(max_workers=5) as executor:  # 系统自动返回CPU数
    #     to_do = []
    #     for site in sites:
    #         future = executor.submit(download_one, site)
    #         to_do.append(future)
    # for future in concurrent.futures.as_completed(to_do):
    #     future.result()  # 和放入的顺序不一定一致


if __name__ == '__main__':
    download_all([1, 2, 3, 4, 0, 5, 6, 7])
