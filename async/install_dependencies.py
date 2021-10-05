import asyncio


async def main():
    res = await asyncio.subprocess.create_subprocess_shell(
        "pip install -i https://pypi.tuna.tsinghua.edu.cn/simple django uvicorn")
    await res.wait()


if __name__ == '__main__':
    asyncio.run(main())
