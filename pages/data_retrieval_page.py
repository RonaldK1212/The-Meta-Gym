from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import sqlite3
from datetime import datetime
import pathlib
import sys

sys.path.append('..')

from scan_card import scan_card
from retrieve_data import get

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
    
    (user_id, dor, first_name, last_name, email, phone_number, sex, dob, weight, cal,energy,points) = get.all(scan_card())


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
 


def main():
    draw_decorations()
    draw_labels((x_size/5)+30,y_size/5)
    root.mainloop()
    draw_data((x_size/5)+30,y_size/5)
    
    

main()
