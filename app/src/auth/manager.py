from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from src.auth.models import user_table
from src.auth.schemas import UserInDB
from src.auth.utils import hash_password, verify_password


async def get_user(session: AsyncSession, username) -> UserInDB | None:
    query = select(user_table).where(user_table.c.username == username)
    result = await session.execute(query)
    user = result.first()
    if user:
        return UserInDB(id=user.id, username=user.username, telegram_id=user.telegram_id)

async def insert_user(session: AsyncSession, username, password):
    user = await get_user(session, username)
    if not user:
        hashed_password = hash_password(password)
        stmt = insert(user_table).values(username=username, hashed_password=hashed_password)
        await session.execute(stmt)
        await session.commit()
        return {'status': 'success'}

async def verify_user(session: AsyncSession, username, password) -> UserInDB | None:
    query = select(user_table).where(user_table.c.username == username)
    result = await session.execute(query)
    user = result.first()
    if user and verify_password(password, user.hashed_password):
        return UserInDB(id=user.id, username=user.username, telegram_id=user.telegram_id)

    
