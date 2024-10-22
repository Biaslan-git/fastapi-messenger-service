from fastapi import APIRouter, Depends, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from typing import Annotated

from src.auth.router import login

router = APIRouter(
    prefix='/pages',
    tags=['Pages']
)

templates = Jinja2Templates(directory='src/templates')

@router.get('/signin')
def get_signin_page(request: Request):
    return templates.TemplateResponse('signin.html', {'request': request})

@router.post('/signin')
def signin(
    request: Request,
    username: Annotated[str, Form()],
    password: Annotated[str, Form()],
    token= Depends(login)
):
    return

@router.get('/users')
async def get_users_page(request: Request):
    return templates.TemplateResponse('users.html', {'request': request})
