from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import pathlib

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


path = pathlib.Path(__file__).parent.absolute()
print("Path = ",path)
image_path = path / '..' / 'assets' / 'registration_bg.png'
db_path = path / '..' / 'meta_gym.db'

#Setup
root = Tk()
frm = ttk.Frame(root, padding=10)
root.geometry("500x400")
root.title("Registration")
root.resizable(width=False, height=False)
bg = PhotoImage(file=image_path)
background = ttk.Label(root, image=bg)
background.place(x=-2,y=-2)

user_id = None
first_name = None
last_name = None
email = None
phone = None
sex = None
dob = None
weight = None

label_font = ("Roboto", 12)

user_id_data =  ttk.Label(root, text= "", font = label_font, background="#ffc815")

#Components created here
first_name_field = ttk.Entry()
last_name_field = ttk.Entry()
email_field = ttk.Entry()
phone_field = ttk.Entry()
dob_field = ttk.Entry()
weight_field = ttk.Entry()
sex_input = IntVar()
male = Radiobutton(root, text="Male", variable=sex_input, value=1) 
female = Radiobutton(root, text="Female", variable=sex_input, value=2)
other = Radiobutton(root, text="Other", variable=sex_input, value=3)


#Functions defined here
def draw_decorations():
    style = ttk.Style()
    style.configure("BY.TLabel", background="#ffc815")
    title = ttk.Label(root, text="THE META-GYM USER REGISTRATION", font = ("Roboto", 18, "bold"), style="BY.TLabel")
    title.place(x = 250,y = 35, anchor = "center")

def draw_labels(x_pos, y_pos):
    user_id_label =  ttk.Label(root, text="ID ",     font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+7*30, anchor = "e")
    first_name_label =  ttk.Label(root, text="First Name*",     font = label_font, background="#ffc815").place(x = x_pos,y = y_pos, anchor = "e")
    last_name_label =   ttk.Label(root, text="Last Name*",      font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+30, anchor = "e")
    email_label =       ttk.Label(root, text="Email*",          font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+2*30, anchor = "e")
    phone_label =       ttk.Label(root, text="Phone Number",    font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+3*30, anchor = "e")
    sex_label =         ttk.Label(root, text="Sex*",            font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+4*30, anchor = "e")
    dob_label =         ttk.Label(root, text="Date of Birth*",  font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+5*30, anchor = "e")
    weight_label =      ttk.Label(root, text="Weight",          font = label_font, background="#ffc815").place(x = x_pos,y = y_pos+6*30, anchor = "e")
    user_id_data.place(x = x_pos,y = y_pos+7*30, anchor = "w")


def draw_input_boxes(x_pos, y_pos, width):
    first_name_field.place(x = x_pos,y = y_pos ,width=width,anchor = "w")
    last_name_field.place(x = x_pos,y = y_pos+30 ,width=width,anchor = "w")
    email_field.place(x = x_pos,y = y_pos+2*30 ,width=width,anchor = "w")
    phone_field.place(x = x_pos,y = y_pos+3*30 ,width=width,anchor = "w")
    male.config(bg="#ffc815")
    male.place(x= x_pos+15,y=y_pos+4*30, anchor = "w")
    female.config(bg="#ffc815")
    female.place(x= x_pos+85,y=y_pos+4*30, anchor = "w")
    other.config(bg="#292929", fg = "#ffc815")
    other.place(x= x_pos+165,y=y_pos+4*30, anchor = "w")
    dob_field.insert(0,"YYYY-MM-DD")
    dob_field.place(x = x_pos,y = y_pos+5*30 ,width=width,anchor = "w")
    weight_field.place(x = x_pos,y = y_pos+6*30 ,width=width,anchor = "w")
    
    

def draw_buttons(x_pos, y_pos):
    save_info = Button(root, text = "Save Info", command = data_verification)
    clear_fields = Button(root, text = "Clear Fields", command = clear_text)
    save_info.place(x = x_pos, y = y_pos)
    clear_fields.place(x = x_pos + 100, y = y_pos)

def scan_card():
    if messagebox.askokcancel(title="Card Scanner", message= "Press OK to start scanning for card."):
        #WRITE CARD SCAN CODE 
        global user_id
        user_id_data.config(text = "")
    #    user_id = input("Enter used ID to simulate card swipe: ")
        user_id = reader.read()[0]
        user_id_data.config(text = user_id)
    else:
        quit()

def fetch_data():
    global user_id, first_name, last_name, email, phone, sex, dob, weight
    first_name = first_name_field.get()
    last_name = last_name_field.get()
    email = email_field.get()
    phone = phone_field.get()
    if (sex_input.get() == 1):
        sex = 'M'
    elif (sex_input.get() == 2):
        sex = 'F'
    else: sex = 'X'
    dob = dob_field.get()
    weight = weight_field.get()

def clear_text():
   first_name_field.delete(0, END)
   last_name_field.delete(0, END)
   email_field.delete(0, END)
   phone_field.delete(0, END)
   weight_field.delete(0, END)
   dob_field.delete(0, END)
   sex_input.set(0)
   scan_card()

def store_in_database():
    global user_id, first_name, last_name, email, phone, sex, dob, weight
    fetch_data()
    try: 
        con = sqlite3.connect(db_path)
    except: 
        print("Database connection failed")
    else:
        print("Connected to database successfully")
        cur = con.cursor()
        dor = datetime.today().strftime('%Y/%m/%d') 
        cur.execute("INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,NULL,NULL,NULL)", (user_id, dor, first_name, last_name, email, phone, sex, dob, weight))
        con.commit()
        con.close()
        messagebox.showinfo(title="Registered", message="You have registered successfully!")
        clear_text()
    
    

def data_verification():
    global user_id, first_name, last_name, email, phone, sex, dob, weight
    fetch_data()
    if not (user_id == "" or first_name == "" or last_name == "" or email == "" or sex == 0 or dob == ""):
        store_in_database()
#Interface created here
def main():
    draw_decorations()
    draw_labels(130, 100)
    draw_input_boxes(155, 100, 300)
    draw_buttons(150, 320)
    scan_card()
    root.mainloop()
    
    
main()