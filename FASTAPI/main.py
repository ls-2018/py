from starlette.requests import Request
from fastapi import Depends, FastAPI, Header, HTTPException

from starlette.staticfiles import StaticFiles
import uvicorn
import time as raw_time
from starlette.middleware.cors import CORSMiddleware
from api.api_v1.endpoints.api import api_router
from core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url='/docs',
    redoc_url=None,
    description="This is a very fancy project, with auto docs for the API and everything",
    version="6.6.6",
)
app.mount('/static', StaticFiles(directory='static'), name='static')
# Set all CORS enabled origins
app.add_middleware(  # 添加中间件
    CORSMiddleware,  # CORS中间件类
    allow_origins=['*'],  # 允许起源所有
    allow_credentials=True,  # 允许凭据
    allow_methods=["*"],  # 允许方法
    allow_headers=["*"],  # 允许头部
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = raw_time.time()
    response = await call_next(request)
    process_time = raw_time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


# def header(request: Request, user_agent: str = Header(None)):
#     # user_agent:str=Header(None) 匹配 User-Agent
#     print(user_agent)
#     return user_agent
async def get_token_header(user_agent: str = Header(None)):
    if not user_agent:  # 假超密令牌
        raise HTTPException(status_code=400, detail="user_agent header invalid")  # X令牌头无效


app.include_router(
    api_router,
    prefix=settings.API_V1_STR,
    tags=['items'],
    dependencies=[Depends(get_token_header)],
    responses={404: {'description': "Not found"}}
)

if __name__ == '__main__':
    uvicorn.run("main:app", host='127.0.0.1', port=8000, log_level='info', reload=True)
    # uvicorn.run(app, host='127.0.0.1', port=8000, log_level='info', reload=True)
# uvicorn main:app --reload
