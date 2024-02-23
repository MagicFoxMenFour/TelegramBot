from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from app.database.request import get_catefories

main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Каталог')],
    [KeyboardButton(text='Контакты')]
    ])

async def categories():
    
    categories = await get_catefories()
    for category in categories:
        