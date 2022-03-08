from lib2to3.pgen2.token import EQUAL
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import pathlib
import pathlib

from numpy import equal

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
reader = SimpleMFRC522()


path = pathlib.Path(__file__).parent.absolute()
print("Path = ",path)
image_path = path / '..' / 'assets' / 'login_bg.png'
db_path = path / 'meta_gym.db'

#Setup
root = Tk()
frm = ttk.Frame(root, padding=10)
x_size = 500
y_size = 500
dimensions = str("%sx%s" % (x_size,y_size))
root.geometry(dimensions)
root.title("Login")
root.resizable(width=False, height=False)
bg = PhotoImage(file=image_path)
background = ttk.Label(root, image=bg)
background.place(x=-2,y=-2)

label_font = ("Roboto", 12)
user_id_label =  ttk.Label(root,     font = label_font)
first_name_data =  ttk.Label(root,     font = label_font)
last_name_data =  ttk.Label(root,    font = label_font)
phone_data =       ttk.Label(root,    font = label_font)
sex_data =         ttk.Label(root,           font = label_font)
dob_data =         ttk.Label(root,  font = label_font)
weight_data =      ttk.Label(root,          font = label_font)
dor_data =         ttk.Label(root, font = label_font)

login_data = None
login_method = IntVar()
using_card = None
card_id = None
user_id = None
dor = None
first_name = None
last_name = None
email = None
phone_number = None
sex = None
dob = None
weight = None
calories_burned = None
energy_generated = None
points = None
login_info_field = None


def draw_decorations():
    style = ttk.Style()
    style.configure("BY.TLabel", background = "#292929", foreground = "#ffc815")
    title = ttk.Label(root, text="THE META-GYM USER LOGIN", font = ("Roboto", 18, "bold"), style="BY.TLabel")
    title.place(x = 250,y = 35, anchor = "center")
    print("Decorations generated")

def draw_labels(x_pos, y_pos):
    label_font = ("Roboto", 12, "bold")
    user_id_label =  ttk.Label(root, text="ID: ",     font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos+250,y = y_pos+4*30, anchor = "e")
    first_name_label =  ttk.Label(root, text="First Name: ",     font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos,y = y_pos, anchor = "e")
    last_name_label =   ttk.Label(root, text="Last Name: ",      font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos,y = y_pos+30, anchor = "e")
    phone_label =       ttk.Label(root, text="Phone Number: ",    font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos+250,y = y_pos, anchor = "e")
    sex_label =         ttk.Label(root, text="Sex: ",            font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos,y = y_pos+2*30, anchor = "e")
    dob_label =         ttk.Label(root, text="Date of Birth: ",  font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos+250,y = y_pos+30, anchor = "e")
    weight_label =      ttk.Label(root, text="Weight: ",          font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos+250,y = y_pos+2*30, anchor = "e")
    dor_label =         ttk.Label(root, text="Date of \nRegistration: ", font = label_font, background="#292929", foreground = "#ffc815").place(x = x_pos, y = y_pos+4*30, anchor = "e")
    print("Labels generated")

def draw_data(x_pos,y_pos):
    global user_id_label, first_name_data, last_name_data, phone_data,sex_data,dob_data,weight_data,dor_data
    
    user_id_label.place(x = x_pos+250,y = y_pos+4*30, anchor = "w")
    first_name_data.place(x = x_pos,y = y_pos, anchor = "w")
    last_name_data.place(x = x_pos,y = y_pos+30, anchor = "w")
    phone_data.place(x = x_pos+250,y = y_pos, anchor = "w")
    sex_data.place(x = x_pos,y = y_pos+2*30, anchor = "w")
    dob_data.place(x = x_pos+250,y = y_pos+30, anchor = "w")
    weight_data.place(x = x_pos+250,y = y_pos+2*30, anchor = "w")
    dor_data.place(x = x_pos, y = y_pos+130, anchor = "w")

    user_id_label.config(text = user_id, background="#292929", foreground = "#ffc815")
    first_name_data.config(text=first_name, background="#292929", foreground = "#ffc815")
    last_name_data.config(text=last_name, background="#292929", foreground = "#ffc815")
    phone_data.config(text = phone_number, background="#292929", foreground = "#ffc815")
    sex_data.config(text = sex, background="#292929", foreground = "#ffc815")
    dob_data.config(text = dob, background="#292929", foreground = "#ffc815")
    weight_data.config(text = weight, background="#292929", foreground = "#ffc815")
    dor_data.config(text = dor, background="#292929", foreground = "#ffc815")
    print("Data displayed")

def scan_card():
    print("Card scanner initiated")
    global using_card, login_data, card_id
    if messagebox.askokcancel(title="Card Scanner", message= "Press OK to start scanning for card."):
        #WRITE CARD SCAN CODE 
        user_id_label.config(text = "")
     #   card_id = input("Enter used ID to simulate card swipe: ")
        card_id = reader.read()[0]
        user_id_label.config(text = card_id)
    else:
        quit()
    print("Card Scanned:", card_id)

    

def draw_login_form(x_pos, y_pos):
    global login_info_field
    if not login_info_field  == None:
        login_info_field.destroy()
    login_info_field = ttk.Entry()
    login_info_field.place(x = x_pos,y = y_pos ,width=300, anchor = "center")
    print("Login form generated")

def choose_login_method():
    login_method_menu = Menubutton(root, text = "Choose a login method")
    login_method_menu.menu = Menu(login_method_menu)
    login_method_menu["menu"] = login_method_menu.menu
    login_method_menu.menu.add_radiobutton(label = "Email", variable = login_method, value = 0, command=get_user)
    login_method_menu.menu.add_radiobutton(label = "Phone", variable = login_method, value = 1, command=get_user)
    login_method_menu.menu.add_radiobutton(label = "Card", variable = login_method, value = 2, command=get_user)
    login_method_menu.place(x = x_size/2, y = (y_size/2)+30, anchor="center")

def get_user():
    global login_info_field
    if (login_method.get() == 2):
        if not login_info_field  == None:
            login_info_field.destroy()
            login_info_field = None
        scan_card()
        draw_buttons(x_size/2,(y_size/2)+100)
    elif (login_method.get() == 1):
        draw_login_form(x_size/2,(y_size/2)+50)
        draw_buttons(x_size/2,(y_size/2)+100)
    else:
        draw_login_form(x_size/2,(y_size/2)+50)
        draw_buttons(x_size/2,(y_size/2)+100)

def get_user_info():
    x_pos = (x_size/5)+30
    y_pos = y_size/5
    global user_id,dor, first_name, last_name, email, phone_number, sex, dob, weight, calories_burned, energy_generated, points, card_id, login_data
    con = sqlite3.connect(db_path)
    cur = con.cursor()
    if not login_info_field  == None:
        login_data = login_info_field.get()
    if (login_method.get() == 2):
       cur.execute("SELECT * FROM users WHERE id= ?", (card_id,))
    elif (login_method.get() == 1):
        cur.execute("SELECT * FROM users WHERE Phone_Number= ?", (login_data,))
    else:
        cur.execute("SELECT * FROM users WHERE email= ?", (login_data,))

    (user_id, dor, first_name, last_name, email, phone_number, sex, dob, weight, calories_burned, energy_generated, points) = cur.fetchall()[0]
    draw_data(x_pos,y_pos)
    print("Retrieved user info")
    

def draw_buttons(x_pos, y_pos):
    login_button = Button(root, text = "Login", command = get_user_info)
    login_button.place(x = x_pos, y = y_pos, anchor ="center")
    print("Buttons generated")


def main():
    draw_decorations()
    choose_login_method()
    draw_labels((x_size/5)+30,y_size/5)
    
    root.mainloop()
    print(login_method.get())

main()
