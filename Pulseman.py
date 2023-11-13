# Lib imports
from rpi_lcd import LCD
import random
import string
import time

# Comp imports
from LCDUtil import *

# Inits
lcd = LCD()

# Loop
while(1):
    RANDl1 = ''.join(random.choice(string.ascii_uppercase) for _ in range(15))
    RANDl2 = ''.join(random.choice(string.ascii_uppercase) for _ in range(15))
    writeToLCD(lcd, RANDl1, 1)
    writeToLCD(lcd, RANDl2, 2)
    time.sleep(1)
