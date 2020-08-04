import sqlite3

connect = sqlite3.connect('sochi_athletes.sqlite3')
cur = connect.cursor()
cur.execute("""DROP TABLE IF EXISTS user;""")
connect.commit()

b = input('Данные удалены')
