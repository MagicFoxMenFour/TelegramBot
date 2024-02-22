import telebot
from telebot import types
import webbrowser
import sqlite3
import requests
import json

bot = telebot.TeleBot('6717675534:AAFYQZGExqasV-psZMgngVCURiPswrqwxyI')
API = '6e8861c425ce28c68889a95b2731aa46'

name = None

@bot.message_handler(commands=['site', 'website'])
def site(message):
    webbrowser.open('https://umo-gta5rp.com/')

@bot.message_handler(commands=['start', 'main', 'hello'])
def main(message):
    conn = sqlite3.connect('mfmf.sql')
    cur = conn.cursor()

    cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), pass varchar(50))')
    conn.commit()
    cur.close()
    conn.close()

    bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    bot.register_next_step_handler(message, user_name)
    markup = types.ReplyKeyboardMarkup()

def user_name(message):
    global name
    name = message.text.strip()
    bot.send_message(message.chat.id, f'Введите пароль')
    bot.register_next_step_handler(message, user_pass)

def user_pass(message):
    password = message.text.strip()
    conn = sqlite3.connect('mfmf.sql')
    cur = conn.cursor()

    cur.execute('INSERT INTO users (name, pass) VALUES ("%s", "%s")' % (name, password))
    conn.commit()
    cur.close()
    conn.close()

    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton('Список пользователей', callback_data='users'))
    bot.send_message(message.chat.id, 'Пользователь зарегистрирован', reply_markup=markup)

@bot.callback_query_handler(func=lambda call:True)
def callback(call):
    conn = sqlite3.connect('mfmf.sql')
    cur = conn.cursor()

    cur.execute('SELECT * FROM users')
    users = cur.fetchall()

    info = ''           
    for el in users:
        info += f'Имя: {el[1]}, пароль: {el[2]}\n'

    cur.close()
    conn.close()

    bot.send_message(call.message.chat.id, info)

@bot.message_handler(commands=['help'])
def main(message):
    bot.send_message(message.chat.id, '<b>Существующие</b> <em><u>команды</u></em>', parse_mode='html')


@bot.message_handler(content_types=['text'])
def get_weather(message):
    city = message.text.strip().lower()

    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    data = json.loads(res.text)
    temp = data['main']['temp']
    bot.reply_to(message, f'Сейчас погода: {temp}')


@bot.message_handler(content_types=['photo'])
def get_photo(message):
    markup = types.InlineKeyboardMarkup()
    markup.add(types.InlineKeyboardButton('Перейти на сайт', url='https://umo-gta5rp.com/'))
    markup.add(types.InlineKeyboardButton('Удалить', callback_data='delete'))
    markup.add(types.InlineKeyboardButton('Изменить текст', callback_data='edit'))
    bot.reply_to(message, 'Какое красивое фото', reply_markup=markup)

@bot.callback_query_handler(func = lambda callback: True)
def callback_message(callback):
    if callback.data == 'delete':
        bot.delete_message(callback.message.chat.id, callback.message.message_id - 1)
    elif callback.data == 'edit':
        bot.edit_message_text('Edit text', callback.message.chat.id, callback.message.message_id)

@bot.message_handler()
def info(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.chat.id, f'Привет {message.from_user.first_name} {message.from_user.last_name}')
    elif message.text.lower() == 'id':
        bot.reply_to(message, f'ID: {message.from_user.id}')

bot.polling(none_stop=True)