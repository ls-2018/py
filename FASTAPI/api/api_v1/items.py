from enum import Enum
from typing import List, Dict, Set, Tuple, Optional, Union
from fastapi import Query, Path, Body, status, Form, File, UploadFile, Cookie, Depends, HTTPException
from fastapi.encoders import jsonable_encoder
from pydantic import BaseModel, Field, HttpUrl
from starlette.requests import Request
from starlette.responses import StreamingResponse
from starlette.templating import Jinja2Templates
from fastapi.responses import JSONResponse, Response, HTMLResponse, ORJSONResponse
from fastapi import APIRouter

from core.security import oauth2_scheme

router = APIRouter()

templates = Jinja2Templates(directory='templates')


class Item(BaseModel):
    # 有等于号的是可选参数
    name: str
    demo: List[Dict[str, float]]
    is_offer: bool = Field(..., example=True)
    # a: Tuple[int, int, bool]
    # se: Set[bytes] = {b"123"}
    # description: str = Field(None, title="The description of the item", max_length=300)
    price: float = Field(..., description="The price must be greater than zero")
    url: HttpUrl

    # Field的工作方式与Query，Path和相同，并且Body具有所有相同的参数

    class Config:
        """
        默认展示信息,覆盖上边的
        """
        schema_extra = {
            "example": {
                "name": "Foo",
                'is_offer': False,
                'dict': {"a": 1},
                "price": 35.4,
                "url": 'https://fastapi.tiangolo.com/tutorial/schema-extra-example/',
            }
        }


class ModelName(str, Enum):  # 继承的属性
    alexnet = "1"
    resnet = "2"


@router.get(
    "/",
    tags=['item'],
    responses={
        404: {"description": "Item not found"},
        302: {"description": "The item was moved"},
        403: {"description": "Not enough privileges"},
        200: {"content": {"image/png": {}}}},
)
async def read_root(a: str = Cookie(None)):  # 从Cookie中读取参数a
    return JSONResponse({"Hello": a})


@router.get("/one/{name:str}")
async def read_one(
        name: ModelName = Path(..., title='The Name of Module'),  # str可选 ge=1  gt  lt  le
        # q: str = Query("fixedquery", min_length=3, max_length=50, regex="^fixedquery$")
        # q: str = Query(..., min_length=3)
        # q: List[str] = Query(["foo", "bar"]),  # ?q=a&q=b
        q: list = Query(
            ["foo", "bar"],
            title="Query  ",
            alias="item-query",  # ?item-query=a
            description="Query string for the items to search in the database that have a good match",
            deprecated=True,  # 标记即将弃用
        ),
        limit: Optional[int] = None
):  # 请求参数如果不指定默认值,则必须输入
    print()
    if name == ModelName.alexnet:
        return {"name": name, "message": "Deep Learning FTW!", 'q': q}
    if name == ModelName.resnet:
        return {"name": name, "message": "LeCNN all the images", 'q': q}
    return {"name": name, "message": "Have some residuals", 'q': q}


class CarItem(BaseModel):
    description: str
    type: str


# 响应将是两种类型中的任何一种
@router.get("/item2s/{item_id}", response_model=Union[CarItem, Item])
async def get_item(
        item_id: str,
        # repeat_at: time = Body(None),  # 不再是请求参数;而是请求体参数
        item: Item = Body(..., embed=False),  # True将item在包装一层{item：{}}
        # response_model_include={"name", "description"},
        # response_model_exclude=["tax"],
        response_description="=========="
):
    """
    asd
    -   :param item_id:
    -   **:param** response_description:
    -   :return:
       Create an item with all the information:
    """
    return jsonable_encoder(item)


# @router.get('/render', status_code=200, tags=['item'])
# @router.get('/render', status_code=200, tags=['item'], response_class=HTMLResponse)
@router.get('/render', status_code=200, tags=['item'], response_class=ORJSONResponse)
async def render(request: Request):
    # return templates.TemplateResponse('index.html', {'request': request})
    data = """<?xml version="1.0"?>
    <shampoo>
    <Header>
        Apply shampoo here.
    </Header>
    <Body>
        You'll have to use soap here.
    </Body>
    </shampoo>
    """
    # return Response(content=data, media_type="application/xml")
    # return data
    # return RedirectResponse("https://typer.tiangolo.com")
    # return [{"item_id": "Foo"}]
    # return FileResponse("large-video-file.mp4")
    return StreamingResponse(fake_video_streamer(), media_type="video/mp4")


async def fake_video_streamer():
    return open('./123.txt', mode="rb")


@router.post('/files/', status_code=status.HTTP_202_ACCEPTED, tags=['item'])
async def user(username: str = Form(..., media_type="application/x-www-form-urlencoded"),
               file_list: List[bytes] = File(...),
               file_name: List[UploadFile] = File(...),
               token: str = Depends(oauth2_scheme)
               ):
    for item in file_list:
        print(len(item))
    for item in file_name:
        print(item.filename)

        contents = await item.read()
    return {"ok": 1}


def query_extractor():
    return 123


async def query_or_cookie_extractor(
        q: int = Depends(query_extractor), last_query: str = Cookie(None)
):
    if q != 123:
        raise HTTPException(status_code=400, detail="X-Token header invalid")
    return q


@router.get("/xx/")
async def read_query(query_or_default: str = Depends(query_or_cookie_extractor)):
    return {"q_or_cookie": query_or_default}
