import os
import tempfile
from concurrent.futures.thread import ThreadPoolExecutor
from contextlib import asynccontextmanager
import asyncio


class AsyncFile:
    def __init__(self, file, loop=None, executor=None):
        if not loop:
            loop = asyncio.get_running_loop()
        if not executor:
            executor = ThreadPoolExecutor(10)
        self.file = file
        self.loop = loop
        self.executor = executor
        self.pending = []
        self.result = []

    def write(self, string):
        self.pending.append(self.loop.run_in_executor(self.executor, self.file.write, string))

    def read(self, i):
        self.pending.append(self.loop.run_in_executor(self.executor, self.file.read, i))

    def read_lines(self):
        self.pending.append(self.loop.run_in_executor(self.executor, self.file.read_lines))


@asynccontextmanager
async def async_open(path, mode='w'):
    with open(path, mode=mode) as f:
        loop = asyncio.get_running_loop()
        file = AsyncFile(f, loop=loop)
        try:
            yield file
        finally:
            file.result = await asyncio.gather(*file.pending, loop=loop)


async def main():
    tempdir = tempfile.gettempdir()
    path = os.path.join(tempdir, 'run.txt')
    print(path)
    async with async_open(path, mode='w') as f:  # type:AsyncFile
        for i in range(1000000):
            # todo 不是线程安全的
            f.write(f'{i}\n')
        print(f.result)


asyncio.run(main())
