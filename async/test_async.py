# pip3 install pytest pytest-asyncio
import asyncio
import sys
from types import SimpleNamespace
import pytest


def check_pytest_asyncio_installed():
    import os
    from importlib import util
    if not util.find_spec('pytest_asyncio'):
        print('need install pytest_asyncio')
        sys.exit(os.EX_SOFTWARE)


async def return_after_sleep(res):
    return await asyncio.sleep(2, result=res)


async def setattr_async(loop, delay, ns, key, payload):
    loop.call_later(delay, setattr, ns, key, payload)


@pytest.fixture()
async def loop():
    return asyncio.get_running_loop()


@pytest.fixture()
def namespace():
    return SimpleNamespace()
