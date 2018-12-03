import RPi.GPIO as GPIO
import time
#this imports the libraries needed for the program

GPIO.setmode(GPIO,BOARD)
GPIO.setup(7,GPIO.OUT)
#this sets up the GPIO ports on the Raspberry Pi

while True:
    GPIO.output(7,True)
    time.sleep(.5)
    GPIO.output(7,False)
    time.sleep(.5)
    #this turns on and off the LED
