import asyncio


async def get_url():
    print(1)
    await asyncio.sleep(1)
    print(2)
    return 'x'
    # reader, writer = await asyncio.open_connection('www.baidu.com', 80)
    # writer.write(b'GET / HTTP/1.1\r\nHOST:www.baidu.com\r\nConnection:close\r\n\r\n')
    # async for line in reader:
    #     print(line)
    # return "html"


async def main():
    tasks = [
        asyncio.create_task(get_url(), name='n1'),
        asyncio.create_task(get_url(), name='n2'),
    ]
    # tasks.append(asyncio.ensure_future(get_url()))

    done, pending = await asyncio.wait(tasks, timeout=2)
    print(done)
    # for res in asyncio.as_completed(tasks):
    #     result = await res
    #     print(result)


if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # loop.run_until_complete(main())  # 处理一个任务
    # loop.run_until_complete(asyncio.wait([main()]))  # 处理多个任务
    # asyncio.run(main())
    """  
    会报错
    tasks = [
          asyncio.create_task(get_url(), name='n1'),    原因:运行到此处时没有事件循环
          asyncio.create_task(get_url(), name='n2'),
      ]
      done, pending =  asyncio.wait(tasks, timeout=2)
      print(done)
  """
    tasks = [
        get_url(),
        get_url(),
    ]
    done, pending = asyncio.run(asyncio.wait(tasks, timeout=2))
    print(done)
