from enum import Enum
from typing import List, Dict, Set, Tuple, Optional
from fastapi import FastAPI, Query, Path, Body, Cookie
from pydantic import BaseModel, Field, HttpUrl
from uuid import UUID
from datetime import datetime, time, timedelta

app = FastAPI()


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


class ModelName(str, Enum):
    alexnet = "1"
    resnet = "2"


@app.get("/")
async def read_root(a: str = Cookie(None)):  # 从Cookie中读取参数a
    return {"Hello": a}


@app.get("/items/{name:str}")
async def read_item(
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

    if name == ModelName.alexnet:
        return {"name": name, "message": "Deep Learning FTW!", 'q': q}
    if name == ModelName.resnet:
        return {"name": name, "message": "LeCNN all the images", 'q': q}
    return {"name": name, "message": "Have some residuals", 'q': q}


@app.put("/items/{item_id}")
async def update_item(
        item_id: UUID,
        repeat_at: time = Body(None),
        item: Item = Body(..., embed=False)
):  # True将item在包装一层{item：{}}
    return {
        "item_name": item.name,
        "repeat_at": repeat_at,
        "item_id": item_id
    }

# uvicorn main:app --reload
