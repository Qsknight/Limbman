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
received_data = bytearray()
newData = False

# Loop
while(1):
    while ser.in_waiting: 
        received_data.extend(ser.read())
        newData = True
        
    if newData:    
        # print(received_data) 
        try:
            data = json.loads(received_data.decode("utf-8")) 
            print("type:" + data["type"]) 
            clearLCD(lcd) 
            writeToLCD(lcd, "type:" + data["type"], 1)
            ser.write("Aye Matey!\n\r".encode("utf-8"))
        except:
            ser.write("Nay Matey!\n\r".encode("utf-8"))
        finally:
            received_data = bytearray()
            newData = False

        
    time.sleep(2)