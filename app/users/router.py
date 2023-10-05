from fastapi import APIRouter, Response, Depends
import app.exceptions as exc
from app.users.dependencies import get_current_user, get_current_admin_user
from app.users.models import Users
from app.users.schemas import SUserAuth
from app.users.repo import UsersRepo
from app.users.auth import get_password_hash, authenticate_user, create_access_token

router = APIRouter(
    prefix='/auth',
    tags=['Auth & пользователи']
)


@router.post('/register')
async def register_user(user_data: SUserAuth):
    existing_user = await UsersRepo.find_one_or_none(email=user_data.email)
    if existing_user:
        raise exc.UserAlreadyExistsException
    hashed_password = get_password_hash(user_data.password)
    await UsersRepo.add(email=user_data.email, hashed_password=hashed_password)


@router.post('/login')
async def login_user(response: Response, user_data: SUserAuth):
    user = await authenticate_user(user_data.email, user_data.password)

    access_token = create_access_token({"sub": str(user.id)})
    response.set_cookie("booking_access_token", access_token, httponly=True)
    # можно заполнить поле expire для того, чтобы он сам удалил куки
    return access_token


@router.post('/logout')
async def logout_user(response: Response):
    response.delete_cookie("booking_access_token")


@router.get('/me')
async def return_user_data(current_user: Users = Depends(get_current_user)):
    return current_user

@router.get("/all")
async def return_all_users_data(current_user: Users = Depends(get_current_admin_user)):
    return await UsersRepo.find_all()