from signal import signal, SIGTERM, SIGHUP, pause
from rpi_lcd import LCD

def safe_exit(signum, frame):
    exit(1)

def writeToLCD(lcd, content, line):
    signal(SIGTERM, safe_exit)
    signal(SIGHUP, safe_exit)
    lcd.text(content, line)

def clearLCD(lcd):
    lcd.clear()
        