import secrets

from fastapi import Depends, APIRouter
from fastapi.security import HTTPBasicCredentials, HTTPBasic

router = APIRouter()
security = HTTPBasic()


@router.get("/base/auth")
def create_user(credentials: HTTPBasicCredentials = Depends(security)):
    print(secrets.compare_digest(credentials.username, "stanleyjobson") == True)
    # 避免直接比较用户名和密码，由此导致的反应速度 可能会给攻击者  机会
    return {"username": credentials.username, "password": credentials.password}
