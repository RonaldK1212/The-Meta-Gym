import csv
from tkinter import E
from venv import create
import serial
import pathlib
import datetime

#===================================================================#
#                            FUNCTIONS                              #
#===================================================================#
#Create unique numbered CSV file every time the program is run

def create_filename(user_id, date):
    filename = str(user_id + date + "_sensor_data.csv")
    return filename

def save_data():
    writer = csv.writer(data_file)
    writer.writerow(header)
    while True:
        writer.writerow(read_serial())


def read_serial(): 
    data_string = ser.readline().decode('utf-8').rstrip()
    data_list = data_string.split(",")
    return data_list

def handler(signum, frame):
    data_file.close()
    print("DATA FILE SAVED AND CLOSED!")


#===================================================================#
#                            VARIABLES                              #
#===================================================================#

# SERIAL STUFF
ser = serial.Serial('COM6', baudrate=9600, bytesize=8)  # open WINDOWS serial port
#ser = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=8)  # open LINUX serial port
#x = ser.readline()
#x.decode('utf-8').rstrip()
#ser.close()

date = datetime.datetime.now()
datestring = date.strftime("%y%m%d%H%M%S")
user_id = "test"
# CSV STUFF
filename = create_filename(user_id, datestring)

data_file = open(filename, 'w', newline='')
writer = csv.writer(data_file)

header = ["Time (ms)","Encoder Counter", "RPM", "Voltage (mV)"]

#Filepath Stuff
path = pathlib.Path(__file__).parent.absolute()
filepath = path / "Sensor Logs" / filename




save_data()