from fastapi import APIRouter, HTTPException, status
from fastapi.responses import JSONResponse
from jwt_manager import create_token
from schema.users import User

user_router = APIRouter()


@user_router.post('/login', tags=['Auth'])
def login(user: User):

    if user.email == 'vicflores11@gmail.com' and user.password == 'abc12345':
        token: str = create_token(user.model_dump())
        return JSONResponse(content={"token": token}, status_code=status.HTTP_200_OK)

    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")
