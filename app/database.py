import sqlite3 as sq


db = sq.connect('tg.db')
cur = db.cursor()


async def db_start():
    cur.execute('CREATE TABLE IF NOT EXISTS accounts( '
                'id INTEGER PRIMARY KEY AUTOINCREMENT, '
                'tg_id INTEGER, '
                'card_id TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS items('
                'i_id INTEGER PRIMARY KEY AUTOINCREMENT,'
                'name TEXT, '
                'desc TEXT, '
                'price TEXT, '
                'photo TEXT, '
                'brand TEXT)')
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute('SELECT * FROM accounts WHERE tg_id == {key}'.format(key=user_id)).fetchone()
    if not user:
        cur.execute('INSERT INTO accounts (tg_id) VALUES ({key})'.format(key=user_id))
        db.commit()


async def add_item(state):
    async with state.proxy() as data:
        cur.execute('INSERT INTO items (name, desc, price, photo, brand) VALUES (?, ?, ?, ?, ?)',
                    (data['name'], data['desc'], data['price'], data['photo'], data ['type']))
        db.commit()
