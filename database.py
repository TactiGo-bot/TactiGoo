import asyncpg
from config import DB_URL

async def connect_db():
    return await asyncpg.create_pool(DB_URL)
