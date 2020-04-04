import RPi.GPIO as GPIO
import time
import LoggerClass
from RPLCD import CharLCD
from datetime import datetime
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.IN)         #Read output from PIR motion sensor
GPIO.setup(12, GPIO.OUT)         #LED output pin
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16,rows=2,pin_rs=37, pin_e=35, pins_data=[33, 31, 29, 23])
counter = 0
persons = 0
value = 0
delay = 1
file_name = 'PIR.csv'
data_logger = LoggerClass.DataLogger(file_name)
lcd.clear()
def Detection(inp,sleeping,people,counter):
    if inp == 0:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("No detection.")
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Persons: {0}".format(people))
        time.sleep(sleeping)
        lcd.clear()
    if inp == 1:
        lcd.cursor_pos = (0, 0)
        lcd.write_string("Detecting... {0}s".format(counter))
        lcd.cursor_pos = (1, 0)
        lcd.write_string("Persons: {0}".format(persons))
        time.sleep(sleeping)
        
while True:
    i=GPIO.input(7)
    if persons == 10:
        break
    if i==0:                 #When output from motion sensor is LOW
        print ("No detection")
        GPIO.output(12, 0)  #Turn OFF LED
        Detection(i,delay,persons,counter)
        if value == 1:
            date = datetime.now()
            data_logger.log({'Date': date ,'Time': counter})
            persons += 1
            value = 0
        counter = 0
    if i==1:#When output from motion sensor is HIGH
        print ("Person detected")
        GPIO.output(12, 1)  #Turn ON LED
        Detection(i,delay,persons,counter)
        value = 1
        counter+=delay
data_logger.save()

