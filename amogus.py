import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

bouton=23
led=5
GPIO.setup(led,GPIO.OUT)
GPIO.setup(bouton,GPIO.IN, pull_up_down=GPIO.PUD_UP)


while GPIO.input(bouton) == 1 :   
    buttonState = GPIO.input(bouton)
    GPIO.output(led, GPIO.HIGH)
    sleep(1)
    GPIO.output(led, GPIO.LOW)
    sleep(1)



