from pydantic import BaseModel
from fastapi import Form
from typing import Annotated


class SignInForm(BaseModel):
    username: Annotated[str, Form()]
    password: Annotated[str, Form()]
