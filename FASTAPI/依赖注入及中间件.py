from fastapi import Depends, FastAPI, Header, HTTPException
import time
import string

app = FastAPI()


async def yi_lai_1(q: str = None, skip: int = 0, limit: int = 100):
    limit += 66
    return {'q': q, 'skip': skip, 'limit': limit}


async def yi_lai_2(xx: dict = Depends(yi_lai_1)):
    print(xx)
    return xx


@app.get('/items/')
async def read_items(commons: dict = Depends(yi_lai_2)):
    # 什么可以作为一个依赖？要可调用的 比如说类 函数 包等
    commons['skip'] += 10
    return commons


async def verify_token(x_token: str = Header(...)):
    if x_token != 'fake-super-secret-token':
        raise HTTPException(status_code=400, detail='X-Token header invalid')


@app.get('/item2/', dependencies=[Depends(verify_token), ])
async def read_item2():
    # 什么可以作为一个依赖？要可调用的 比如说类 函数 包等
    return {}


if __name__ == '__main__':
    import uvicorn

    uvicorn.run(app='依赖注入:app', host='127.0.0.1', port=8000, reload=True)

"""
依赖注入：
    可以理解为 异步的装饰器
    
"""
