from time import sleep
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer = 6
bouton = 23
led = 5
GPIO.setup(led, GPIO.OUT)
GPIO.setup(bouton, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer, GPIO.OUT)

class Alarme():
    def __init__(self, buzzer, led, bouton):
        self.buzzer = buzzer
        self.led = led
        self.bouton = bouton
    
    def activationAlarme(self, msg):
        for i in range(3):
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(0.8)
            GPIO.output(buzzer,GPIO.LOW)
            sleep(0.8)
    
    def activationLed(self, msg):
        while GPIO.input(bouton) == 1 :   
            GPIO.output(led, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(led, GPIO.LOW)
            sleep(0.5)
