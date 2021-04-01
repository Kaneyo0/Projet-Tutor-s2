import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BOARD)
GPIO.setup(32,GPIO.OUT,initial=GPIO.LOW)
GPIO.setup(31,GPIO.IN,pull_up_down=GPIO.PUD_DOWN)
while True:
    etat = GPIO.input(31)
    if etat == 1:
        print("pushed")
        GPIO.output(32,GPIO.HIGH)
        sleep(1)
        GPIO.output(32,GPIO.LOW)
        sleep(1)
    
