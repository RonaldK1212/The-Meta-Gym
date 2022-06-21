from write_csv import create_filename, save_data, read_serial, header, path
import datetime
import sqlite3
import pathlib
try:
    from scan_card import scan_card
except:
    print("No card scanner available.")
    user_id = input("Input user ID: ")
else: 
    user_id = scan_card()



db_path = path / '..' / 'meta_gym.db'

con = sqlite3.connect(db_path)
cur = con.cursor()

date = datetime.datetime.now()  #gets current date
datestring = date.strftime("%y%m%d%H%M%S")  #formats date
filename = create_filename(user_id, datestring)

cur.execute("INSERT INTO sessions VALUES (?,?,?)", (filename, user_id, date))
con.commit()
con.close()

save_data(filename, header)