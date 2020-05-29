from typing import List, Optional, Any
import peewee
from pydantic import BaseModel
from pydantic.utils import GetterDict


class PeeweeGetterDict(GetterDict):
    def get(self, key: Any, default: Any = None):
        res = getattr(self._obj, key, default)
        if isinstance(res, peewee.ModelSelect):
            return list(res)
        return res


class Item(BaseModel):
    id: int
    owner_id: int
    title: str
    description: str = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class User(BaseModel):
    username: str
    password: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None

    class Config:
        orm_mode = True
        getter_dict = PeeweeGetterDict


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    username: str = None
    scopes: List[str] = []
