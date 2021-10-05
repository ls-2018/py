# 发现回调时间长运行的回调函数
import argparse
import asyncio
import logging
import os
import sys
import time
import inspect
from functools import wraps
import pdb


def get_asyncio_debug_mode_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('--asyncio-debug', action='store_true', dest='__asyncio_debug__', default=True)
    return parser


def is_asyncio_debug_mode(parser=get_asyncio_debug_mode_parser()):
    return parser and parser.parse_args().__asyncio_debug__ or os.getenv("CUSTOM_ASYNCIO_DEBUG")


__asyncio_debug__ = is_asyncio_debug_mode()


def post_mortem(f):
    if not __asyncio_debug__:
        return f
    if inspect.isasyncgenfunction(f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            try:
                async for payload in f(*args, **kwargs):
                    yield payload
            except BaseException as e:
                pdb.post_mortem()
                raise e
    else:
        @wraps(f)
        async def wrapper(*args, **kwargs):
            try:
                return await f(*args, **kwargs)
            except BaseException as e:
                pdb.post_mortem()
                raise e
    return wrapper


def pre_run(f):
    if not __asyncio_debug__:
        return f
    if inspect.isasyncgenfunction(f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            pdb.set_trace()
            async for payload in f(*args, **kwargs):
                yield payload
    else:
        @wraps(f)
        async def wrapper(*args, **kwargs):
            pdb.set_trace()
            return await f(*args, **kwargs)
    return wrapper


def post_run(f):
    if not __asyncio_debug__:
        return f
    if inspect.isasyncgenfunction(f):
        @wraps(f)
        async def wrapper(*args, **kwargs):
            async for payload in f(*args, **kwargs):
                yield payload
            pdb.set_trace()

    else:
        @wraps(f)
        async def wrapper(*args, **kwargs):
            result = await f(*args, **kwargs)
            pdb.set_trace()
            return result
    return wrapper


@post_mortem
async def main():
    raise Exception()


asyncio.run(main())
