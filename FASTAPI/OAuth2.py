from fastapi import Depends, FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from starlette import status
from passlib.context import CryptContext
from datetime import timedelta
from typing import Optional
import uvicorn
import datetime
import jwt
from jwt import exceptions

app = FastAPI()
SECRET_KEY = 'iv%x6xo7l7_u9bf_u!9#g#m*)*=ej@bek5)(@u3kh*72+unjv='
ALGORITHM = 'HS256'
ACCESS_TOKEN_EXPIRE_MINUTES = 1
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token')
pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

# 生命该URL是客户端应用于获取凌派的URL。该信息在OpenAPI中使用，然后在交互式API文档系统中使用。
# 该oauth2_scheme变量的一个实例OAuth2PasswordBearer 但它也是一个通知

fake_users_db = {
    'alice': {
        'username': 'alice',
        "full_name": "Alice Wonderson",
        "email": "alice@example.com",
        'hashed_password': "$2b$12$XeydVWRHSQxTcg0r2XWv4.1i7A916JYv/7WXKllLwRbrsV2jBa72a",
        'disabled': False  # 禁用
    }
}


class User(BaseModel):
    username: str
    email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None


class Token(BaseModel):
    access_token: str
    token_type: str


class AUTH:
    @staticmethod
    def verify_password(plain_password, hashed_password):
        """
        验证密码
        :param plain_password: 明文密码
        :param hashed_password: 密文密码
        :return:
        """
        return pwd_context.verify(plain_password, hashed_password)

    @staticmethod
    def generate_hash_password(plain_password):
        """
        生成密文密码
        :param plain_password: 明文密码
        :return:
        """
        return pwd_context.hash(plain_password)

    @staticmethod
    def create_access_token(data: dict, expire_delta: timedelta = None):
        to_encode = data.copy()
        expire = datetime.datetime.utcnow() + expire_delta  # 过期时间
        to_encode.update({'exp': expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt


@app.get('/item/')  # Authorization: Bearer
async def read_items(token: str = Depends(oauth2_scheme)):
    try:
        verified_payload = jwt.decode(token, SECRET_KEY, True)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token已失效')
    except jwt.DecodeError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token认证失败')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='非法的token')
    return verified_payload


@app.post('/token', response_model=Token)
async def auth2(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
    if form_data.username not in fake_users_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username')
    if AUTH.verify_password(form_data.password, fake_users_db[form_data.username]['hashed_password']):
        return {
            'access_token': AUTH.create_access_token(
                form_data.__dict__,
                expire_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            ),
            "token_type": 'bearer'
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid username or password')


if __name__ == '__main__':
    uvicorn.run(app='OAuth2:app', host='127.0.0.1', port=8000, reload=True)
