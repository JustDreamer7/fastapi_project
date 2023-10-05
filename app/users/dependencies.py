import datetime

import app.exceptions as exc
from fastapi import Request, Depends
from jose import jwt, JWTError
from app.config import settings
from app.users.models import Users
from app.users.repo import UsersRepo


def get_token(request:Request):
    token = request.cookies.get("booking_access_token")
    if not token:
        raise exc.AbsentTokenException
    return token

async def get_current_user(token: str = Depends(get_token)):
    try:
        test = jwt.decode(token, settings.SECRET_KEY, settings.ALGORITHM)
    except JWTError:
        raise exc.IncorrectTokenFormatException
    expire: str = test.get("exp")
    if not expire or int(expire) < datetime.datetime.utcnow().timestamp():
        raise exc.ExpiredTokenException
    user_id: str = test.get("sub")
    if not user_id:
        raise exc.UserIsNotPresentException
    user = await UsersRepo.find_by_id(int(user_id))
    if not user:
        raise exc.UserIsNotPresentException
    return user


async def get_current_admin_user(current_user: Users = Depends(get_current_user)):
    # if current_user.role != "admin":
    #     raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    return current_user