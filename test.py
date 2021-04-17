import discord
import RPi.GPIO as GPIO
from discord.ext import commands
from picamera import PiCamera
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer=6
bouton=23
led=5
GPIO.setup(led,GPIO.OUT)
GPIO.setup(bouton,GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(buzzer,GPIO.OUT)

DEFAULT = "poisson.jpg"
USER_IMG = "image.jpeg"
fichier = open("TOKEN.txt", "r")
TOKEN = fichier.read()
fichier.close()

class Bot(commands.Bot, discord.Client):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=";")
        self.add_command(commands.Command(self.poisson, name="poisson"))
        self.add_command(commands.Command(self.photo, name="photo"))

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")

    async def poisson(self, msg):
        try:
            file = discord.File(DEFAULT, filename=DEFAULT)
            await msg.channel.send("Neuneuil : ", file=file)
        except:
            await msg.channel.send("Erreur : la photo n'a pas pu être envoyée.")
        
    async def photo(self, msg):
        try:
            camera = PiCamera()
            camera.resolution = (1920, 1080)
            camera.rotation = 180
            camera.start_preview(fullscreen=False, window=(50, 50, 640, 480))
            sleep(5)
            camera.capture(USER_IMG)
            camera.stop_preview()
            camera.close()
            file = discord.File(USER_IMG, filename=USER_IMG)
            await msg.channel.send("Image de la rasberry : ", file=file)
        except:
            await msg.channel.send("Erreur : La camera n'est pas branchée")
            try:
                for i in range(3):
                    GPIO.output(buzzer,GPIO.HIGH)
                    sleep(1) # Delay in seconds
                    GPIO.output(buzzer,GPIO.LOW)
                    sleep(1)
            except:
                 await msg.channel.send("Erreur : le buzzer n'est pas branché.")
            try:
                file = discord.File(DEFAULT, filename=DEFAULT)
                await msg.channel.send("Voici votre image préféré de Neuneuil par défaut : ", file=file)
            except:
                await msg.channel.send("Erreur : la photo n'a pas pu être envoyée.")
            
disc_Bot = Bot()
disc_Bot.run(TOKEN)