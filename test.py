import discord
import RPi.GPIO as GPIO
from discord.ext import commands
from picamera import PiCamera
from time import sleep
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

buzzer=6
GPIO.setup(buzzer,GPIO.OUT)

class Bot(commands.Bot, discord.Client):

    def __init__(self):
        super(Bot, self).__init__(command_prefix=";")
        self.add_command(commands.Command(self.poisson, name="poisson"))
        self.add_command(commands.Command(self.photo, name="photo"))

    async def on_ready(self):
        print(f"{self.user.display_name} est connecté")

    async def poisson(self, msg):
        file = discord.File("poisson.jpg", filename="poisson.jpg")
        await msg.channel.send("Neuneuil : ", file=file)
        
    async def photo(self, msg):
        try:
            camera = PiCamera()
            camera.resolution = (1920, 1080)
            camera.rotation = 180
            camera.start_preview(fullscreen=False, window=(50, 50, 640, 480))
            sleep(5)
            camera.capture("image.jpeg")
            camera.stop_preview()
            camera.close()
            file = discord.File("image.jpeg", filename="image.jpeg")
            await msg.channel.send("Image de la rasberry : ", file=file)
        except:
            await msg.channel.send("Erreur : La camera n'est pas branchée")
            for i in range(3):
                GPIO.output(buzzer,GPIO.HIGH)
                sleep(1) # Delay in seconds
                GPIO.output(buzzer,GPIO.LOW)
                sleep(1)
            file = discord.File("poisson.jpg", filename="poisson.jpg")
            await msg.channel.send("Voici votre image préférée de Neuneuil par défaut : ", file=file)

disc_Bot = Bot()
disc_Bot.run("ODI3MTg3NTQ4ODMyMDA2MTc0.YGXYcA.aO9mCFxDP2L0qMocZ4rJc-h2-6M")
