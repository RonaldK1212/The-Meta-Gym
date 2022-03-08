import sqlite3
from datetime import datetime

con = sqlite3.connect('meta_gym.db')
cur = con.cursor()
print("Connected to The Meta-Gym Database")

#Creates the users table
cur.execute('CREATE TABLE IF NOT EXISTS users (\
    id integer PRIMARY KEY AUTOINCREMENT, \
    DOR date NOT NULL, \
    First_Name text NOT NULL, \
    Last_Name text NOT NULL, \
    Email text UNIQUE, \
    Phone_Number text UNIQUE, \
    Sex tinyint NOT NULL,\
    DOB date NOT NULL, \
    Weight real, \
    Calories_Burned integer, \
    Energy_Generated integer, \
    Points integer)')

#Creates the records table
cur.execute('CREATE TABLE records (id integer, \
Top_Speed real, \
Longest_Time time, \
Max_Energy_In_Single_Session integer, \
Max_Instantaneous_Power real, \
FOREIGN KEY (id) REFERENCES users(id))')

#User inputs their data through the terminal
x = False
while x:
    dor = datetime.today().strftime('%Y/%m/%d')
    email = input("Enter your Email: ")
    phone = input("Enter your Phone number: ")
    first_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    sex = input("Enter your sex (0 other - 1 male - 2 female - 9 not applicable: ")
    dob = input("Enter your date of birth: ")
    weight = input("Enter your weight: ")
    cur.execute("INSERT INTO users VALUES (NULL,?,?,?,?,?,?,?,?,NULL,NULL,NULL)", (dor,first_name,last_name,email,phone,sex,dob,weight))
    x = False






con.commit()
con.close()