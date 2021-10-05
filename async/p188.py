import os
import pickle
import sys
import tempfile
import time
import tracemalloc
from collections import namedtuple, defaultdict
from concurrent.futures.thread import ThreadPoolExecutor
from contextlib import asynccontextmanager
import asyncio
from inspect import iscoroutinefunction
import socket
from contextlib import asynccontextmanager
import asyncio
import contextlib
import inspect
import json
import logging
from functools import wraps
from tracemalloc import Filter, take_snapshot, start as tracemalloc_start, stop as tracemalloc_stop

logging.basicConfig(level=logging.DEBUG, stream=sys.stdout)
Timing = namedtuple("Timing", ['start', 'end', 'delta'])


class MockException(Exception):
    pass


def raiser_sync(text):
    raise MockException(text)


def exception_handler(loop, context):
    exception = context.get("exception")
    if isinstance(exception, MockException):
        print(exception, file=sys.stderr)
    else:
        loop.default_exception_handler(context)


async def main():
    loop: asyncio.AbstractEventLoop = asyncio.get_running_loop()
    loop.set_exception_handler(exception_handler)
    loop.call_soon(raiser_sync, 'Finally caught the loop.call_* mock exception')


asyncio.run(main(), debug=True)
