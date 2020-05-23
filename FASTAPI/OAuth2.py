from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status
from typing import Optional
import uvicorn

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')

# 生命该URL是客户端应用于获取凌派的URL。该信息在OpenAPI中使用，然后在交互式API文档系统中使用。
# 该oauth2_scheme变量的一个实例OAuth2PasswordBearer 但它也是一个通知

fake_users_db = {
    'alice': {
        'username': 'alice',
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        'hashed_password': "fakehashsecert",
        'disabled': False  # 禁用
    }
}


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


@app.get('/item/')  # Authorization: Bearer
async def read_items(token: str = Depends(oauth2_scheme)):
    print("token", token)
    if token in fake_users_db:
        return User(**fake_users_db[token])
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='over time ')


@app.post('/token')
async def auth2(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
    if form_data.username not in fake_users_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username')
    return {'access_token': form_data.username, "token_type": 'bearer'}


if __name__ == '__main__':
    uvicorn.run(app='OAuth2:app', host='127.0.0.1', port=8000, reload=True)
