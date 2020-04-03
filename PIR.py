import RPi.GPIO as GPIO
import time
from RPLCD import CharLCD
#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BOARD)

#set GPIO Pins
GPIO_TRIGGER = 16
GPIO_ECHO = 18

GPIO.setup(GPIO_TRIGGER, GPIO.OUT)

GPIO.setup(GPIO_ECHO, GPIO.IN)
lcd = CharLCD(numbering_mode=GPIO.BOARD,cols=16,rows=2,pin_rs=37, pin_e=35, p$
while True:
    #set GPIO direction (IN / OUT)

    GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER,False)
    while GPIO.input(GPIO_ECHO)==False:
        start = time.time()
    while GPIO.input(GPIO_ECHO)==True:
        end = time.time()
    slapsed_time=end-start
    distance = slapsed_time/0.000058
    distance1 = round(distance,4)
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Distance" )
    lcd.cursor_pos = (1, 0)
    lcd.write_string("{0} cm".format(distance1) )
    print("Distance: {0} cm".format(distance1))
        GPIO.output(GPIO_TRIGGER,True)
    time.sleep(0.0001)
    GPIO.output(GPIO_TRIGGER,False)
    while GPIO.input(GPIO_ECHO)==False:
        start = time.time()
    while GPIO.input(GPIO_ECHO)==True:
        end = time.time()
    slapsed_time=end-start
    distance = slapsed_time/0.000058
    distance1 = round(distance,4)
    lcd.cursor_pos = (0, 0)
    lcd.write_string("Distance" )
    lcd.cursor_pos = (1, 0)
    lcd.write_string("{0} cm".format(distance1) )
    print("Distance: {0} cm".format(distance1))
    time.sleep(2)
    lcd.clear()
