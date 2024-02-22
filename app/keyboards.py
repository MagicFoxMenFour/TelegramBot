from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(resize_keyboard=True)
main.add('Каталог').add('Корзина').add('Контакты')


main_admin = ReplyKeyboardMarkup(resize_keyboard=True)
main_admin.add('Каталог').add('Корзина').add('Контакты').add('Админ-панель')

admin_panel = ReplyKeyboardMarkup(resize_keyboard=True)
admin_panel.add('Добавить товар').add('Удалить товар').add('Сделать рассылку')


catalog_list = InlineKeyboardMarkup(row_width=2)
catalog_list.add(InlineKeyboardButton(text='Платья', callback_data='t-shirt'), 
                 InlineKeyboardButton(text='Юбки', callback_data='shorts'), 
                 InlineKeyboardButton(text='Туфли', callback_data='sneakers'))

cancel = ReplyKeyboardMarkup(resize_keyboard=True)
cancel.add('Отмена')