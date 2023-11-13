# Lib imports
from rpi_lcd import LCD
import time
import serial

# Comp imports
from LCDUtil import *

# Inits
lcd = LCD()
ser = serial.Serial ("/dev/ttyS0", 9600)

# Loop
while(1):
    received_data = ser.read() 
    if(received_data.decode("utf-8") == "A"):
        # time.sleep(0.1)
        # data_left = ser.inWaiting()
        # received_data += ser.read(data_left)
        print(received_data.decode("utf-8"))
        writeToLCD(lcd, received_data.decode("utf-8"), 1)
        #time.sleep(5)