def scan_card_f():
    import time
    card_id = None
    while True:
        print("Card scanner initiated")
        try:
            import RPi.GPIO as GPIO
            from mfrc522 import SimpleMFRC522
            reader = SimpleMFRC522()
            card_id = reader.read()[0]
        except:
            card_id = '999888777'
        finally:
            if card_id:
                time.sleep(0.1)
                print("Card scanned with ID: ", card_id)
                return card_id
            else:
                time.sleep(0.1)
            
def register_user(user_data): #adds user to database
    #TODO: get user data as tuple and export it to database as tuple    
    import sqlite3 as sql
    import pathlib 
    con = db()
    con.cursor().execute('INSERT INTO users VALUES (?,?,?,?,?,?,?,?,?,NULL,NULL,NULL)', user_data)
    con.commit()
    con.close()

def db():   #connects to database
    import sqlite3 as sql
    import pathlib
    path = pathlib.Path(__file__).parent.absolute()
    #print("Path = ",path)
    db_path = path / 'meta_gym.db'
    #print('Database path: ' + str(db_path))
    con = sql.connect(db_path)
    return con

def getUserData(user_id): #gets user information 
    import sqlite3 as sql
    data = []
    con = db()
    cur = con.cursor()
    user_id_int = int(user_id)
    cur.execute('SELECT * FROM users WHERE id = ?', (user_id_int,))
    #print(["Get user data (ID): ", user_id_int])
    data_tuple = cur.fetchall()
    for _ in data_tuple:
        data.append(_)
    return data

def getUserWorkouts(user_id): #gets list of ALL workouts
    import sqlite3 as sql
    data = []
    con = db()
    cur = con.cursor()
    cur.execute("SELECT filename,timestamp FROM sessions WHERE user_id = ?", (str(user_id),))
    data_tuple = cur.fetchall()
    for _ in data_tuple:
        data.append(_)
    print(data)
    return data

def displayWorkout(filename): #gets data of a SINGLE workout
    import pyqtgraph as pg
    import pandas as pd
    from pyqtgraph.Qt import QtCore, QtGui, QtWidgets
    import pathlib
    import csv
    import serial
    import datetime
    
    path = pathlib.Path(__file__).parent.absolute()
    filepath = path / "Sensor Logs"
    data = pd.read_csv(filepath / str(filename)) #gets workout data from file
    
    class DisplayWindow(QtWidgets.QMainWindow):
            def __init__(self, *args, **kwargs):
                super(DisplayWindow, self).__init__(*args, **kwargs)
                self.stopFlag = False
                self.graphWidget = pg.PlotWidget()
                self.setCentralWidget(self.graphWidget)
                self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                self.setGeometry(0,0,1024,600)
                
                self.toolbar = self.addToolBar("Close")
                self.button = self.toolbar.addAction("Close", self.closeWorkout)                
    
                self.y = data["Voltage"]

                n_series = pd.Series(self.y)
                r = 15
                windows = n_series.rolling(r)
                mov_avg = windows.mean()
                self.y = mov_avg.tolist()
                        

                pg.setConfigOptions(antialias=False)        
                self.graphWidget.addLegend()
                pen = pg.mkPen(color=(255,255,0), width = 1.5)
                self.data_line = self.graphWidget.plot(self.y, pen=pen, name="Voltage (mV)")
                self.graphWidget.setYRange(0, 4300)
                
            def closeWorkout(self):
                self.close()
                
    q = DisplayWindow()
    q.show()
    if(sys.flags.interactive != 1) or not hasattr(QtCore, 'PYQT_VERSION'):
        QtGui.QApplication.instance().exec_()


distance = 0
maxVoltage = 0

def recordWorkout(user_id):
    import csv
    import serial
    import pathlib
    import datetime
    import sqlite3
    from PyQt5 import QtWidgets, QtCore, QtGui
    from pyqtgraph import PlotWidget, plot
    import pyqtgraph as pg
    import sys  # We need sys so that we can pass argv to QApplication
    import os
    import pandas as pd
    import numpy as np
    
    filename = None
    filepath = None


    def create_filename(user_id, date): #Create unique numbered CSV file every time the program is run
        filename = str(str(user_id) + "_" + date + "_sensor_data.csv")
        return filename


    def create_file(filename, header):   #writes data to csv file
        filepath = path / "Sensor Logs" / filename  
        data_file = open(filepath, 'w', newline='') #creates a new file in write mode 
        writer = csv.writer(data_file)
        ser.flush()
        with open(filepath, 'w') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)
            writer.writeheader()
            
        ser.flush()
        return filepath
    
    def read_serial():  #reads serial input
        serialData = ser.readline()
        data_string = serialData.decode('utf-8', errors='ignore').rstrip()
        data_list = data_string.split(",")
        print(data_list)
        return data_list
    
    
    def save_data(filepath):
        with open(filepath, 'a') as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=header)

            data = read_serial()
            print(data)
                
            info = {
            #    "Milliseconds": int(data["Milliseconds"]),
                "Voltage": int(data[0])
            }

            writer.writerow(info)
        return data


    def postSessionData():
        con = db()
        cur = con.cursor()
        maxSpeed = ((((maxVoltage/1000) * 13.75/2) * 2108) * 60)/1000 #speed in KM/H
        cur.execute('UPDATE sessions SET end_time = (?), distance = (?), max_speed = (?), calories = (?) WHERE user_id = (?) and timestamp = (?)', (datetime.datetime.now(),distance,maxSpeed,distance * 0.03, user_id, date ))
        con.commit()
        con.close()

    
    #ser = serial.Serial('COM3', baudrate=9600, bytesize=8)  # open LINUX serial port
    ser = serial.Serial('/dev/ttyACM0', baudrate=115200, bytesize=8)  # open LINUX serial port
    date = datetime.datetime.now()  #gets current date
    datestring = date.strftime("%y%m%d%H%M%S")  #formats date
    path = pathlib.Path(__file__).parent.absolute() #gets current path
    #header = ["Milliseconds", "Voltage"] #csv columns/header
    header = ["Voltage"] #csv columns/header
    
    def record_workout(filepath):    
        ser.flush()
        class MainWindow(QtWidgets.QMainWindow):
            def __init__(self, *args, **kwargs):
                super(MainWindow, self).__init__(*args, **kwargs)
                self.stopFlag = False
                self.graphWidget = pg.PlotWidget()
                self.setCentralWidget(self.graphWidget)
                self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
                self.setGeometry(0,0,1024,600)
                self.graphWidget.addLegend()
                self.toolbar = self.addToolBar("End Workout")
                self.button = self.toolbar.addAction("End Workout", self.endWorkout)                
                #self.graphWidget.add
                self.x = list(range(100))
                self.y = [0 for _ in range(100)]

                pg.setConfigOptions(antialias=False)        
                
                pen = pg.mkPen(color=(255,255,0), width = 1.5)
                
                self.data_line = self.graphWidget.plot(self.x, self.y, pen=pen, name="Voltage (mV)", fillLevel=-0.3, brush=(255,255,0,50))
                
                self.graphWidget.setYRange(0, 4300)
                self.timer = QtCore.QTimer()
                self.timer.setInterval(50)
                self.timer.timeout.connect(self.update_plot_data)
                self.timer.start()
                
            def endWorkout(self):
                postSessionData()
                self.close()
                self.stopFlag = True
                #QtGui.QApplication.instance().quit()
            

            

            def update_plot_data(self):
                #ser.flush()
                global distance, maxVoltage
                if self.stopFlag is not True:
                    data = save_data(filepath)
                    data = np.array(data, dtype=float)
                    #print(data)
                    
                    if(data[0] and (data[0] or data[0] == 0)):
                        self.x = self.x[1:]  # Remove the first y element.
                        self.x.append(self.x[-1]+1)  # Add a new value 1 higher than the last.

                        n_series = pd.Series(self.y)
                        r = 15
                        windows = n_series.rolling(r)
                        mov_avg = windows.mean()
                        mov_avg_list = mov_avg.tolist()
                        

                        self.y = self.y[1:]  # Remove the first
                        self.y.append(data[0])  # Add a new value.
                    
                    self.data_line.setData(self.x, mov_avg_list)

                    voltage = data[0] / 1000

                    rpm = voltage * 13.75
                    distance = distance + (rpm/60000) * 2108 * 50 / 1000

                    if voltage > maxVoltage:
                        maxVoltage = voltage
                
                
        #app = QtWidgets.QApplication(sys.argv)
        w = MainWindow()
        w.show()
        #sys.exit(app.exec_())
        QtGui.QApplication.instance()#.exec_()
                
            

    
    con = db()
    cur = con.cursor()

    date = datetime.datetime.now()  #gets current date
    datestring = date.strftime("%y%m%d%H%M%S")  #formats date
    filename = create_filename(user_id, datestring)

    cur.execute("INSERT INTO sessions VALUES (?,?,?, NULL, NULL, NULL, NULL, NULL)", (filename, user_id, date))
    con.commit()
    con.close()

    filepath = create_file(filename, header)
    record_workout(filepath)

