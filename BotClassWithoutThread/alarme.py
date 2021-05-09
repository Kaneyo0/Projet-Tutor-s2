class Alarme():
    def __init__(self, buzzer, led, bouton):
        self.buzzer = buzzer
        self.led = led
        self.bouton = bouton
    
    def activationAlarme(self, buzzer):
        for i in range(3):
            GPIO.output(buzzer,GPIO.HIGH)
            sleep(1)
            GPIO.output(buzzer,GPIO.LOW)
            sleep(1)
            
    def activationLed(self, led, bouton):
        while GPIO.input(bouton) == 1 :   
            buttonState = GPIO.input(bouton)
            GPIO.output(led, GPIO.HIGH)
            sleep(1)
            GPIO.output(led, GPIO.LOW)
            sleep(1)