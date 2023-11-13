# Lib imports
from rpi_lcd import LCD
import time
import serial
import json
from adafruit_servokit import ServoKit

# Comp imports
from LCDUtil import *

# Inits
lcd = LCD()
ser = serial.Serial ("/dev/ttyS0", 9600)
kit = ServoKit(channels=16)

# Glovars
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
            print("Command Recieved:")
            print(json.dumps(data, indent=4)) 
            print("")
            clearLCD(lcd) 
            writeToLCD(lcd, "cmd>" + data["type"], 1)
            writeToLCD(lcd, "writing to PCA", 2)
            kit.servo[0].angle = data["value"]["A"]["angle"]
            kit.servo[1].angle = data["value"]["B"]["angle"]
            ser.write("Aye Matey!\n\r".encode("utf-8"))
        except:
            ser.write("Nay Matey!\n\r".encode("utf-8"))
        finally:
            received_data = bytearray()
            newData = False

        
    time.sleep(2)