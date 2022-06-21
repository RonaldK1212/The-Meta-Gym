import csv
import serial
import pathlib
import datetime
#from re import L
#import matplotlib.pyplot as plt
#import random
#from matplotlib.animation import FuncAnimation
#from itertools import count
#import pandas as pd

#===================================================================#
#                            FUNCTIONS                              #
#===================================================================#

# x_values = []
# y_values=[]
# index = count()
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
        ser.flush()
        with open(filepath, 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            
            data = read_serial()
            try:
                oldmillis = milliseconds
                oldvoltage = voltage
            except:
                oldmillis = 0
                oldvoltage = 0
                
                
            try:
                milliseconds = data[0]
                voltage = data[1]
            except:
                milliseconds = oldmillis
                voltage = oldvoltage
                
                
            info = {
                "Milliseconds": int(milliseconds),
                "Voltage": int(voltage)
            }


            print(voltage)
            writer.writerow(info)
           
# 
# def displayLive():
#     def animate(i):
# #         x_values.append(next(index))
# #         y_values.append(random.randint(-5,5))
# #         for x in range(len(y_values)):
# #             print(y_values[x])
# #         if(len(y_values) >= 10):
# #             y_values.pop(0)
# #             x_values.pop(0)
#             
#             
#         data = pd.read_csv(filename)
#         x_values = data["Milliseconds"] #Time in ms
#         y_values = data["Voltage"]      #Voltage 
# 
#         plt.cla()
#         plt.plot(x_values, y_values)
#         print("x_values", x_values, "y_values", y_values)
#         plt.legend(loc='upper right')
#         
#     ani = FuncAnimation(plt.gcf(), animate, interval=1000)
#     plt.show()




def read_serial():  #reads serial input
    serialData = ser.readline()
    data_string = serialData.decode('utf-8', errors='ignore').rstrip()
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