import csv
import serial
import pathlib



#===================================================================#
#                            VARIABLES                              #
#===================================================================#

# SERIAL STUFF
ser = serial.Serial('COM3', baudrate=9600, bytesize=8)  # open WINDOWS serial port
#ser = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=8)  # open LINUX serial port
#x = ser.readline()
#x.decode('utf-8').rstrip()
#ser.close()

# CSV STUFF
filenumber = 0
filename = "sensor_data"+".csv"
data_file = open(filename, 'w', newline='')
writer = csv.writer(data_file)

#Filepath Stuff
path = pathlib.Path(__file__).parent.absolute()
filepath = path / "Sensor Logs" / filename


#===================================================================#
#                            FUNCTIONS                              #
#===================================================================#
#Create unique numbered CSV file every time the program is run

def save_data():
    writer = csv.writer(data_file)
    writer.writerow(["Millis","Pot Values"])
    while True:
        writer.writerow(read_serial())


def read_serial(): 
    data_string = ser.readline().decode('utf-8').rstrip()
    data_list = data_string.split(",")
    return data_list

def handler(signum, frame):
    data_file.close()
    print("DATA FILE SAVED AND CLOSED!")

save_data()