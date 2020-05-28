from fastapi import Depends, HTTPException
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordRequestForm
from starlette import status
from typing import Optional
from core.security import *
from core.config import settings
import jwt
from fastapi import APIRouter

from core.security import oauth2_scheme

router = APIRouter()

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


async def get_current_user(token: str = Depends(oauth2_scheme)):
    """
    需要授权
    :param token:
    :return:
    """
    try:
        verified_payload = jwt.decode(token, settings.SECRET_KEY, True)
    except jwt.exceptions.ExpiredSignatureError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='token已失效')
    except jwt.DecodeError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid authentication credentials",
            headers={"WWW-Authenticate": "Bearer"}
        )
    except jwt.InvalidTokenError:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail='非法的token',
            headers={
                'X-Error': 'There goes my error'
            }
        )

    return verified_payload


# @router.put('/item/', tags=['oauth2'], dependencies=[Depends(get_current_user)])  # Authorization: Bearer
@router.put('/item/', tags=['oauth2'])  # Authorization: Bearer
async def read_items(current_user: User = Depends(get_current_user)):
    return current_user


@router.post(
    '/token',
    response_model=Token,
    response_model_exclude_unset=True,
    tags=['oauth2'],
    summary='Generate a token',
    description='-----------------'
)
async def auth2(form_data: OAuth2PasswordRequestForm = Depends(OAuth2PasswordRequestForm)):
    if form_data.username not in fake_users_db:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Incorrect username')
    if verify_password(form_data.password, fake_users_db[form_data.username]['hashed_password']):
        return {
            'access_token': create_access_token(
                form_data.__dict__
            ),
            "token_type": 'bearer'
        }
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='invalid username or password')
