from typing import Optional
from fastapi import HTTPException, status


class BookingException(HTTPException):
    status_code = 500
    detail = ""

    def __init__(self, detail: Optional[str]=None):
        super().__init__(status_code=self.status_code, detail=detail or self.detail)


class UserAlreadyExistsException(BookingException):
    status_code = status.HTTP_409_CONFLICT
    detail = "Пользователь уже существует"

class IncorrectEmailOrPasswordException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверная почта или пароль"

class ExpiredTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен истек"

class AbsentTokenException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Токен отсутствует"

class IncorrectTokenFormatException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = "Неверный формат токена"

class UserIsNotPresentException(BookingException):
    status_code = status.HTTP_401_UNAUTHORIZED
    detail = ""

