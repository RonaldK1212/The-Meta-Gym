import csv
import serial
import pathlib
import datetime
from re import L
import matplotlib.pyplot as plt
import random
from matplotlib.animation import FuncAnimation
from itertools import count
import pandas as pd

#===================================================================#
#                            FUNCTIONS                              #
#===================================================================#

x_values = []
y_values=[]

index = count()


filename = None


def create_filename(user_id, date): #Create unique numbered CSV file every time the program is run
    filename = str(str(user_id) + "_" + date + "_sensor_data.csv")
    return filename



def save_data(filename, header):   #writes data to csv file
    filepath = path / '..' / "Sensor Logs" / filename  
    data_file = open(filepath, 'w', newline='') #creates a new file in write mode 
    writer = csv.writer(data_file)
    ser.flush()
    with open(filepath, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
    while True:
        writer.writerow(read_serial())
        with open(filepath, 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            data = read_serial()
            info = {
                "Milliseconds": data[0],
                "Voltage": data[1]
            }

            writer.writerow(info)
            print(data)



def animate(i):
    data = pd.read_csv(filename)
    x_values = data["Milliseconds"] #Time in ms
    y_values = data["Voltage"]      #Voltage 

    plt.cla()
    plt.plot(x_values, y_values)
    plt.legend(loc='upper right')


ani = FuncAnimation(plt.gcf(), animate, interval=1)

plt.tight_layout()
plt.show()


def read_serial():  #reads serial input 
    data_string = ser.readline().decode('utf-8').rstrip()
    data_list = data_string.split(",")
    return data_list

#===================================================================#
#                            VARIABLES                              #
#===================================================================#


# SERIAL STUFF
#ser = serial.Serial('COM3', baudrate=9600, bytesize=8)  # open WINDOWS serial port
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=8)  # open LINUX serial port
date = datetime.datetime.now()  #gets current date
datestring = date.strftime("%y%m%d%H%M%S")  #formats date
path = pathlib.Path(__file__).parent.absolute() #gets current path
header = ["Milliseconds", "Voltage"] #csv columns/header

#save_data(create_filename("7162591", datestring), header)