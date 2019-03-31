# yield 可以完成一个委派生成器的作用，在子生成器和调用者之间建立一个双向通道
import datetime
import heapq  # 堆模块
import time


class Task:
    def __init__(self, wait_until, coro):
        self.coro = coro
        self.waiting_until = wait_until

    def __eq__(self, other):
        return self.waiting_until == other.waiting_until

    def __lt__(self, other):
        return self.waiting_until < other.waiting_until


class SleepingLoop:

    def __init__(self, *coros):
        self._new = coros
        self._waiting = []

    def run_until_complete(self):

        for coro in self._new:
            wait_for = coro.send(None)  # delta 第一次等待接受
            heapq.heappush(self._waiting, Task(wait_for, coro))

        while self._waiting:
            now = datetime.datetime.now()
            task = heapq.heappop(self._waiting)
            if now < task.waiting_until:
                delta = task.waiting_until - now
                time.sleep(delta.total_seconds())
                now = datetime.datetime.now()
            try:
                wait_until = task.coro.send(now)
                heapq.heappush(self._waiting, Task(wait_until, task.coro))
            except StopIteration:
                pass


def sleep(seconds):
    now = datetime.datetime.now()
    wait_until = now + datetime.timedelta(seconds=seconds)
    actual = yield wait_until  # 返回一个datetime数据类型的时间
    return actual - now


def countdown(label, length, *, delay=0):
    delta = yield from sleep(delay)
    while length:
        print(label, 'T-minus', length)
        waited = yield from sleep(1)
        length -= 1


def main():
    loop = SleepingLoop(countdown('A', 2), countdown('B', 3, delay=1))
    start = datetime.datetime.now()

    loop.run_until_complete()

    print('Total elapsed time is', datetime.datetime.now() - start)


if __name__ == '__main__':
    main()
