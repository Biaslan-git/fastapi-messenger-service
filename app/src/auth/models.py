from sqlalchemy import MetaData, Table, Column, String
from sqlalchemy.dialects.postgresql import UUID
import uuid

metadata = MetaData()

user_table = Table(
    'users', 
    metadata, 
    Column('id', UUID(as_uuid=True), primary_key=True, default=uuid.uuid4),
    Column('username', String, nullable=False, unique=True),
    Column('hashed_password', String, nullable=False),
    Column('telegram_id', String, nullable=True),
)
