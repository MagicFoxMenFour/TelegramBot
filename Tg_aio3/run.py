from aiogram import Bot, Dispatcher
from config import TOKEN
from app.handlers import router
import logging
import sys
import asyncio

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()   
    dp.include_router(router)
    await dp.start_polling(bot)
    
    
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
        