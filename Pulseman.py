# Lib imports
from rpi_lcd import LCD
import time
import serial

# Comp imports
from LCDUtil import *

# Inits
lcd = LCD()
ser = serial.Serial ("/dev/ttyS0", 9600)
print(serial.__version__)
received_data = 0
newData = False

# Loop
while(1):
    while ser.in_waiting: 
        received_data += ser.read() 
        newData = True
        
    if newData:    
        print(received_data.decode("utf-8"))    
        writeToLCD(lcd, received_data.decode("utf-8"), 1)
        newData = False
        
    time.sleep(5)