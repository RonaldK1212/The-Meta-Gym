import csv
import serial
import pathlib
import datetime

#===================================================================#
#                            FUNCTIONS                              #
#===================================================================#


def create_filename(user_id, date): #Create unique numbered CSV file every time the program is run
    filename = str(user_id + "_" + date + "_sensor_data.csv")
    return filename

def save_data(filename, header):   #writes data to csv file
    filepath = path / "Sensor Logs" / filename  
    data_file = open(filepath, 'w', newline='') #creates a new file in write mode 
    writer = csv.writer(data_file)
    writer.writerow(header)
    while True:
        writer.writerow(read_serial())

def read_serial():  #reads serial input 
    data_string = ser.readline().decode('utf-8').rstrip()
    data_list = data_string.split(",")
    return data_list

def handler(signum, frame): #if ctrl+c was used to end the program, need to use another way
    #data_file.close()   #IMPORTANT !!! Required to use in the end
    print("DATA FILE SAVED AND CLOSED!")

#===================================================================#
#                            VARIABLES                              #
#===================================================================#

# SERIAL STUFF
#ser = serial.Serial('COM6', baudrate=9600, bytesize=8)  # open WINDOWS serial port
ser = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=8)  # open LINUX serial port

date = datetime.datetime.now()
datestring = date.strftime("%y%m%d%H%M%S")
#user_id = "test"

# CSV STUFF
#filename = create_filename(user_id, datestring)

#Filepath Stuff
path = pathlib.Path(__file__).parent.absolute() #gets current path





header = ["Time (ms)","Encoder Counter", "RPM", "Voltage (mV)"]

#save_data()