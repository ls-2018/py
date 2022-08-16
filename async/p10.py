# 进程本地事件循环
# 仅适用于UNIX
# 进程间共享一个字典，保存每个进程ID的事件循环实例


import os
import asyncio

pid_loops = {}


def get_event_loop():
    return pid_loops[os.getpid()]


def asyncio_init():
    pid = os.getpid()
    print('asyncio_init', pid, flush=True)
    if pid not in pid_loops:
        pid_loops[pid] = asyncio.new_event_loop()
        pid_loops[pid].pid = pid
    print(pid_loops)


if __name__ == '__main__':
    os.register_at_fork(after_in_parent=asyncio_init, after_in_child=asyncio_init)
    if os.fork() == 0:
        # 子进程
        loop = get_event_loop()
        print(pid_loops)

        pid = os.getpid()
        assert pid == loop.pid
        print('子进程', pid)
    else:
        # 父进程
        loop = get_event_loop()
        pid = os.getpid()
        assert pid == loop.pid
        print('父进程', pid)
        print(pid_loops)
