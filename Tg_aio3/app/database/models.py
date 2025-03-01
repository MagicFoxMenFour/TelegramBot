from sqlalchemy import BigInteger, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import AsyncAttrs, async_sessionmaker, create_async_engine
from config import SQLALCHEMY_URL

engine = create_async_engine(SQLALCHEMY_URL, echo = True)

async_sessionmaker = async_sessionmaker(engine)

class Base(AsyncAttrs, DeclarativeBase):
    pass

class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger)


class Category(Base):
    __tablename__ = 'categories'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    
    product = relationship('Product', back_populates='category')
    
class Product(Base):
    __tablename__ = 'products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column()
    description: Mapped[str] = mapped_column()
    price: Mapped[int] = mapped_column()
    category_id: Mapped[int] = mapped_column(ForeignKey('categories.id'))
    
    category = relationship('Category', back_populates='products')
    
    
async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
        

