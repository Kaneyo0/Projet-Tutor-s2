import RPi.GPIO as GPIO
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer=6
GPIO.setup(buzzer,GPIO.OUT)

for i in range(3):
    GPIO.output(buzzer,GPIO.HIGH)
    print ("Beep")
    sleep(1) # Delay in seconds
    GPIO.output(buzzer,GPIO.LOW)
    print ("No Beep")
    sleep(1)