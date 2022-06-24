def scan_card_f():
    import time
    card_id = None
    print("Card scanner initiated")
    try:
        import RPi.GPIO as GPIO
        from mfrc522 import SimpleMFRC522
        reader = SimpleMFRC522()
        card_id = reader.read()[0]
    except:
        card_id = '999888777'
    finally:
        if card_id:
            time.sleep(0.1)
            print("Card scanned with ID: ", card_id)
            return card_id
        else:
            time.sleep(0.1)
            
def register_user(user_data): #adds user to database
    #TODO: get user data as tuple and export it to database as tuple    
    import sqlite3 as sql
    import pathlib 
    con = db()
    con.cursor().execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,NULL,NULL,NULL)', user_data)
    con.commit()
    con.close()

def db():   #connects to database
    import sqlite3 as sql
    import pathlib
    path = pathlib.Path(__file__).parent.absolute()
    #print("Path = ",path)
    db_path = path / 'meta_gym.db'
    print('Database path: ' + str(db_path))
    con = sql.connect(db_path)
    return con

def getUserData(user_id): #gets user information 
    import sqlite3 as sql
    data = []
    con = db()
    cur = con.cursor()
    user_id_int = int(user_id)
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id_int,))
    print(["Get user data (ID): ", user_id_int])
    data_tuple = cur.fetchall()
    for _ in data_tuple:
        data.append(_)
    return data

def getUserWorkouts(user_id): #gets list of ALL workouts
    import sqlite3 as sql
    import pathlib
    con = db()
    cur = con.cursor()
    cur.execute("SELECT filename,timestamp FROM sessions WHERE user_id = ?", (user_id,))
    data = cur.fetchall()
    return data

def getWorkout(user_id, workout_id): #gets data of a SINGLE workout
    import pandas as pd
    filename = getUserWorkouts(user_id)[0] #gets workout *.csv filename
    data = pd.read_csv(str(filename + '.csv')) #gets workout data from file
    return data