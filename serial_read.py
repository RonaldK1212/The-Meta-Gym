import serial

ser = serial.Serial('COM3', baudrate=9600, bytesize=8)  # open WINDOWS serial port
#ser = serial.Serial('/dev/ttyACM0', baudrate=9600, bytesize=8)  # open LINUX serial port

print(ser.name)         # check which port was really used
i = 0
while True:
    x = ser.readline()
    print(x.decode('utf-8').rstrip())
    if i == 1000:
        ser.close()
    i+=1

