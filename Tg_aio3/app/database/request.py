from app.database.models import User, Category, Product, async_session
from sqlalchemy import select


async def get_catefories():
    async with async_session() as session:
        result = await session.scalars(select(Category))
        return result   