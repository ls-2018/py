from datetime import datetime, timedelta
import jwt
from fastapi import Depends, HTTPException, Security
from fastapi.security import OAuth2PasswordBearer, SecurityScopes
from passlib.context import CryptContext
from starlette import status

from core.config import settings
from schemas import User, TokenData

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/token', scopes={
    "me": "Read information about the current user.",
    "items": "Read items."
})


async def get_current_user(
          token: str = Depends(oauth2_scheme)
):
    """
    需要授权
    :param token:
    :return:
    """
    # if security_scopes.scopes:
    #     authenticate_value = f'Bearer scope="{security_scopes.scope_str}"'
    # else:
    #     authenticate_value = f"Bearer"
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "authenticate_value"},
    )
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        username: str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_scopes = payload.get("scopes", [])
        token_data = TokenData(scopes=token_scopes, username=username)
    except (jwt.PyJWTError, jwt.InvalidTokenError):
        raise credentials_exception
    user = User(username=username,)
    # if user is None:
    #     raise credentials_exception
    # for scope in security_scopes.scopes:
    #     if scope not in token_data.scopes:
    #         raise HTTPException(
    #             status_code=status.HTTP_401_UNAUTHORIZED,
    #             detail="Not enough permissions",
    #             headers={"WWW-Authenticate": authenticate_value},
    #         )
    return user


# async def get_current_active_user(
#         current_user: User = Security(get_current_user, scopes=["me"])
# ):
#     if current_user.disabled:
#         raise HTTPException(status_code=400, detail="Inactive user")
#     return current_user


def create_access_token(data: dict, expires_delta: timedelta = None) -> str:
    """jwt"""
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(
            minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES
        )
    to_encode.update({'exp': expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    验证密码
    :param plain_password: 明文密码
    :param hashed_password: 密文密码
    :return:
    """
    return pwd_context.verify(plain_password, hashed_password)


def generate_hash_password(plain_password: str) -> str:
    """
    生成密文密码
    :param plain_password: 明文密码
    :return:
    """
    return pwd_context.hash(plain_password)
