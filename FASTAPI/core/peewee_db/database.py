from contextvars import ContextVar

import peewee
from fastapi import Depends

DATABASE_NAME = "test.db"
db_state_default = {"closed": None, "conn": None, "ctx": None, "transactions": None}
db_state = ContextVar("db_state", default=db_state_default.copy())


class PeeweeConnectionState(peewee._ConnectionState):
    def __init__(self, **kwargs):
        super().__setattr__("_state", db_state)
        super().__init__(**kwargs)

    def __setattr__(self, name, value):
        self._state.get()[name] = value

    def __getattr__(self, name):
        return self._state.get()[name]


db = peewee.SqliteDatabase(DATABASE_NAME, check_same_thread=False)

db._state = PeeweeConnectionState()  # 检查peewee是否经过修改


# fastapi并没有赋予peewee异步能力
# 替换peewee内部使用的threading.local  ;并使用ContextVar
async def reset_db_state():
    db._state._state.set(db_state_default.copy())
    db._state.reset()  # 每个请求都是独立的


def get_db(db_state=Depends(reset_db_state)):
    try:
        db.connect()
        """
        这里没有直接使用数据库对象
        它将连接到数据库,并将连接存储到一个内部变量中,该变量对于每个请求都是独立的（contextVars)
        由于数据库链接可能会阻止IO,因此将使用常规def功能创建此依赖关系
        然后,在需要访问数据库的每个路径操作函数中,我们将其添加为依赖项
        
        """
        yield
    finally:
        if not db.is_closed():
            db.close()
