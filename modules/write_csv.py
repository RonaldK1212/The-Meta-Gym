import csv
import serial
import pathlib
import datetime
import sqlite3
from PyQt5 import QtWidgets, QtCore
from pyqtgraph import PlotWidget, plot
import pyqtgraph as pg
import sys  # We need sys so that we can pass argv to QApplication
import os
import pandas as pd
import numpy as np
#===================================================================#
#                            FUNCTIONS                              #
#===================================================================#

filename = None
filepath = None

def create_filename(user_id, date): #Create unique numbered CSV file every time the program is run
    filename = str(str(user_id) + "_" + date + "_sensor_data.csv")
    return filename


def create_file(filename, header):   #writes data to csv file
    filepath = path / '..' / "Sensor Logs" / filename  
    data_file = open(filepath, 'w', newline='') #creates a new file in write mode 
    writer = csv.writer(data_file)
    ser.flush()
    with open(filepath, 'w') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=header)
        writer.writeheader()
        
    ser.flush()
    return filepath

def save_data(filepath):
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

        writer.writerow(info)
    return data
           



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
ser = serial.Serial('/dev/ttyACM0', baudrate=115200, bytesize=8)  # open LINUX serial port
date = datetime.datetime.now()  #gets current date
datestring = date.strftime("%y%m%d%H%M%S")  #formats date
path = pathlib.Path(__file__).parent.absolute() #gets current path
header = ["Milliseconds", "Voltage"] #csv columns/header

def record_workout(filepath):
    ser.flush()
    class MainWindow(QtWidgets.QMainWindow):

        def __init__(self, *args, **kwargs):
            super(MainWindow, self).__init__(*args, **kwargs)
            
            self.graphWidget = pg.PlotWidget()
            self.setCentralWidget(self.graphWidget)
            self.graphWidget.setYRange(0, 1200)
            self.x = list(range(100))  # 100 time points
            self.y = [0 for _ in range(100)]  # 100 data points

            pen = pg.mkPen(color=(255, 255, 0))
            self.data_line =  self.graphWidget.plot(self.x, self.y, pen=pen)
                    # ... init continued ...
            self.timer = QtCore.QTimer()
            self.timer.setInterval(10)
            self.timer.timeout.connect(self.update_plot_data)
            self.timer.start()
            
        def update_plot_data(self):
            ser.flush()
            data = save_data(filepath)
            data = np.array(data, dtype=float)
            print(data)
            
            
            if(data[0] and (data[0] or data[0] == 0)):
                self.x = self.x[1:]  # Remove the first y element.
                self.x.append(self.x[-1]+1)  # Add a new value 1 higher than the last.


                self.y = self.y[1:]  # Remove the first
                self.y.append(data[0])  # Add a new random value.
            

            self.data_line.setData(self.x, self.y)  # Update the data.
            

            

    app = QtWidgets.QApplication(sys.argv)
    w = MainWindow()
    w.show()
    sys.exit(app.exec_())