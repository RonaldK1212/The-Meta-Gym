import matplotlib.pyplot as plt
import datetime
import sqlite3
import pathlib
import pandas as pd
try:
    from scan_card import scan_card
except:
    print("No card scanner available.")
    user_id = input("Input user ID: ")
else: 
    user_id = scan_card()

path = pathlib.Path(__file__).parent.absolute()
print("Path = ",path)
db_path = path / '..' / 'meta_gym.db'
logs_file = path / '..' / 'Sensor Logs'

con = sqlite3.connect(db_path)
cur = con.cursor()




cur.execute('SELECT filename,timestamp FROM sessions WHERE user_id = ?', (user_id,))
data = cur.fetchall()
print("Your ID: ", user_id)
i = 1
for row in data:
    print( "Session ", i, " date: ", row[1])
    i+=1

selected_session = input("Select session number to view: ")

log_path = logs_file / data[int(selected_session)-1][0]
print("Log Path: ", log_path)

dataFile = pd.read_csv(log_path, usecols=["Voltage"])
print(dataFile)
dataFile.plot()

plt.show()