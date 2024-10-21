from fastapi import Depends, APIRouter, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from sqlalchemy.ext.asyncio import AsyncSession

from src.database import get_async_session
from src.auth.utils import create_access_token, decode_access_token
from src.auth.manager import insert_user, verify_user
from src.auth.schemas import Token, UserCreateForm

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@router.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends(), session: AsyncSession = Depends(get_async_session)):
    user = await verify_user(session, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token = create_access_token({'user': user.username})

    return Token(access_token=access_token, token_type="bearer")

@router.post('/create_user/', status_code=status.HTTP_201_CREATED)
async def create_user(user_data: UserCreateForm, session: AsyncSession = Depends(get_async_session)):
    result = await insert_user(session, user_data.username, user_data.password)
    return result or {'status': 'error'}

@router.get("/users/me/")
async def read_users_me(token: str = Depends(oauth2_scheme)):
    payload = decode_access_token(token)
    return payload

