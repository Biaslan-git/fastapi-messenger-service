from pydantic import BaseModel
from uuid import UUID

class User(BaseModel):
    username: str

class UserInDB(BaseModel):
    id: UUID
    username: str
    # hashed_password: str
    telegram_id: str | None = None

class UserCreateForm(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str
