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
    while ser.in_waiting: 
        received_data = ser.read() 
        print(received_data.decode("utf-8"), end='')
        writeToLCD(lcd, received_data.decode("utf-8"), 1)
    
    time.sleep(5)