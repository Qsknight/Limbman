# Lib imports
from rpi_lcd import LCD
import time
import serial
import json

# Comp imports
from LCDUtil import *

# Inits
lcd = LCD()
ser = serial.Serial ("/dev/ttyS0", 9600)
print(serial.__version__)
received_data = ""
newData = False

# Loop
while(1):
    while ser.in_waiting: 
        received_data += ser.read().decode("utf-8") 
        newData = True
        
    if newData:    
        # print(received_data) 
        data = json.loads(received_data) 
        print("type : " + data["type"]) 
        clearLCD(lcd) 
        writeToLCD(lcd, "type : " + data["type"], 1)
        received_data = ""
        newData = False
        
    time.sleep(5)