import sqlite3
import pathlib

path = pathlib.Path(__file__).parent.absolute()
db_path = path / '..' / 'meta_gym.db'

try:
    con = sqlite3.connect(db_path)
except:
    print("Database connection failed.")

cur = con.cursor()


class get:
    def firstName(user_id):
        cur.execute("SELECT First_Name FROM users WHERE id= ?", (user_id,))
        (data) = cur.fetchall()[0][0]
        return data
    def lastName(user_id):
        cur.execute("SELECT Last_Name FROM users WHERE id= ?", (user_id,))
        data = cur.fetchall()[0][0]
        return data
    def fullName(user_id):
        data = get.firstName(user_id) + ' ' + get.lastName(user_id)
        return data
    def phone(user_id):
        cur.execute("SELECT Phone_Number FROM users WHERE id= ?", (user_id,))
        data = cur.fetchall()[0][0]
        return data
    def email(user_id):
        cur.execute("SELECT Email FROM users WHERE id= ?", (user_id,))
        data = cur.fetchall()[0][0]
        return data
    def all(user_id):
        data = None
        cur.execute("SELECT * FROM users WHERE id= ?", (user_id,))
        data = cur.fetchall()[0]
        return data